---
type: concept
title: Partitioning (Sharding)
description: >
  Splitting a dataset so each record belongs to exactly one partition,
  spreading storage and load across a shared-nothing cluster.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 6"
---

# Partitioning (Sharding)

Breaking a large dataset into subsets — partitions — such that each record
(row, document, key) belongs to **exactly one** partition. Every system has
its own word for the same thing: shard (MongoDB, Elasticsearch), region
(HBase), tablet (Bigtable), vnode (Cassandra, Riak), vBucket (Couchbase).

The goal is **scalability**: each node handles the storage and query load for
its share of partitions, so a shared-nothing cluster scales by adding nodes.
Effectiveness depends entirely on spreading load *evenly* — an unfair split
concentrates load on [hot spots](hot-spots-and-skew.md) and reduces an
n-node cluster to the throughput of one.

Design decisions that follow, each with its own note:

- How to assign keys to partitions:
  [key-range](key-range-partitioning.md) vs.
  [hash](hash-partitioning.md) partitioning.
- What happens to [secondary indexes](partitioned-secondary-indexes.md),
  which don't map neatly onto a primary-key partitioning.
- How to [rebalance](rebalancing-partitions.md) partitions when nodes join,
  leave, or fail.
- How requests [find the right node](request-routing.md) as placement
  changes.

Partitioning is combined with replication: each partition is replicated
across several nodes, and with
[single-leader replication](single-leader-replication.md) each node is leader
for some partitions and follower for others. It also weakens cross-partition
guarantees — partitions replicate independently, so there is no global write
order (see [consistent prefix reads](consistent-prefix-reads.md)), and
transactions spanning partitions need
[atomic commit machinery](two-phase-commit.md). Analytical (MPP) databases
additionally use partitions to parallelize whole queries across nodes.
