---
type: concept
title: Request Pipeline
description: >
  Sending the next request before the previous response arrives, to stop a
  single-socket channel from sitting idle between round trips — and the
  reordering hazard that pipelining introduces under retry.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 32, Request Pipeline"
---

# Request Pipeline

Over a [single socket channel](single-socket-channel.md), waiting for each
response before sending the next request under-utilizes both the network
and the receiver: a server backed by a [singular update
queue](singular-update-queue.md) can keep accepting and queuing new work
while it's still processing an earlier request, but a client sending
one-at-a-time leaves that capacity idle regardless. The fix is to decouple
sending from receiving with two separate concerns per connection — one path
that fires requests without blocking for a response, one that reads
responses as they arrive — trusting the transport (TCP) to preserve
delivery order even though the sender no longer waits in lockstep with it.

This is also the direct fix for the head-of-line blocking [single socket
channel](single-socket-channel.md) and [heartbeat](heartbeat.md) both
describe: a heartbeat queued behind a slow request no longer has to wait for
that request's full round trip to complete first.

## Two problems pipelining introduces

- **Overwhelming the receiver.** Sending without any limit can flood the
  receiving node faster than it can process. The fix is capping the number
  of in-flight (sent but unacknowledged) requests per connection — a small
  constant such as 5 — and having the sender block once that cap is
  reached, which throttles it naturally without an explicit protocol for
  the receiver to signal back-off.
- **Reordering under retry.** If an early request fails and is retried
  while a later request (sent after it) already succeeded and was
  processed, the server can end up applying the later request before the
  retried earlier one — silently reordering effects, exactly the kind of
  duplicate/reorder hazard [idempotency](idempotency.md) and [effectively
  once delivery](effectively-once-delivery.md) exist to prevent, but sharper
  here because *order* is at stake, not just duplication. This has to be
  actively prevented: Raft has every replication request name the previous
  log index it expects, rejecting the request outright on a mismatch and
  forcing the sender to resync from the correct point (the same conflict
  check described in [replicated log](replicated-log.md)); Kafka's
  idempotent producer instead attaches a unique id plus a monotonically
  increasing sequence number to each batch, and the broker rejects anything
  that arrives out of the expected sequence.

Pipelining is also what makes [idempotent receiver](idempotency.md)'s
response-caching bound trickier: if the protocol allows several requests
in flight at once, the server must retain as many cached responses as the
maximum possible number of in-flight requests, not just the single most
recent one. Zab and Raft both support pipelining as described; Kafka's wire
protocol explicitly documents and encourages it for throughput.
