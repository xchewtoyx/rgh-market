---
type: concept
title: Type 1 Change Corrupts Aggregate Attribution Retroactively
description: >
  Why a Type 1 overwrite on a dimension attribute used by a rollup aggregate
  silently misattributes historical summary rows once the load reaches the
  aggregate step, and why Type 2 attributes don't share the problem.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Adamson), ch. 15"
---

An [aggregate table](aggregate-table-load-consistency.md) built by rolling up
a dimension attribute that's maintained as a
[Type 1 overwrite](scd-overwrite-load-mechanics.md) has a load-ordering
correctness trap that doesn't show up in either piece considered alone.
Walk the normal load sequence — dimensions, then rollups, then base facts,
then aggregate facts — for a rollup dimension built on a Type 1 attribute
(product manager, say, reassigned from one manager to another):

1. The base dimension loads first, and the Type 1 overwrite does its job
   correctly: the product's manager field is updated in place. The *old*
   manager's name is now gone from the base table — that's what a Type 1
   overwrite means.
2. The rollup dimension loads next; if a row for the new manager already
   exists, nothing new is created.
3. The base fact table loads, and new transactions correctly attribute to
   the new manager.
4. The aggregate fact table loads last. New transactions land correctly
   under the new manager — but the aggregate rows that already existed
   before this load, summarizing transactions that happened *while the old
   manager was still assigned*, are now wrong. Fixing them requires
   re-attributing that historical volume from the old manager's summary row
   to the new one, and by step 4 the base dimension no longer records what
   the old value even was — the overwrite in step 1 already destroyed the
   information needed to correct step 4.

**Type 2 attributes never have this problem**, which is why it's specifically
a Type 1-in-a-rollup issue and not a general aggregate-maintenance concern: a
Type 2 change inserts a new dimension row rather than rewriting an old one,
so it never restates the context under which previously-loaded facts were
already correctly summarized — there's nothing to retroactively fix.

**Resolutions, in practice:**

- **Drop and rebuild the aggregate fact table** whenever a Type 1 attribute
  used in its rollup dimension changes. Often less total work than
  incremental correction, and it's what most automated cube/aggregate tools
  default to.
- **Exclude Type 1 attributes from aggregate rollup dimensions entirely** —
  avoids the trap at design time by never letting an aggregate depend on
  something that can silently rewrite its own history.
- **Scope the correction narrowly when the Type 1 attribute is fully
  dependent on a Type 2 attribute already in the same rollup** — if the
  rollup dimension also carries the Type 2 attribute the Type 1 field
  depends on, the update can be confined to the one affected row instead of
  requiring a full aggregate-fact correction, at the cost of extra load
  logic to detect and scope that dependency correctly.

The load-order lesson generalizes beyond this specific case: whenever an
aggregate load runs *after* the base dimension it rolls up has already been
overwritten, any information needed to correct the aggregate for that
overwrite has to be captured **before** the base dimension load destroys it —
either by diffing old-vs-new values as part of the dimension load itself, or
by defaulting to a full aggregate rebuild instead of trying to capture that
diff at all.
