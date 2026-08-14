---
type: concept
title: Asynchronous Offload for Capacity
description: Moving heavy computational or I/O work out of the synchronous request path and into background workers, trading immediate completion for a smaller, more predictable synchronous capacity footprint.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 9"
---

**Asynchronous offload** is a capacity pattern where heavy computational or I/O-bound work is removed from the synchronous request-handling path and pushed onto a message queue (e.g., RabbitMQ, Kafka) for background workers to process independently.

## Effect on Capacity

Offloading changes the capacity profile of the synchronous tier rather than eliminating the work:

*   The request-handling tier's per-request service time shrinks to just "enqueue the work," so it can sustain far higher request throughput with the same resources — by the [Utilization Law](utilization-law.md), a shorter service time directly raises the maximum throughput a given number of servers can sustain.
*   The heavy work still has to happen somewhere; it now consumes capacity on the worker tier, on a schedule the worker tier controls rather than at the rate requests arrive. This decouples the *arrival rate* the synchronous tier must absorb from the *processing rate* the underlying work actually requires, buffered by the queue.
*   The queue itself becomes a capacity-relevant component: if the worker tier's processing rate falls behind the enqueue rate for a sustained period, the queue grows without bound, and now the queue's own storage and the request's real end-to-end completion time (not just the synchronous acknowledgment) become the capacity constraint.

## Trade-Off

Offloading trades **immediate completion** for a **smaller, more predictable synchronous footprint**: the client's synchronous request now only waits for enqueue latency, not the full processing time, but any part of the workflow that needs the *result* of the offloaded work (rather than just an acknowledgment that it was queued) must poll or be notified asynchronously — pushing complexity from capacity sizing into workflow design.
