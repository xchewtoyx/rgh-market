---
type: concept
title: Derived Data vs. Distributed Transactions
description: >
  Why CDC- and event-driven pipelines keeping secondary stores in sync won
  out over distributed transactions as the way to update multiple systems
  from one change.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

An application that needs a change to land consistently in several
specialized stores at once — an OLTP database, a search index, a cache, a
warehouse — has two structurally different ways to keep them in sync.

**Distributed transactions** (two-phase commit / XA) synchronously
coordinate the write across every participating system using locks and an
atomic commit protocol, so either every store gets the change or none does.
This gives strong consistency, but at a steep operational cost: every
participant must stay available and responsive for the whole transaction, a
coordinator failure can leave participants blocked holding locks
indefinitely, and throughput is capped by the slowest participant in the
protocol. In practice this makes distributed transactions fragile and
expensive to run at the scale most analytical pipelines operate at.

**Derived data systems** — the pattern behind
[change data capture](change-data-capture.md) and
[event sourcing](transactional-outbox-pattern.md) — instead treat the
downstream stores as followers, asynchronously fed from a durable write log.
A change is written once (usually to the system of record), captured as an
event, and applied to every derived store independently and at its own pace,
using processors that are deterministic and
[idempotent](idempotent-and-replayable-jobs.md) so a redelivered or
reordered event doesn't corrupt derived state. Faults stay local: a failure
in one derived store's consumer doesn't block the write to the system of
record, or to any other derived store — it just leaves that one store
temporarily behind, catching up once the consumer recovers, rather than
propagating backpressure or blocking failure across every participant the
way two-phase commit does.

This is the concrete reason CDC- and event-driven pipelines, not distributed
transactions, are the default way data engineering keeps a warehouse, a
search index, and a cache all reflecting the same underlying source: giving
up synchronous, all-or-nothing consistency in exchange for independent
failure domains and much higher throughput is, for nearly every analytical
pipeline's actual requirements, a trade worth making.
