---
type: concept
title: Singular Update Queue
description: >
  Funnel concurrent callers through one queue drained by exactly one worker
  thread, so state mutation stays single-threaded and correct without
  blocking callers on slow work like disk writes.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 13, Singular Update Queue"
---

# Singular Update Queue

A [leader](leader-election.md) handling a [replicated log](replicated-log.md)
must parse client requests, append to its [write-ahead
log](write-ahead-log.md) (durable, therefore slow), and process replication
acknowledgements from followers to advance the [high water
mark](high-water-mark.md) — all against shared state, under concurrent
callers, without racing. Locks are the obvious tool, but locking around slow
work (a disk write) blocks every caller thread until it completes, which
kills throughput under load.

The fix: one work queue, and exactly one dedicated worker thread draining it.
Any number of caller threads submit concurrently and get back a future
immediately, without blocking each other; only the single worker thread ever
touches the protected state, applying one handler function per item in
order. This keeps the core state-mutation logic single-threaded — trivially
correct, no locks needed — while remaining responsive, because submission
itself never blocks. Go's channels-plus-goroutines and similar
lightweight-thread/channel primitives (Kotlin) give this shape natively: all
requests funnel into one shared channel, a single goroutine processes them,
and responses go out on separate channels.

## Queue choice governs backpressure

- A **bounded, blocking** queue (e.g. Java's `ArrayBlockingQueue`, used in
  Kafka's request queue) makes a fast producer block once the queue is full —
  natural backpressure against a slow consumer, at the cost of stalling
  callers under sustained overload.
- An **unbounded** queue (Zookeeper, Kafka's response queue) never blocks the
  producer but can exhaust memory if nothing else limits the rate of
  incoming work.
- A queue with no dedicated waiting consumer (Akka Actors' mailbox, backed by
  `ConcurrentLinkedQueue` plus a thread pool) schedules consumption only once
  work has actually been queued.
- Latency-sensitive pipelines that can't tolerate even a blocking queue's
  copy overhead between stages use a lock-free ring buffer (the LMAX
  Disruptor), following the related **Single Writer Principle**: avoid
  mutual exclusion entirely by ensuring only one thread ever writes a given
  piece of state.

## Two rules for keeping the worker thread free

- **Never chain slow work onto the worker thread itself.** If a result needs
  a further stage (write to the log, then send a response over a socket),
  run that continuation on a separate thread or hand it to a further
  singular update queue — never inline it where it would block the sole
  worker.
- **Never touch protected state from an external callback.** If the queue's
  handler needs to call another service and use the response to update
  state, that call must be asynchronous, and its completion callback (which
  runs on a different thread) must not mutate the protected state directly —
  it must feed its result back into the queue as an ordinary new work item.
  Skipping this reintroduces the exact concurrency bug the pattern exists to
  prevent.

Because callers wait on a returned future rather than blocking synchronously,
this pattern pairs directly with a [request waiting
list](request-waiting-list.md) for correlating asynchronous peer responses
back to the original caller. Real systems: ZooKeeper's `SyncRequestProcessor`
and etcd's Raft goroutine both serialize updates this way; Kafka's Controller
and Cassandra's gossip state updates (SEDA-style single-threaded stages) use
the same shape.
