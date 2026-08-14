---
type: concept
title: Replication Lag
description: >
  The delay between a write on the leader and its appearance on asynchronous
  followers, which turns "scale reads with replicas" into a source of
  consistency anomalies.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
---

# Replication Lag

In a read-scaling architecture — one leader, many [asynchronous
followers](synchronous-vs-asynchronous-replication.md) — a follower serves
whatever state it has applied so far, which may be seconds or (under load or
network trouble) minutes behind the leader. Reads from leader and follower run
concurrently can return different answers. This is temporary — stop writing and
replicas converge — hence [eventual consistency](eventual-consistency.md).

Lag is not just a performance number; it produces specific, user-visible
anomalies, each with its own containment guarantee:

- Users not seeing their own submitted data —
  [read-your-writes consistency](read-your-writes-consistency.md).
- Data appearing to move backward in time between successive reads —
  [monotonic reads](monotonic-reads.md).
- Effects observed before their causes (an answer before the question) —
  [consistent prefix reads](consistent-prefix-reads.md).

The design lesson: decide up front how the application behaves when lag grows
to minutes. If the answer is "that's a problem", engineer the specific
guarantee needed rather than pretending the replication is synchronous —
stronger guarantees than eventual consistency exist without paying for full
[linearizability](linearizability.md).

## Why followers fall behind, and the mitigation ladder

Structural causes: followers often apply the log serially while the leader
wrote with full concurrency; follower caches are cold for the write workload;
and read traffic contends with the apply process. When lag persists, fixes
escalate: short term, add replica capacity (or tactically preload the hot
dataset, relax follower durability settings); medium term, functionally
partition — split distinct workloads onto their own clusters; long term,
[shard the dataset](partitioning.md) or change datastores. None scales
linearly forever, so lag deserves the same
[monitoring](monitoring-replication-health.md) as any capacity metric.
