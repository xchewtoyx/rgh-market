---
type: concept
title: SCD Type 2 Load via Change Stream Before-Images
description: >
  Getting Type-2-style full history at close to Type-1 load cost, by
  capturing a change stream's pre-update row images instead of computing
  history with window functions or extra lookups.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 13"
---

A [Type 2 slowly-changing-dimension load](insert-only-history-pattern.md)
that preserves full history is inherently heavier than a Type 1
overwrite-in-place load, since the table keeps growing rather than staying
roughly the same size. There's a load-mechanics technique that closes most
of that gap: attach a [change stream](change-stream-consumption-pattern.md)
to the dimension table, and use it in two steps instead of one:

1. **Merge current values in place**, exactly the way a Type 1 load would —
   matched rows get updated to their latest values, unmatched rows get
   inserted. This step's cost profile is identical to a plain Type 1 merge,
   using [hash-based change detection](hash-based-change-detection.md) to
   skip rows that haven't actually changed.
2. **Insert the stream's before-images as new history rows.** Because most
   warehouse storage is internally insert-only underneath an `UPDATE`
   statement — a row is never literally overwritten in place at the storage
   layer — the change stream's delete-tagged entries are exactly the
   pre-change values, retrievable directly with no window functions and no
   extra lookup against a prior snapshot:
   ```sql
   INSERT INTO dim_customer
   SELECT <stream columns> FROM change_stream
   WHERE metadata$action = 'DELETE';
   ```
   The row count this step inserts should always match the row count the
   merge step updated, which is a cheap built-in consistency check on the
   load itself.

The payoff is concrete: at meaningful scale, this two-step
merge-plus-stream-drain approach has measured roughly 40% faster than a
generic Type 2 implementation that reconstructs history through temp tables
or window-function comparisons, because it never has to recompute what
changed — the stream already tells it. The two steps chain naturally into
sequential [orchestration](orchestration-vs-scheduling.md) tasks for a single
daily (or more frequent) load routine, and the stream's
[consumption semantics](change-stream-consumption-pattern.md) mean a failed
step 2 doesn't lose the pending history — it just leaves the stream
undrained for the next run.
