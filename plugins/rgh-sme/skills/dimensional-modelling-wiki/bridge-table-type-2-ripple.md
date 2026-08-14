---
type: concept
title: Bridge Table Type 2 Ripple Effect
description: >
  Why a type 2 change to one node forces new type 2 rows for every other
  member of its hierarchy, and how to bound that cascade in a ragged
  hierarchy bridge table.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 10"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Keying a [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md)'s parent and child columns on the dimension's [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) surrogate key means a changed member can't simply be added as a new peer row alongside its unchanged predecessor in the same tree: if the new version is added as a sibling of the old version, both still link to the same subordinate rows, so any query that constrains on the member's natural key — which necessarily now matches both the old and new surrogate-keyed versions — double-counts every subordinate's facts once per version.

The only way to keep old facts cleanly associated with the pre-change tree and new facts with the post-change tree, while still allowing ordinary natural-key-based filtering, is to give **every other member that participates in the same hierarchy** a new type 2 row too — not just the changed member and its direct ancestors/descendants, but siblings and any other member transitively reachable through the bridge — plus a full parallel set of bridge rows connecting the new versions into a second tree alongside the old one. The same full-hierarchy ripple applies when the change is to a relationship itself (a member moves to a different parent) rather than to a dimension attribute.

Stamping bridge rows with effective/expiration dates instead of rippling does not avoid this problem — it only pushes the complexity into every query, which must then correlate the bridge's date range against the fact's own transaction date, and is easy to get wrong even for trained developers.

## The ripple effect

Any type 2 change to a node deep in the tree — especially a senior node with a large subtree, such as top management in an org chart — forces new path rows for every affected ancestor-descendant pair, cascading in the same way a [self-referencing outrigger](outrigger-dimension.md) does. This full-hierarchy cascade is sometimes called the **ripple effect**: a routine micro-level change to one node (see [micro-level vs. macro-level change](slowly-changing-dimension-type-2.md)) turns into a macro-level event for the whole subtree beneath it, purely as a side effect of how the bridge is keyed — a hierarchy that is small and stable can absorb this without difficulty, but a hierarchy that is large and volatile (a company-wide reporting-line hierarchy, where every employee ultimately traces back to the same CEO) cannot.

## Mitigations

Two mitigations, usable independently or together:

- **Key the bridge on the dimension's durable key rather than its type 2 surrogate key**, adding effective and expiration dates directly on the bridge to capture the historical timespan of each relationship. New bridge rows are then created only when the *relationships themselves* change (a node moves to a new parent), not on every unrelated type 2 attribute change elsewhere in the tree — substantially reducing bridge growth, at the cost of a bridge table that is easier to keep small but harder to navigate, particularly when associating historical org structure with the timing of individual fact-table events. Joining an effective-dated bridge to a fact table also gets more expensive at query time — a plain equi-join (`bridge.employee_key = fact.employee_key`) becomes a theta join that must also check the fact's own date against the bridge row's effective/expiration range. If a fact table joins to the bridge constantly, adding a single dedicated surrogate key to the bridge (built once by ETL to represent "this relationship as of this timespan") restores a plain equi-join at query time — at the cost of a new ETL ordering dependency, since the bridge must now be fully built before any fact table that references its dedicated key can be loaded.
- **Split one large, deeply interconnected hierarchy into several smaller, more independent ones** — for example, removing the topmost executive level(s) from a company-wide reporting hierarchy so that each remaining branch becomes its own smaller, less volatile hierarchy. A smaller hierarchy is inherently less exposed to the ripple effect, which can make keying directly on the dimension's ordinary type 2 surrogate key viable again, avoiding both the durable-key bridge and the theta-join cost altogether.
