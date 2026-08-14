---
type: concept
title: Parent-Child Snapshot Rollup
description: A self-referencing surrogate key on a periodic snapshot fact table that lets users drill down through a multilevel organizational hierarchy of pre-aggregated rows.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
---

When a [periodic snapshot fact table](periodic-snapshot-fact-table.md) already holds rows at multiple levels of an ascending organizational hierarchy (department → division → enterprise, for example, in a general ledger rolled up through a reporting structure), a **parent snapshot surrogate key** lets users navigate that hierarchy directly through the fact table itself rather than through a separate dimension hierarchy technique.

The pattern adds two columns to the fact table: an explicit, single-column numeric surrogate key incrementing per fact row, and a parent-snapshot-key column on each row pointing to the surrogate key of the aggregate row it rolls up into. To drill down from a high-level row of interest, a query fetches the surrogate key of that row, then selects every row whose parent-snapshot-key matches it — directly exposing the next level's contributors, one level at a time.

This differs from a [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md), which models a variable-depth parent-child hierarchy within a *dimension*; the parent-child snapshot rollup instead self-references *fact table rows* that are themselves already pre-aggregated to different levels, useful specifically when the source data already arrives as a multilevel snapshot rather than as atomic transactions that could be rolled up on demand.
