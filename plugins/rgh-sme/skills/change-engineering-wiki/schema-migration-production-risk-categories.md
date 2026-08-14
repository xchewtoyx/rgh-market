---
type: concept
title: Schema Migration Production Risk Categories
description: >
  Database migrations carry four distinct production risks — locking,
  resource saturation, data integrity, and replication stalls — each
  needing its own mitigation, not a single generic "be careful" review.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
---

# Schema Migration Production Risk Categories

A schema migration's production impact analysis should check four
distinct risk categories, because each has a different failure mode and a
different mitigation:

1. **Locking of objects** — how long the migration holds a lock on a table
   or index. Acceptable duration is subjective and tied to the affected
   service's SLOs; measure historically and plan mitigation (reduce the
   locked duration, or redirect traffic away from the locked object) if the
   duration is unacceptable. Worked mitigation for the common case of
   "adding a column with a default locks the whole table": add the column
   empty → regression test → use conditional code at access time to
   backfill/validate the value → add a watcher to detect full backfill
   completion → remove the conditional code. Where locking is genuinely
   unavoidable, standardize on one consistent process (online DDL via
   triggers/renames, or a [rolling](rolling-deployment.md) node-by-node
   migration) rather than maintaining two divergent "light" and "heavy"
   processes — the rarely-used one atrophies and becomes unsafe by the time
   it's needed.
2. **Saturation of resources** — heavy I/O from the migration can raise
   latency for all transactions on the affected system and cascade into
   failure elsewhere. Mitigate by throttling batched updates, using
   lazy/on-access updates for large-scale changes, using soft deletes
   (flag now, remove asynchronously later) instead of bulk deletes, and
   using partition-drop rather than row-by-row deletion for range-based
   removal.
3. **Data integrity issues** — a migration's transitional, relaxed or
   deferred constraints can let data land in an unexpected state during
   the transition window. This is exactly the risk
   [expand-and-contract schema migration](expand-and-contract-schema-migration.md)
   is designed to contain by keeping each phase individually consistent.
4. **Replication stalls** — increased write activity or lock contention
   from a migration can increase replication lag, jeopardizing replicas
   and failover safety for the duration of the migration.

Persistent, migration-driven I/O latency is a capacity red flag worth
treating as an early warning sign in its own right, independent of whether
the migration otherwise "succeeds."
