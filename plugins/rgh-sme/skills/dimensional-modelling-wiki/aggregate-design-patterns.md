---
type: concept
title: Aggregate Design Patterns
description: The three ways to build an aggregate fact table from a base fact table, in increasing order of complexity and acceleration.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 15"
---

An [aggregate fact table](aggregate-fact-table.md) is built from a base fact table one of three ways, in increasing order of complexity:

- **Lost dimension aggregate**: drop a subset of dimensions from the base table entirely and sum what remains — for example, dropping customer and store from a sales fact table to leave only date and product. This is the simplest to build, since it needs no dimensional joins at all (`CREATE MATERIALIZED VIEW ... AS SELECT date_key, product_key, SUM(revenue) FROM sales_fact GROUP BY date_key, product_key`). At least one of the dropped dimensions must itself be a [grain](grain.md)-defining dimension, or the "aggregate" won't actually be smaller than the base table.
- **Shrunken dimension aggregate**: replace one or more base dimensions with a [shrunken dimension](shrunken-dimension.md) rollup — dates rolled up to months, stores rolled up to regions — often combined with dropping the most granular remaining dimension outright (customer, say), since keeping it would leave the aggregate nearly as large as the base table. More complex to build (needs the rollup dimensions themselves, plus joins to derive them), but can satisfy a broader range of queries than a lost-dimension aggregate. A rollup dimension's own surrogate key can conveniently reuse a base dimension key value it maps to — a MONTH key equal to the DATE key of that month's last day, say — the specific value chosen doesn't matter as long as it's applied consistently. If the rollup dimension carries a type 1 attribute, see the [type 1 aggregate-maintenance trap](type-1-aggregate-maintenance-trap.md) for a hazard specific to this pattern.
- **Collapsed dimension aggregate**: summarize using selected dimensional *attributes* directly, storing facts and the attributes they're grouped by together in one denormalized table (sales by quarter and product type, with no separate join back to a date or product dimension at all). This offers the most acceleration, since the join itself is precomputed away, but risks becoming too wide if too many attributes are folded in — a 20× reduction in row count paired with a 3× increase in row width delivers far less net benefit than the row-count reduction alone suggests.
