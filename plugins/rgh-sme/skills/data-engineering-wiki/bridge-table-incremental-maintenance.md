---
type: concept
title: Hierarchy Bridge Table Incremental Maintenance
description: >
  Loading a ragged-hierarchy bridge table so a structural change touches
  only the affected paths, instead of forcing a full rebuild or a
  relabeling cascade across the whole tree.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 7"
---

A **hierarchy bridge table** represents a ragged, variable-depth rollup
tree (an org chart, a chart-of-accounts structure) as one row per
parent-to-descendant path — every node paired with every node beneath it,
not just its immediate children — rather than as a self-referencing parent
key on the dimension row itself. The self-referencing-pointer alternative is
a load-mechanics dead end at any real scale: because a high-level node's key
change ripples down its entire subtree, maintaining that structure as a
[Type 2](insert-only-history-pattern.md) dimension is impractical, and
switching to a different rollup grouping means destructively rewriting many
pointers at once.

The bridge table's payoff is a **limited-blast-radius load**: a tree
restructuring only requires touching the paths that actually changed, never
the whole table.

- **Static bridge table** (current structure only): when a subtree moves to
  a new parent, delete the higher-level paths that point into the moved
  nodes from their *old* ancestor chain, then insert new paths connecting
  the same moved nodes to their *new* ancestor chain. Paths entirely above
  or entirely below the moved subtree are untouched.
- **Time-varying bridge table**: instead of deleting the old paths, add
  begin/end-effective date columns to the bridge table and set the
  superseded paths' end-effective date to the moment of change, then insert
  the new structure's paths with a matching begin-effective date. Every
  query against a time-varying bridge table must constrain to a single
  point in time — omitting that constraint pulls in multiple
  mutually-exclusive-in-time paths at once and produces an incoherent
  result, the same hazard an unconstrained [Type
  2](insert-only-history-pattern.md) join produces on an ordinary
  dimension.

Either way, the row count that has to be inserted or end-dated for a given
structural change is proportional to the size of the moved subtree and its
new ancestor chain, not to the size of the whole tree — which is what makes
this load tractable for org structures that get reorganized on an ongoing
basis rather than being rebuilt from scratch on every change.

**Shared ownership** (a node whose contribution rolls up partially into more
than one parent) is loaded the same incremental way: add extra path rows
connecting the shared node up through each additional ownership chain, and
set an ownership-percentage column only on the path rows that terminate at
that node — every other existing path row is left alone.

This limited-blast-radius maintenance assumes the members' own surrogate
keys stay stable across the restructuring. If a member's own dimension row
instead undergoes a Type 2 change, the bridge maintenance is not local at
all — see [the hierarchy bridge Type 2 ripple
effect](hierarchy-bridge-type2-ripple-effect.md) for why that case forces
versioning the entire hierarchy tree, not just the changed paths.
