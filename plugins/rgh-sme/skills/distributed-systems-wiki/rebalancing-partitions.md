---
type: concept
title: Rebalancing Partitions
description: >
  Moving partitions between nodes as the cluster grows, shrinks, or fails —
  minimizing data movement while keeping load fair, and the case for a human
  in the loop.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
---

# Rebalancing Partitions

When nodes are added or removed, [partitions](partitioning.md) must move to
keep load fair — while the database keeps serving traffic, and while moving as
little data as possible (moves consume network and I/O the cluster needs for
its real work).

**The anti-pattern: `hash(key) mod N`.** Going from N to N+1 nodes changes
the placement of *almost every key*, triggering a cluster-wide reshuffle.
Never couple placement directly to node count.

Strategies that move only what's needed:

- **[Fixed partitions](fixed-partitions.md).** Create far more partitions
  than nodes up front (e.g. 1,000 partitions on 10 nodes); a joining node
  *steals a few whole partitions* from each existing node. Partition-to-key
  mapping never changes, only partition-to-node. Simple and widely used
  (Riak, Elasticsearch, Couchbase, Voldemort); the catch is choosing the
  count — it caps cluster size, and both too-large and too-small partitions
  are costly when the dataset's future size is unknown.
- **Dynamic partitioning.** Partitions split when exceeding a size threshold
  (e.g. 10 GB in HBase) and merge when shrinking — the count adapts to the
  dataset. Natural for [key-range partitioning](key-range-partitioning.md).
  Caveat: an empty database is one partition on one node until enough data
  accumulates to split — mitigated by **pre-splitting** initial ranges.
- **Partitions proportional to nodes.** A fixed number of partitions *per
  node* (Cassandra: 256 vnodes); a joining node splits a random selection of
  existing partitions. Keeps partition sizes stable as the cluster scales.

## Automatic vs. manual

Fully automatic rebalancing interacts dangerously with
[failure detection](timeouts-and-failure-detection.md): an overloaded, slow
node gets declared dead, automatic rebalancing migrates its partitions, the
copying loads the network and remaining nodes further, more nodes slow down —
a cascading failure. Rebalancing is expensive and rare enough that
**human-in-the-loop** is a sound default: the system proposes a movement
plan, an operator approves it.
