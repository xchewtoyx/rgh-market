---
type: concept
title: Change Data Capture (CDC)
description: >
  Extracting a database's write stream from its replication log and feeding
  it to derived systems, making search indexes, caches, and warehouses
  followers of the system of record.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
---

# Change Data Capture (CDC)

CDC observes every write committed to a database and streams it, in commit
order, to other systems. Rather than trusting applications to
[write everywhere](dual-writes-problem.md), CDC taps the database's own
[replication log](replication-log-implementations.md) — parsing the MySQL
binlog, PostgreSQL WAL, or MongoDB oplog (Debezium, Maxwell) — so the
capture is low-level, complete, and ordered.

The architecture this enables: **one system of record, many derived
followers.** Search indexes, caches, warehouses, and materialized views each
consume the change stream (usually via a
[log-based broker](log-based-messaging.md)) and update themselves —
essentially [followers](single-leader-replication.md) implemented outside
the database. Derived systems are *asynchronous* consumers: they lag, with
all the [replication lag](replication-lag.md) caveats, and they cannot feed
guarantees back (a [linearizable](linearizability.md) uniqueness check can't
be built downstream of an async log).

**Log compaction** (Kafka) solves the "need the full history but the log is
infinite" problem: keep only the latest value per key, dropping overwritten
records and tombstoned deletions. A compacted changelog topic is then a
complete snapshot of the database *plus* its ongoing changes — a new
consumer bootstraps by reading from offset 0 instead of coordinating a
snapshot with the log position.

CDC also underlies rebuilding: because the derived view is a pure function
of the log, you can drop and repopulate an index, or build a new view
alongside the old, by replaying — the operational escape hatch that
[dual-write](dual-writes-problem.md) architectures lack. For replay to be
safe, derivation processors must be **deterministic and
[idempotent](idempotency.md)** — the properties that let this style
[replace distributed transactions](unbundling-the-database.md) as the
integration mechanism between heterogeneous systems.
