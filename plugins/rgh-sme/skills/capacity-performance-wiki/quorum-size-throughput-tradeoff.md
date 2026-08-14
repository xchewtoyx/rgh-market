---
type: concept
title: Quorum Size vs. Write Throughput Trade-Off
description: Requiring more replicas to acknowledge a write before it counts as durable buys higher failure tolerance but degrades write throughput non-linearly, which is why real quorum-based systems converge on cluster sizes of three or five rather than scaling replica count up freely.
sources:
  - title: "Patterns of Distributed Systems"
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 10, Quorum"
---

In a replicated system where a write is only considered durable once a majority (**quorum**) of `n` nodes have acknowledged it, quorum size is `n/2 + 1`. Growing `n` therefore buys failure tolerance — a cluster tolerates `f` simultaneous failures once sized to `2f + 1` — but every additional node in the quorum also adds a participant that must respond before the write can complete, and write latency is bounded by the slowest quorum member.

## The Throughput Cost Is Non-Linear

Quorum-based write throughput degrades faster than linearly as cluster size grows — cited analysis puts the degradation at roughly `O(1/n²)`, and observed behavior in production consensus systems (Zookeeper and others) shows markedly lower write throughput once cluster size exceeds five nodes. As a rough rule of thumb, doubling cluster size roughly halves write throughput. This is the same underlying phenomenon as the coordination-overhead term in the [Universal Scalability Law](universal-scalability-law.md): each additional coordinating participant adds pairwise synchronization cost, not just a constant per-node overhead.

## Failure Tolerance Doesn't Scale Smoothly Either

The tolerance side of the trade-off is lumpy, not smooth: going from a 3-node to a 4-node cluster buys *no* additional failure tolerance at all — quorum for `n=3` is 2 (tolerates 1 failure), and quorum for `n=4` is still 3 (still tolerates only 1 failure). The next actual gain in tolerance requires jumping all the way to 5 nodes. This means an even-sized cluster is strictly worse than the next-smaller odd size: it pays the throughput cost of an extra node without buying any extra tolerance.

## Practical Sizing Conclusion

Because the throughput cost is non-linear and the tolerance gain is lumpy, real quorum-based systems overwhelmingly converge on cluster sizes of **three or five** rather than scaling replica count up as a general lever for durability. A five-node cluster tolerates two failures while still sustaining on the order of a few thousand writes per second — enough for most workloads — whereas larger clusters trade away throughput for failure tolerance most workloads don't need. When more durability margin is wanted, the better lever is usually [N+M redundancy](n-plus-m-redundancy.md) applied at a coarser level (extra standby capacity, multiple independently-quorumed shards) rather than inflating a single quorum's size.

This same reasoning governs partition replica counts generally: [fixed partition count as a scaling ceiling](fixed-partition-count-scaling-ceiling.md) and [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) both assume each partition's own replica set stays small for exactly this reason — replicating a partition to more nodes for extra safety margin has a direct write-throughput cost that must be weighed against the tolerance gained.

This note covers a *fixed* majority quorum, sized once for the whole cluster. Some systems instead expose replica count and read/write quorum size as three independently tunable numbers, chosen per use case rather than fixed cluster-wide — see [tunable per-request quorum (N/R/W)](tunable-per-request-quorum-nrw.md) for that variant and the counter-intuitive way it decouples durability from availability.
