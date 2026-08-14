---
type: concept
title: Serializability
description: >
  The strongest isolation level — outcomes equal to some serial execution —
  and its three implementations: actual serial execution, two-phase locking,
  and serializable snapshot isolation.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 11"
---

# Serializability

The strongest [isolation](acid-transactions.md) guarantee: concurrent
transactions produce the same net outcome as *some* serial, one-at-a-time
execution. All race anomalies — [lost updates](lost-updates.md),
[write skew, phantoms](write-skew-and-phantoms.md) — are excluded by
definition, which is why it's the only comprehensive answer when invariants
span multiple objects. (Distinct from
[linearizability](linearizability.md): serializability permits orders that
differ from real time; the combination is strict serializability.)

Three known implementation families:

## 1. Actual serial execution

Run every transaction sequentially on a single thread (VoltDB, Redis,
Datomic). Feasible because RAM got cheap (whole dataset in memory — no disk
stalls) and OLTP transactions are short. Requires transactions be submitted
as **stored procedures** executing entirely server-side — an interactive
client round-trip per statement would serialize the waiting too. Scales
writes by [partitioning](partitioning.md) data so each core serially owns a
partition — but **cross-partition transactions need coordination and are
drastically slower** (~1,000 tx/sec), so the data model must keep
transactions single-partition.

## 2. Two-phase locking (2PL)

The classic pessimistic approach (MySQL InnoDB serializable, SQL Server).
Readers take shared locks, writers exclusive locks, all held to
commit/abort: **readers block writers and writers block readers** (exactly
what [snapshot isolation](snapshot-isolation.md) avoids). Phantoms are
prevented with **predicate locks** (lock a `WHERE` condition, including
future rows) approximated in practice by **index-range (next-key) locks**.
Cost: poor throughput and severe latency tails under contention — queueing
behind long transactions, frequent deadlocks with retries.

## 3. Serializable snapshot isolation (SSI)

Optimistic: transactions run without blocking on
[MVCC snapshots](snapshot-isolation.md); at commit, the database checks
whether the transaction's premises were invalidated by concurrent commits —
(a) an uncommitted write it ignored in its snapshot later committed, or
(b) a concurrent transaction wrote into an index range it read (index
entries as non-blocking tripwires). Violators abort and
[retry](transaction-aborts-and-retries.md). Readers and writers never block
each other, latency is predictable, and it scales across cores
(PostgreSQL serializable, FoundationDB). Cost: wasted work under high
contention — aborts rise with conflict rate, so it wants short transactions
and low contention.

## Verify the label, not the marketing

Vendor isolation-level names routinely overstate: Oracle's "serializable" is
closer to [snapshot isolation](snapshot-isolation.md); MySQL InnoDB's
lock-based serializable famously failed to detect some
[lost updates](lost-updates.md). The permitted-anomaly definitions are the
ground truth — test actual behavior (Jepsen and Hermitage are the standard
tools) rather than trusting the level's name.
