---
type: concept
title: Eventual Consistency
description: >
  The weak guarantee that replicas converge to the same value once writes
  stop — with no promise about when, or what reads return in the meantime.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

# Eventual Consistency

Most replicated systems promise at minimum *convergence*: if you stop writing
and wait an unspecified time, all replicas eventually return the same value.
That is the whole guarantee. It says nothing about **when** convergence
happens or what a read returns before it does — reading immediately after a
write may return nothing at all.

**BASE** (Basically Available, Soft-state, Eventual consistency) is the
common label for this posture, coined as [ACID](acid-transactions.md)'s
opposite: reads/writes are best-effort rather than guaranteed-consistent
("basically available"), and a transaction's committed-or-not status can be
fuzzy for a window ("soft-state") before convergence resolves it. It names
the same trade this note describes — eventual consistency is the price
commonly paid for horizontal scalability, since it lets a node answer
without cross-node verification on every read.

This makes eventual consistency a hard programming model: the anomalies of
[replication lag](replication-lag.md) are subtle, hard to test for (bugs
surface only under network trouble or high concurrency), and easy to write
past without noticing. Database "consistency" here differs from a
single-threaded variable — the edge cases matter.

The spectrum above it, in increasing strength and cost:

- Session guarantees: [read-your-writes](read-your-writes-consistency.md),
  [monotonic reads](monotonic-reads.md),
  [consistent prefix](consistent-prefix-reads.md) — per-user containment of
  lag anomalies without global coordination.
- [Causal ordering](causal-ordering.md) — everyone observes cause before
  effect; the strongest model that stays available under partition.
- [Linearizability](linearizability.md) — the system behaves as a single copy
  with a recency guarantee; simple to use, expensive to provide.

Convergence itself is only automatic in single-leader designs; multi-leader
and leaderless systems must engineer it via
[conflict resolution](write-conflict-resolution.md), and it must be
**proven, not assumed** — divergence windows during partitions can last
hours or days, and testing tools like Jepsen exist precisely because vendors'
convergence and isolation claims frequently fail under induced partitions.
Note "eventually" is a [liveness property](system-models.md) — allowed to
depend on the network healing.
