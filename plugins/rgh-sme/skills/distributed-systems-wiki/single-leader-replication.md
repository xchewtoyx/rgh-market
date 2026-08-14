---
type: concept
title: Single-Leader Replication
description: >
  Replication design where one node (the leader) accepts all writes and streams
  ordered change logs to followers, which serve read-only queries.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Single-Leader Replication

The most common replication design: one node is the **leader** (also
master/primary), and all client writes go through it. The leader applies each
write locally and streams the change to its **followers** (read replicas) via a
[replication log](replication-log-implementations.md). Followers apply log
records in the same order the leader wrote them, so every replica converges on
the same state; they serve read-only queries.

Why replicate at all: keep data geographically close to users (latency), keep
the system available when nodes fail, and scale out read throughput by adding
followers.

Key design consequences:

- Because writes are serialized through one node, there are no write conflicts
  to resolve — unlike [multi-leader](multi-leader-replication.md) and
  [leaderless](leaderless-replication.md) designs.
- The replication stream can be [synchronous or
  asynchronous](synchronous-vs-asynchronous-replication.md); asynchronous is the
  common choice and introduces [replication lag](replication-lag.md) and its
  read anomalies.
- The leader is a single point of failure for writes; recovering from its loss
  requires [failover](leader-failover.md), which is where most of the design's
  operational risk concentrates.

Setting up a new follower does not require downtime: take a consistent snapshot
of the leader, copy it to the new node, then have the follower request all log
records after the snapshot's position (log sequence number / LSN in PostgreSQL,
binlog coordinates in MySQL) and catch up. The same mechanism handles follower
crash recovery — the follower knows the last transaction it processed and
requests everything since.
