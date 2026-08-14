---
type: concept
title: Concurrency Limiting as Admission Control
description: Deliberately capping how many requests a downstream resource is allowed to work on at once, queuing the rest, can raise overall throughput compared to letting unlimited concurrency reach that resource — because past a resource's optimal concurrency, additional simultaneous work adds contention overhead instead of useful progress.
sources:
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 12"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §6.5"
---

It seems intuitive that letting more requests reach a backend resource at once should only help throughput — more work in flight, more getting done. Past a certain point this stops being true: a resource has an optimal level of concurrent work, and pushing more concurrent requests at it beyond that point adds coordination and contention overhead ([lock waits](lock-contention-overhead.md), context switching, cache thrashing) that competes with the resource's own useful work, so *effective* throughput falls even as *offered* concurrency rises.

## The Mechanism

A component sitting in front of the constrained resource — a database proxy, a connection pool, an API gateway — can enforce a hard cap on how many requests are allowed through to the resource concurrently, queuing any request beyond that cap rather than forwarding it immediately. Counterintuitively, this can *increase* the resource's overall throughput relative to letting all offered concurrency through directly, at the cost of adding queueing latency for the requests now waiting in front of the cap instead of contending behind it.

This is consistent with the shape of the [M/M/1 queue model](mm1-queue-model.md) and [Little's Law](littles-law.md): a resource has a throughput-maximizing operating point, and concurrency beyond that point buys queueing delay, not additional completed work. The admission-control component is deliberately choosing to hold that extra concurrency in a queue *in front of* the resource — where it adds only queueing latency — rather than letting it reach the resource itself, where it would add contention that degrades the resource's throughput for every request, including the ones that were already in flight.

## When the Trade-Off Pays Off

*   The queueing delay added at the admission-control point must be smaller than the throughput loss avoided by not letting excess concurrency reach the resource directly — this is a property of the specific resource's own concurrency/throughput curve, not a universal constant, and needs to be measured (e.g., via [capacity testing](capacity-test-types.md)) rather than assumed.
*   It's most valuable for resources whose internal concurrency-handling has a sharp knee — where throughput degrades noticeably past some point — rather than resources that degrade gracefully, since a gently-degrading resource has less to gain from external admission control.

This is a preventive measure for a resource that is *healthy but nearing its limit*. Once a resource has already crossed into failure, the better response shifts from queueing excess concurrency to a [circuit breaker](circuit-breaker-pattern.md) that stops sending it work entirely for a cooldown period. A related but more proactive alternative, when both ends of the call can cooperate, is [backpressure](backpressure-and-handshaking.md) — having the downstream communicate its capacity so the upstream slows its own sending rate, rather than the downstream unilaterally queueing whatever arrives.

## Related Application: Throttling Administrative Load

The same principle applies to large, non-request-driven operations sharing a resource with normal traffic — a bulk schema migration or data backfill, for instance. Running such an operation at full, unthrottled speed can saturate the same I/O capacity that foreground transactions depend on, degrading latency for all transactions and risking cascading failure. Deliberately throttling the batched operation's own concurrency or rate — accepting that the migration itself takes longer — protects the shared resource's throughput for foreground traffic, the same trade this note describes applied to a one-off operation instead of steady-state request traffic. Persistently elevated I/O latency that tracks a running administrative operation is a concrete signal that this throttling is missing or insufficient.

### A Concrete Feedback-Loop Mechanism

One production implementation of this pattern (Dynamo's handling of background replica-synchronization and data-handoff work competing with foreground reads/writes) makes the throttle dynamic rather than a fixed static rate: background work is granted a pool of runtime "slices" of the shared resource, and a controller continuously monitors foreground-path health signals — disk-operation latency, failed accesses from lock contention or transaction timeouts, request-queue wait times — over a trailing window (e.g., the last 60 seconds). The controller compares a chosen percentile of a chosen signal (e.g., p99 database read latency) against a preset threshold, and grows or shrinks the number of slices available to background work based on how close that trailing percentile is to the threshold. This keeps the throttle self-adjusting to actual foreground impact rather than requiring an operator to guess a fixed safe rate for background work up front, and it directly ties the admission-control decision to a [percentile](latency-percentiles-vs-mean.md), not an average, so a background task that's fine on average but occasionally spikes foreground tail latency still gets throttled back.
