---
type: concept
title: Hierarchy Bridge Type 2 Ripple Effect
description: >
  Why a Type 2 change to one member of a bridged hierarchy forces every
  other member of that same tree to be versioned too, not just the changed
  node's own ancestors and descendants.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Adamson), ch. 10"
---

A [hierarchy bridge table](bridge-table-incremental-maintenance.md) that
resolves a structural change (a subtree moving to a new parent) only needs
to touch the paths for that moved subtree — a limited-blast-radius load.
A different kind of change hits the same bridge much harder: when a
**dimension member itself** undergoes a [Type 2 change](insert-only-history-pattern.md)
(a new surrogate key for an attribute change, unrelated to its position in
the hierarchy), naive handling breaks the bridge's natural-key-based query
pattern in a way that isn't obvious until it's already produced wrong
numbers.

**Why patching in just the one new row fails.** Say member E gets a new
surrogate key E-1 after a Type 2 change. If E-1 is simply added as a peer of
E in the *existing* tree, both E and E-1 still link, through the bridge, to
E's same subordinates (F, G, H). Any query that filters on E's *natural*
key — the only practical way to filter a bridge query, since surrogate keys
are meaningless — necessarily matches both E and E-1 rows. F, G, and H's
facts then get counted through both paths: once via E, once via E-1. The
double-counting isn't a corner case; it's the direct, structural consequence
of a bridge that assumes one surrogate key per natural key per tree
position.

**The required fix is a full-tree ripple, not a local patch:** every other
member that participates in the *same hierarchy* as the changed member —
not just its direct ancestors and descendants, but every sibling and cousin
transitively connected to it through the bridge — gets a new Type 2 row too,
even though none of their own source data changed. New bridge rows then
connect all of these new-versioned rows into a second, parallel hierarchy
tree, so the bridge ends up holding two complete trees for the same set of
members: the pre-change tree (old surrogate keys throughout) and the
post-change tree (new surrogate keys throughout). A query filtering on
either tree's natural key now resolves cleanly to exactly one tree, with no
row shared between them to double-count through.

**Why the cheaper-looking alternatives don't work:**

- **Time-stamping bridge rows instead of rippling** pushes the correlation
  between bridge validity and fact transaction date into every single
  query, which is slow and error-prone at scale — worth keeping bridge
  date stamps for point-in-time *hierarchy* analysis regardless, but not as
  a substitute for the ripple.
- **Banning Type 2 changes for bridged dimensions** cripples the dimension's
  ordinary, non-hierarchy analysis (a company's headquarters location could
  no longer be tracked historically at all).
- **Requiring queries to qualify on a specific surrogate-key version**
  isn't realistic — the only way to identify a specific version without
  date stamps is to filter on the natural key plus every Type 2 attribute
  at once, which no ad hoc query author will reliably get right.

**A relationship change (not a member attribute change) triggers the
identical full-tree ripple.** If a member is reassigned to a different
parent hierarchy entirely (a subsidiary sold to a different parent
company), every member of both the old and new hierarchy needs fresh
Type 2 rows and bridge entries — otherwise a natural-key lookup from the
reassigned member still walks the old bridge rows into its former,
now-incorrect ancestor chain. This is distinct from the ordinary [bridge
path maintenance](bridge-table-incremental-maintenance.md) case, where
surrogate keys stay stable and only the bridge's path rows need
inserting or end-dating — that lighter-weight maintenance only applies when
no member's own surrogate key changes as part of the restructuring.

**Practical consequence for load design:** a load process touching any
member of a bridged hierarchy must check whether that hierarchy has a
Type 2-tracked dimension behind it, and if so, treat *any* Type 2 change
anywhere in that tree as a trigger for versioning the whole tree — not just
the member whose source data actually changed.
