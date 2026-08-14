---
type: concept
title: Change Stream Consumption Pattern
description: >
  A queryable change-capture object that accumulates deltas since the last
  read and drains only when a downstream load actually consumes it, plus
  gating a job to run only when there's real work waiting.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 4"
---

A change stream is a logical object layered on top of a table (or view) that
captures row-level changes — inserts, deletes, and before/after images of
updates — since some reference offset, without physically duplicating the
source table's data. It works by combining a logical snapshot with metadata
columns tracking subsequent changes, similar in spirit to
[log-based change data capture](change-data-capture.md) but exposed as
something directly queryable rather than an external log format.

The consumption model is the important mechanic: **querying** the stream
(a plain `SELECT`) doesn't advance it, but successfully **loading** its
contents into a downstream target does — the stream's offset moves forward
only once a consuming job actually commits, and a failed consumption attempt
leaves the stream untouched so the same changes are available to retry. This
is exactly the guarantee [idempotent and replayable jobs](idempotent-and-replayable-jobs.md)
need: a downstream load can fail partway through without losing or
double-counting the delta it was working on, because the stream doesn't
drain until the load actually succeeds.

Pairing a change stream with [orchestration](orchestration-vs-scheduling.md)
enables a cheap conditional-execution pattern: schedule the consuming job
frequently, but gate its actual execution on a check for whether the stream
currently has any pending changes at all. This lets a pipeline poll often
without paying compute cost on every poll when there's nothing new to
process — only actually running (and consuming resources) on the polls where
real work is waiting.
