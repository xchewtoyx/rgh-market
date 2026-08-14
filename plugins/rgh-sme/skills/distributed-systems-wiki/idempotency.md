---
type: concept
title: Idempotency
description: >
  Making an operation safe to apply multiple times with the effect of once —
  the property that makes retries safe on a network where success is
  unknowable.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 15, Idempotent Receiver"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §6.1.1"
---

# Idempotency

An operation is idempotent if performing it several times has the same
effect as performing it once. This is the keystone of retry safety: on an
[unreliable network](unreliable-networks.md), a missing response never
distinguishes "not done" from "done, ack lost", so every
[timeout-triggered](timeouts-and-failure-detection.md) retry risks a
duplicate. If the operation is idempotent, retrying is always safe and
at-least-once delivery upgrades to
[effectively-once processing](effectively-once-delivery.md).

Ways to get it:

- **Naturally idempotent operations:** setting a key to a value, deleting by
  id. `increment by 1` is not — design APIs toward absolute assignments
  where possible.
- **Idempotency keys / deduplication:** the client attaches a unique
  operation id; the receiver records processed ids and ignores repeats. The
  id store must be as durable as the effect it guards. Checking that store
  on every delivery gets expensive at high volume, so MillWheel fronts it
  with a **Bloom filter** of previously-seen ids: a filter miss proves the
  id is genuinely new (skip the durable store, cheap fast path), while a
  filter hit only means "maybe seen before," so it falls through to the
  authoritative store to confirm — trading a small, tunable false-positive
  rate (which merely costs an unnecessary store lookup, never a wrong
  dedup decision) for avoiding that lookup on the common case. Retained ids
  are garbage-collected once every possible retry window has passed —
  ordinarily within minutes of the original delivery, stretched by an
  explicit slack value (hours, typically) for sources known to redeliver
  late data.
- **Offset/token tagging:** tag writes with a monotonically increasing
  position — e.g. a [log](log-based-messaging.md) consumer includes the
  message offset with the state it writes, so a replayed message overwrites
  identically instead of double-applying. ([Fencing
  tokens](fencing-tokens.md) use the same monotonic-token idea for
  authority rather than deduplication.)

Idempotence must hold *end to end*: a retried request that is deduplicated
by the server but re-triggers an email, payment, or downstream message is
not idempotent where it matters (see
[transaction retries](transaction-aborts-and-retries.md)). Assume every
delivery mechanism will occasionally duplicate; build consumers so that's
boring.

## The Idempotent Receiver mechanism

A concrete pattern for the "idempotency keys" technique above, used by
[replicated log](replicated-log.md) leaders (Raft's reference implementation,
Kafka's idempotent producer): the client first **registers** with the leader
and receives a unique client id — in a [consensus](consensus.md)-backed
system this can just be the [write-ahead log](write-ahead-log.md) index of
the registration entry itself, since registration is replicated through the
same log and so survives [failover](leader-failover.md). Every subsequent
request from that client carries its client id plus a client-assigned,
monotonically increasing request number. The server keeps a small ring of
recent (client id, request number) → response pairs per client; before
executing an incoming request it checks whether a response is already
recorded for that pair and, if so, returns the cached response instead of
re-executing.

This distinction matters more than it looks: setting a key to a value is
naturally idempotent, so a retry is harmless either way — but *creating* a
[lease](distributed-locks.md) is not, since a second identical create-lease
call must legitimately fail with "duplicate," which is exactly the wrong
answer if the first call actually succeeded and only its *response* was
lost. Without per-request dedup, the retrying client would misread that
duplicate-error as "I never got the lease" when it actually holds it. Two
complementary approaches keep the cached-response ring bounded: the client
tracks the highest request number it has already received a response for and
sends that along with new requests, letting the server discard everything
below it; or, when the protocol allows several requests in flight at once
(see [request pipelining](request-pipeline.md)), the server retains as many
cached responses as the maximum possible number of in-flight requests
(Kafka's producer allows 5 in-flight requests, so brokers cache the last 5
responses per client).

Two explicit limits of this scheme: it only dedupes retries from connection
failures on a still-alive client — a client process that crashes and
restarts re-registers as a new client id and loses all prior deduplication —
and it has no visibility into *application-level* duplicates (the same
logical action issued twice with two different request numbers), which
remains the application's problem to solve.
