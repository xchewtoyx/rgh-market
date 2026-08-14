---
type: concept
title: Table Load Patterns (Truncate-Reload, Insert-Only, Delete, Upsert/Merge)
description: >
  The concrete write patterns available for getting a transformation's
  output into a target table, and what each one costs in a file-based
  columnar system.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

A pipeline writing to a target table has a small set of concrete load
patterns to choose among — this is the load-mechanics layer that actually
implements whatever dimensional design (grain, SCD type) the target model
calls for:

- **Truncate and reload**: not really an update at all — wipe the old
  table, rerun the transformation, reload, producing an effectively new
  table version each time. Simple, but means the whole table is recomputed
  regardless of how little actually changed. A dedicated `TRUNCATE` (rather
  than a row-by-row `DELETE`) is the fastest way to clear a staging table at
  the start of each cycle, since it skips per-row logging entirely.
- **Insert only**: insert new records without touching or deleting old
  ones; a query or view finds the newest record per key to present current
  state. Note that columnar databases generally don't *enforce* primary-key
  uniqueness the way an RDBMS does — it's a convention the pipeline has to
  maintain itself. This is the general-purpose mechanism behind
  [the insert-only history pattern](insert-only-history-pattern.md) and
  behind implementing Type 2 slowly-changing-dimension processing at load
  time. The downside is that finding "the latest record per key" at query
  time gets expensive as history accumulates — mitigate with a materialized
  view or a separately maintained truncate-and-reload "current state"
  table.
- **Delete**: more expensive than inserts in columnar/file-based systems.
  A **hard delete** permanently removes a record. A **soft delete** flags a
  record as deleted without removing it, so it's filtered out of query
  results but still recoverable and auditable. **Insert deletion** is a
  soft-delete variant that inserts a new "deleted"-flagged record rather
  than modifying the prior one, keeping the insert-only pattern intact at
  the cost of a query that now has to both deduplicate to the latest version
  per key *and* exclude any key whose latest version is flagged deleted. For
  a dimension table specifically, don't delete a row just because its
  member disappeared from the source system — historical fact rows loaded
  earlier likely still reference it, and hard-deleting the dimension row
  turns those into orphaned foreign keys.
- **Two-phase correction**: when fixing already-loaded fact rows (a
  corrected quantity or amount), insert the corrected rows first, and only
  delete the original rows in a separate, second step — rather than
  updating or deleting-then-inserting in one pass. This depends on the fact
  table having a sequentially assigned surrogate key so corrected and
  original rows can coexist briefly without ambiguity, and it means a
  failure between the two steps leaves both versions present (safe to
  reconcile) rather than leaving a gap where neither version exists.
- **Upsert / merge**: match source records against the target by key or
  another logical condition — matched records get replaced, unmatched get
  inserted (merge additionally supports deletion). This is the pattern that
  causes the most trouble migrating from row-based warehouses to columnar
  cloud systems, because of the underlying
  [copy-on-write cost](copy-on-write-load-cost.md) it triggers in file-based
  storage.

Common antipattern: an engineer coming from a row-oriented system tries
single-row inserts against a columnar OLAP target — this creates excessive
small files that need later reclustering. Load in periodic micro-batches
instead, except on hybrid systems (BigQuery, Druid) that are specifically
built with a streaming-insert buffer to tolerate frequent single-row writes.

**Scope every merge to the latest unprocessed batch, never the whole
source.** A merge already pays [copy-on-write cost](copy-on-write-load-cost.md)
proportional to what it touches; filtering the source side of a merge down
to only the rows from the most recent load (e.g., `WHERE load_id = (SELECT
MAX(load_id) FROM staging)`) avoids re-comparing and re-touching records the
pipeline already processed in a prior run. This filter is easy to lose track
of as a pipeline evolves, so it's worth encapsulating in a view or a
dedicated staging object rather than repeating the filter condition inline
in every merge statement that needs it.
