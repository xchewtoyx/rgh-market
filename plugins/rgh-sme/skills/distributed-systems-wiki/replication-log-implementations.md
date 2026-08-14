---
type: concept
title: Replication Log Implementations
description: >
  The four ways a leader can represent changes for followers — statement-based,
  WAL shipping, logical (row-based), and trigger-based — and what each breaks.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 10"
---

# Replication Log Implementations

[Single-leader replication](single-leader-replication.md) needs a log format
for shipping changes to followers. The choice determines what the replication
stream can safely do:

1. **Statement-based.** The leader logs the SQL statements it executed and
   followers re-run them. Broken by nondeterminism: `NOW()` and `RAND()`
   evaluate differently per node, auto-increment and concurrent-transaction
   ordering must match exactly, and triggers/stored procedures may have
   different side effects. Largely abandoned (MySQL switched away by default).
2. **Write-ahead log (WAL) shipping.** Stream the storage engine's own
   [write-ahead log](write-ahead-log.md) of disk-block byte changes
   (PostgreSQL, Oracle). Exact but
   tightly coupled to the physical storage format — leader and follower must
   run compatible versions, which blocks zero-downtime rolling upgrades where
   a follower runs newer software than the leader.
3. **Logical (row-based) log.** A sequence of row-level change events decoupled
   from storage internals: inserted row's column values, deleted row's primary
   key, updated row's new values (MySQL binlog in row mode). Supports [rolling
   upgrades across versions](rolling-upgrade-compatibility.md), and is easily
   parsed by external systems — the basis of [change data
   capture](change-data-capture.md).
4. **Trigger-based.** Application-level triggers record writes into shadow
   tables that an external process harvests (Oracle GoldenGate, Databus,
   Bucardo). Most flexible — can replicate a subset, transform data, or feed a
   different system — but highest overhead and most bug-prone.
5. **Block-level (outside the database).** Replicate at the disk-block layer
   (e.g. DRBD), invisible to the database engine. Synchronous with little
   overhead, but the standby has *no running database instance* — failover
   requires a full instance start, including crash recovery if the primary
   died dirty, lengthening recovery time.

The trade-off axes across all of these: bandwidth (statement-based is
compact, WAL shipping heavy), determinism (statement-based risks silent
follower drift), portability across versions and engines (logical wins —
which matters for rolling upgrades and for feeding external consumers), and
auditability (logical logs are inspectable; WAL bytes are not).
