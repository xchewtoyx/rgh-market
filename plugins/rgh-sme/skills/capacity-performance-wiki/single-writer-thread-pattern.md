---
type: concept
title: Single-Writer Thread Pattern
description: Serializing all mutations of a piece of state through one dedicated thread reading from a queue eliminates lock contention on that state entirely, while a queue-plus-callback handoff keeps calling threads from blocking on the slower serialized work.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 13, Singular Update Queue"
---

State that many concurrent callers need to mutate safely (for example, an append-only log that must preserve write order) is usually protected with a lock, but locking has a real capacity cost — see [lock contention and synchronization overhead](lock-contention-overhead.md). Locking gets worse specifically when the protected work is slow (a disk write, a network call): every caller thread blocks for the full duration of that slow work while holding up the lock, wasting scheduler capacity on threads doing nothing but waiting.

## The Mechanism

Route all mutations through a bounded work queue drained by exactly one dedicated worker thread; no other thread ever touches the protected state directly. Calling threads do not block: each submits its request to the queue (an operation that returns immediately) and receives a future/callback that resolves once the single worker thread has actually processed it. This decouples "accepted" from "done" in the same way as a [request waiting list](request-batching-for-throughput.md) decouples send from completion.

Because exactly one thread ever mutates the state, there is no lock to contend for at all — the mutual-exclusion problem is eliminated structurally rather than managed with a faster lock. This is the same idea as the LMAX Disruptor's **Single Writer Principle**: removing mutual exclusion overhead entirely by construction, rather than trying to make the lock cheaper.

## Capacity Trade-Offs

*   **Throughput ceiling becomes single-threaded.** Because only one thread ever does the actual mutation, that thread's own processing rate is now the hard ceiling on throughput for this piece of state — the pattern trades away multi-core parallelism on the protected state in exchange for removing contention overhead. It is a good trade only when the serialized work itself is cheap enough (or can be made cheap enough via [batching](request-batching-for-throughput.md)) that single-thread throughput is sufficient for the workload; if the protected work is CPU-heavy, this pattern shifts the bottleneck to [CPU saturation](use-method.md) on a single core rather than resolving it.
*   **Queue choice determines backpressure behavior.** A bounded queue (blocking producers once full) provides natural backpressure against a slow worker; an unbounded queue avoids blocking producers but risks unbounded memory growth if the worker falls behind — the same trade as any producer/consumer buffer.
*   **Never block the worker thread on external I/O.** If the single worker's task needs to call another service, that call must be issued asynchronously and its result fed back into the queue as a new work item — blocking the sole worker thread on a slow external call stalls the entire serialized stream behind it, turning a local contention problem into a much larger latency problem for every other caller.

## When to Reach for This vs. Partitioning

This pattern helps when the state genuinely must stay single-threaded (ordering guarantees, a single log). When the state can instead be split so each partition has its own owner, [partitioning/sharding](horizontal-vs-vertical-scaling.md) removes the single-thread throughput ceiling entirely by giving each partition its own single-writer thread running in parallel — the general mitigation this pattern is a specific instance of.
