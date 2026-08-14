---
type: concept
title: Numeric Value as Fact or Dimension Attribute
description: The rule for deciding whether an ambiguous numeric value (e.g., a standard price) belongs in the fact table, a dimension, or both.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
---

Some numeric values are genuinely ambiguous under the general [fact-table](fact-table.md) fact-vs-attribute test — a product's standard list price is the canonical example. If the value is used mainly for calculation, it belongs in the fact table, even if it's individually non-additive itself: it can still be multiplied by quantity to derive an additive extended amount, or a price-variance metric can be stored instead. If the value is used mainly for filtering or grouping, it belongs as a [dimension-table](dimension-table.md) attribute — optionally supplemented with a value-band attribute (e.g., "$0-50") for coarser grouping.

If the value genuinely serves both purposes, store it in **both** places — for example, a fact-table standard price capturing valuation at the time of a specific sale, plus a dimension attribute labeled as the *current* standard price for filtering. The general rule: "data involved in calculations should be in fact tables and data involved in constraints, groups, and labels should be in dimension tables," even where a clever application could derive one value from the other — consistency and predictable simplicity across every application matters more than avoiding a small amount of redundancy.
