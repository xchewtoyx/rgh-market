---
type: concept
title: Queue as Load Buffer
description: >
  Placing a message queue between a fast producer and a rate- or
  capacity-limited consumer decouples their speeds and lets you tune worker
  parallelism to protect downstream systems.
sources:
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 6"
---

# Queue as Load Buffer

A [transient message broker](message-brokers.md) between two stages turns
bursty production into steady consumption: the producer enqueues as fast as
it can (or as fast as an cheap upstream API allows), and workers pull at a
rate the downstream can sustain. This is the predictable-load property of
queueing architecture used deliberately — not only to survive spikes, but to
**cap parallelism** so a shared database or third-party API is not
overwhelmed.

## Rate-limited downstream APIs

A common shape splits **enumeration** from **detail fetch**:

1. A producer calls a cheap list endpoint (e.g. `/items` returning hundreds
   of IDs per call) and enqueues one message per item needing further work
   (e.g. `GET /items/{id}`).
2. Downloader workers dequeue and call the expensive, rate-limited API.
3. Workers read rate-limit headers after each call (e.g.
   `X-Ratelimit-Usage: 2142,3000`) and **stop dequeuing** when usage nears a
   threshold (often ~90% of quota), resuming after the provider's reset
   window.

The queue holds the backlog while workers idle during the rate-limit window;
adding workers raises throughput only until the external quota binds —
the buffer absorbs the mismatch between "how fast can I discover work" and
"how fast may I execute it." The same [pull-based](push-vs-pull-consumption.md)
consumption model lets each worker self-throttle without central coordination.

This pattern is distinct from [write buffering for latency](write-buffering-for-latency.md)
(replica-side durability trade-offs) and from broker-level flow control: here
the application uses queue depth plus a fixed worker count as an explicit
**admission controller** for an external dependency.
