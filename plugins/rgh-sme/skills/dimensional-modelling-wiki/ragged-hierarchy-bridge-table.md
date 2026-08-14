---
type: concept
title: Ragged Hierarchy Bridge Table
description: A table holding one row per path from every node to every descendant in a ragged hierarchy, enabling full-tree traversal via standard SQL joins.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 10"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

A ragged hierarchy bridge table is a specialized [bridge table](bridge-table.md) built for [ragged hierarchies](ragged-hierarchy.md) of indeterminate depth — an organization structure, a bill of materials — where a recursive self-referencing parent key on the [dimension-table](dimension-table.md) row can't be traversed with plain SQL and is fragile under change.

## Structure

Grain: one row per path in the tree from a parent to every descendant below it, including a self-referencing parent-to-itself row for every node. Columns: parent primary key, child primary key. A 13-node example tree produces 43 path rows (e.g., 13 paths originating from the topmost node, 5 from a mid-tree node, 1 self-path from a leaf node). Two flag columns support common queries: a **highest parent flag** (the path originates at the tree's topmost node) and a **lowest child flag** (the path terminates at a leaf node).

Query pattern: constrain the dimension to a single node, join dimension → bridge table → [fact-table](fact-table.md). Constraining to the topmost node and summing an [additive fact](additive-fact.md) traverses the whole tree in one query, with no recursion at query time. Adding a lowest-child-flag constraint restricts the same query to only leaf-node facts.

**Caution on non-key constraints**: constraining the dimension via a non-unique attribute (e.g., "location = California" instead of a specific node) risks overcounting children and grandchildren through a simple join, and requires a subquery instead — selecting the distinct child keys from the bridge table for all nodes matching the attribute, then constraining the fact table to that key set.

## Double-counting and safe query patterns

The bridge-to-fact join is genuinely many-to-many, since one fact can be reached by walking up through several ancestor rows at once — a member several levels deep in the tree has its facts counted once per ancestor in its path (itself included), so an ungrouped, unfiltered query against the bridge overcounts badly. The safe pattern is to filter for or group by **exactly one member, identified by its natural key** — never by surrogate key (meaningless for this purpose) and never by an arbitrary shared attribute like a department type, which can match multiple hierarchy members and silently reintroduce the same overcounting the bridge is meant to solve. Grouping by every top-level member (when rolling up) or every bottom-level member (when rolling down) is also safe, but only as long as the resulting per-group totals are never subsequently summed into one grand total — the same fact legitimately belongs to more than one group's total (a leaf node's facts appear under every one of its ancestors), so a further SUM across groups double-counts it again. When the desired filter is an attribute rather than a single member, a natural key can't express it directly — fall back to the subquery technique above rather than joining the bridge on the attribute.

Given how easy this is to get wrong, restrict direct bridge table access to trained developers rather than exposing it to end users building ad hoc reports; offering a [pathstring hierarchy attribute](pathstring-hierarchy-attribute.md) or flattened rollup as a simpler, lower-risk alternative for less experienced users is a reasonable complement.

## Multiple parents and multiple hierarchies

A bridge table can represent a node with more than one parent (e.g., joint ownership) with no structural change, but the levels-removed column must then be dropped — with more than one path connecting the same two members, a single removed-levels value isn't well defined — and the bridge must be constrained to hold only one row per member pair to avoid double-counting the same relationship twice.

When a dimension carries more than one independent hierarchy at once (e.g., a department's budgetary reporting line and its separate chain-of-command line), model **separate bridge tables**, one per hierarchy, rather than a single combined bridge with a hierarchy-name discriminator column — a shared bridge requires every query to remember to constrain on the discriminator, and a forgotten constraint silently blends two unrelated hierarchies into "wildly inaccurate and nonsensical" results. The cost of separate bridges is that a type 2 change to the dimension now ripples into every hierarchy's bridge table (see [bridge-table-type-2-ripple](bridge-table-type-2-ripple.md)), even when only one hierarchy's relationships actually changed, since all the hierarchies share the same underlying dimension rows.

## Shared ownership

The bridge table can represent partial or shared ownership by adding an **ownership percentage** column. If a node is 50% owned by each of two parents, extra path rows connect it up through both ownership chains, with the ownership-percentage column set to 50% only on the path rows that terminate at that node; any measure attributed to the shared node flows upward through both parent chains, each weighted accordingly. In an organizational or reporting-line hierarchy the same technique is called a **weighting factor** (e.g. percentage of full-time-equivalent effort) instead of an ownership percentage, and a companion **role type** column can distinguish why two nodes are connected at all (permanent line management versus a temporary, partial-effort project assignment, for instance) — the weighting factor still governs how measures allocate, while the role type is purely descriptive context for the relationship.

**Cascading weights through indirect relationships**: when a weighted relationship sits several levels removed rather than directly between parent and child, its effective weight along that longer path is the *product* of every direct relationship's own weight along the way — an employee splitting time 50/50 between two managers, one of whom in turn reports 20% of their own effort further up the chain, contributes only 0.5 × 0.2 = 10% weight to that distant ancestor's rollup, even though no direct relationship between them was ever recorded at 10%. Because a single new or changed direct relationship can alter the weight of every indirect path that passes through it, one small change can force a disproportionately large number of bridge rows to be recalculated — a change affecting a handful of direct relationships can update a third or more of an existing bridge table's rows. This is a further reason (beyond the [type 2 ripple effect](bridge-table-type-2-ripple.md)) that dropping and rebuilding a multi-parent, weighted bridge table is often more practical than updating it in place whenever history doesn't need to be preserved.

## Time-varying ragged hierarchies

Adding begin-effective and end-effective date/time-stamp columns to the bridge table accommodates a hierarchy structure that itself changes over time. When a node stops being a child of another, the old relationship's path rows get their end-effective date/time set to the change moment, and new path rows are inserted with the correct begin-effective date/time. **Queries against a time-varying bridge table must always constrain to a single date/time** to "freeze" a consistent view of the hierarchy — otherwise multiple mutually-exclusive-in-time paths get fetched together, producing an incoherent result.

## Modifying the hierarchy

**Static bridge table** (current structure only): delete the higher-level paths pointing into the moved node group, then insert new paths connecting the moved nodes to their new ancestor chain.

**Time-varying bridge table**: set the end-effective date on the affected higher-level paths to the moment of change, then insert new dated path rows for the new structure. Only the paths directly involved in the change are touched — every other path is left alone, avoiding the "nightmarish scenarios" that afflict other hierarchical modeling schemes when the tree structure itself changes.

## Trade-offs

The bridge table costs more ETL effort to build and more work at query time than a plain recursive pointer, but is the only technique among the alternatives (see [pathstring hierarchy attribute](pathstring-hierarchy-attribute.md)) that offers, together: alternative rollup structures selectable at query time, shared-ownership rollups, time-varying ragged hierarchies, and a limited blast radius both when nodes undergo [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) changes (see [bridge-table-type-2-ripple](bridge-table-type-2-ripple.md)) and when the tree structure itself changes. A single organization hierarchy bridge table can also join across multiple [fact-table](fact-table.md)s built on the same dimension simultaneously, enabling [drill-across](drilling-across.md) reports that roll all of them up from the same leaf nodes.

The same underlying structure, joined through its parent key instead of its child key, also handles a bill-of-materials hierarchy — see [parts explosion bridge table](parts-explosion-bridge-table.md). Before committing to any ragged-hierarchy bridge table, [estimate its row count and plan its display ordering](bridge-table-sizing-and-display.md).
