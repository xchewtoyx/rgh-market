---
type: concept
title: Write Buffering for Latency
description: >
  Acknowledging writes from an in-memory buffer instead of the storage
  engine trades a bounded durability risk for a large cut in tail latency,
  and composes with replica quorums to bound that risk without slowing the
  write down.
sources:
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §6.1"
---

# Write Buffering for Latency

A storage node can hold an in-memory **object buffer**: each write lands in
the buffer first and a background writer thread periodically flushes it to
the storage engine, while reads check the buffer before falling through to
storage. This is the same [flush trade-off](write-ahead-log.md) every durable
log faces — delaying the disk write improves throughput and latency at the
cost of losing unflushed entries on crash — applied per-node in a replicated
store rather than to a single log.

The effect can be large for a small cost: in Dynamo's production measurements,
a buffer of only a **thousand objects** cut 99.9th-percentile write latency by
a **factor of 5** during peak traffic, and also smoothed out the tail's
variance (see [tail latency amplification](tail-latency-amplification.md) for
why the tail, not the average, is the metric that matters here). The risk is
concrete: a node crash loses any writes still sitting in the buffer,
unflushed.

## Bounding the risk with the replica quorum

Because the object lives on multiple replicas anyway (see [quorum reads and
writes](quorum-reads-and-writes.md)), the durability risk doesn't have to be
carried by every replica equally. The coordinator handling a write can
designate **one of the n replicas** to perform a "**durable write**" —
writing straight to storage, bypassing its buffer — while the rest buffer
normally. Since the coordinator only waits for **w** responses before
acknowledging the client, and w is normally less than n, the slower
durable-write replica doesn't gate the write's latency as long as the other
buffered replicas respond in time. The result: most replicas get the latency
win, one replica anchors durability, and the client-visible latency tracks
the buffered replicas rather than the durable one.
