---
type: concept
title: Sloppy Quorum and Hinted Handoff
description: >
  Accepting writes on reachable non-home replicas during a partition, then
  forwarding them home later — better write availability at the cost of the
  quorum overlap guarantee.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.6"
---

# Sloppy Quorum and Hinted Handoff

In a large [leaderless](leaderless-replication.md) cluster, a network partition
can cut a client off from the n "home" replicas for a key while other nodes
remain reachable. The system faces a choice: fail writes, or accept them on w
nodes that are reachable but not among the key's home nodes.

The latter is a **sloppy quorum**. When the partition heals, the stand-in
nodes forward the writes to the proper home nodes — **hinted handoff**
("you're back, here's what I held for you").

Consequences:

- Write availability improves dramatically: the system accepts writes as long
  as *any* w nodes are reachable.
- The [w + r > n overlap guarantee](quorum-reads-and-writes.md) is void while
  handoff is pending: a read quorum against the home nodes can miss writes
  sitting on stand-ins. A sloppy quorum is an availability mechanism, not a
  consistency one.

Optional in Riak (enabled by default), Cassandra, and Voldemort (disabled by
default). Enable it when write availability during partitions matters more
than read freshness.

## Mechanics (Dynamo)

A stand-in node keeps a handed-off replica in a **separate local database**
from its own resident keys, and scans it periodically; once it detects the
intended home node has recovered, it delivers the replica there and, once
the transfer succeeds, may delete its own copy without ever having reduced
the number of replicas the system held in the meantime. This works well
specifically because failures are usually transient — a stand-in holding a
hint for a long-departed node just accumulates unhandoffable state.

Taken to its extreme, setting **w = 1** gives the most available write
policy possible: a write succeeds as long as a single node anywhere in the
system durably stores it locally, and is rejected only if literally every
node is unreachable. Production systems rarely run this low in practice,
since it trades away most of the durability quorum writes are meant to
provide — but it marks the availability ceiling the mechanism makes
reachable.

Sloppy quorums also compose with **cross-datacenter replication**: if a
key's preference list is deliberately spread across multiple datacenters
(connected by high-speed links), the same mechanism that tolerates a single
unreachable node also tolerates an entire datacenter going dark — reads and
writes keep succeeding against the other datacenters' replicas, with hinted
handoff reconciling once the failed datacenter returns.
