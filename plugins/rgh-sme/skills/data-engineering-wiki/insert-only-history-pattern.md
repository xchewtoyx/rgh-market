---
type: concept
title: Insert-Only History Pattern
description: >
  Retaining history by always inserting a new timestamped row instead of
  updating in place, and the two costs (table growth, expensive current-state
  lookups) that come with it.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
---

Instead of updating a row in place when a value changes, the insert-only
pattern inserts a new timestamped row under the same entity key and leaves
the old row untouched — a customer address change, for example, becomes a
new row rather than an overwrite, and reading "current" state means finding
the row with the latest timestamp for that customer. This effectively embeds
a database log inside the table itself, which is useful whenever the
application (not just downstream analytics) needs direct access to history —
a banking app showing address history, for instance.

The same pattern shows up as a distinct **analytics insert-only ETL
pattern**: a pipeline layers this behavior on top of a regular CRUD source
table by inserting a new target-table record on every source update, even
though the source itself doesn't retain history — giving the target the
history the source lacks. This is one concrete way to implement the load
mechanics behind [slowly changing dimensions](change-data-capture.md), at the
pipeline layer rather than in the source system.

Two costs to weigh before adopting it:

1. **Table growth**: frequent changes make the table grow without bound,
   which needs a mitigation — purging on a sunset date, or capping the
   number of retained versions per key.
2. **Expensive current-state lookups**: finding "the current row" requires a
   `MAX(timestamp)`-style query per key, which gets costly once many versions
   accumulate per entity — an index or a separate materialized "current"
   view is often needed to keep that lookup cheap.

**The validity-interval variant**: rather than a single timestamp, many
implementations give each row an explicit `from_date`/`to_date` (or
`valid_from`/`valid_to`) pair — the currently-active row conventionally
carries a far-future sentinel `to_date` (`9999-12-31` is a common choice) to
flag it as open-ended. This directly answers two things a single insert
timestamp doesn't: which row was correct as of any arbitrary past date (a
`BETWEEN from_date AND to_date` filter against the date in question, not
just "the latest"), and it gives the load a concrete data-quality invariant
to check after every run — for a given entity key, `from_date` values must
be unique and no two intervals may overlap. This is the mechanic that
actually implements Type 2 slowly-changing-dimension tracking at load time;
see [hash-based change detection](hash-based-change-detection.md) for how a
load decides a new interval-bounded row is even needed, and
[SCD Type 2 load via change stream](scd-type2-load-via-change-stream.md) for
a technique that produces this pattern's output cheaply. See
[SCD Type 1/3 overwrite load mechanics](scd-overwrite-load-mechanics.md) for
what happens instead when a change is overwritten rather than versioned, and
[hybrid SCD current-value backfill](hybrid-scd-current-value-backfill.md) for
layering a "current attribute" view on top of this pattern without losing
its point-in-event accuracy. A separate variant, the [mini-dimension
pattern](mini-dimension-load-mechanics.md), sidesteps this pattern's row
growth for a large, frequently-changing dimension by versioning only the
volatile attributes in their own small table instead of the whole entity.

**Building a gapless interval sequence needs a two-step insert, not one.**
For a validity-interval table meant to have no gaps between consecutive
rows for the same key (a "timespan" fact table used for exact
point-in-time or duration queries), setting a new row's `to_date` one tick
before the *next* row's `from_date` is tempting because it fits `BETWEEN`
syntax neatly, but it leaves a real gap between the two ticks where a
transaction can fall through undetected. Set `to_date` exactly equal to the
next row's `from_date` instead, and use `>= from_date AND < to_date`
comparisons rather than `BETWEEN`. That equality can't be established in a
single insert, since the new row's `from_date` isn't known until the new
row is actually being written: load it in two steps — (1) insert the new
row with a far-future sentinel `to_date`, then (2) immediately after, update
the *prior* row for that key, setting its `to_date` to the new row's
`from_date`. This extra back-room update is a deliberate trade-off: more
load-time work in exchange for point-in-time and duration queries that stay
simple range filters at read time instead of needing gap-aware logic.

**A factless fact table whose row count tracks its dimension 1:1 is a
design smell, not a load problem to work around.** If every profile-change
event produces both a new Type 2 dimension row and a new row in a
transaction-grained factless fact table recording that same event, the two
tables end up the same size and are almost always queried joined together
— the fact table is adding no independent grain of its own. The fix is to
drop the redundant fact table and load the event's context (its "reason"
or "change type") as an attribute directly on the Type 2 dimension row
instead, reserving separate fact tables for events that carry an actual
numeric measure or that involve genuinely different dimensionality (a
review event's reviewer and outcome, say) from the entity's own profile.

**Never resurrect or reopen an already-expired row's validity window.** If
an entity's attributes revert to a set of values it held previously (an
employee moves back to a department they'd left, say), the correct load
response is to insert a brand-new row with a new effective/expiration span
— never to reuse or extend the older row that originally held those values.
Reopening a prior row's window risks two rows claiming to be valid for
overlapping periods, which breaks the same from-date uniqueness and
no-overlap invariant an ordinary Type 2 load already has to maintain.

**Date-only granularity silently breaks once a key can change more than once
per day.** If the validity interval is tracked with dates alone but the
source allows multiple updates to the same entity within a single day, a
date-range point-in-time filter for "today" can return more than one open
row for that key — correct per the interval logic, but wrong for any
aggregate query expecting exactly one row per key per day. Widening the
interval columns to `effective_time`/`expiration_time` (at whatever
sub-day precision the source actually needs) fixes the range filter, but
then reintroduces the same one-row-per-day expectation at the query layer;
the load-time fix is a same-day rollup flag — set on whichever row was the
last version to be effective that day — so a query that wants clean
end-of-day status can filter to it directly instead of reasoning about
intraday ordering itself.

**Derive the effective timestamp from the pipeline's own as-of/system date,
never from a source-supplied metadata field** like a `last_modified_date`
column. Back-end scripts and bulk fixes on the source frequently write to a
table without updating its own modification-timestamp metadata, so trusting
that field to mark when a version became effective silently misdates rows —
the pipeline's own clock at load time is the only timestamp guaranteed to
reflect when the change was actually captured.
