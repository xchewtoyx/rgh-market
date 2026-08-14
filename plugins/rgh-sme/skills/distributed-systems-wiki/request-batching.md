---
type: concept
title: Request Batching and Idempotency
description: >
  Coalescing several requests into one network call amortizes fixed
  per-request overhead, but retrying a partially-applied batch is only safe
  if the receiver deduplicates.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 31, Request Batch"
---

# Request Batching and Idempotency

Many small requests each pay a fixed per-request cost — network latency plus
server-side (de)serialization — regardless of payload size, so a stream of
tiny requests sent independently hits that fixed cost as its throughput
ceiling well before bandwidth does. Batching accumulates several logical
requests client-side and ships them as one network call; the server unpacks
and processes each contained request individually and returns one combined
response, with the client resolving each original caller's own pending
result out of the batch reply. A batch is flushed on whichever of two
triggers fires first: accumulated size crossing a threshold, or the oldest
still-queued request having waited past a maximum latency budget — the
second trigger exists because a size threshold alone would stall
indefinitely under light traffic. Batching is commonly paired with [request
pipelining](request-pipeline.md) for further throughput gains, and is a
lower-level instance of the same idea as TCP's own Nagle's algorithm.

## The correctness hazard: partial application on retry

If a batch as a whole is retried after a partial failure — the network drops
the response but some contained requests already applied on the server — a
naive retry re-executes every request in the batch, including the ones that
already succeeded. This is exactly the retry-safety problem [idempotent
receiver](idempotency.md) solves in general terms; a batching client can
only retry safely if the receiver deduplicates each contained request by its
own id, not just the batch as a whole. Batch size itself is a tuned
parameter with diminishing and eventually negative returns at the high end
(megabyte-scale batches add processing overhead rather than reducing it),
which is a throughput-tuning question belonging to capacity and performance
work rather than a distribution-correctness one — the idempotency
requirement above is the part that's load-bearing for correctness.
