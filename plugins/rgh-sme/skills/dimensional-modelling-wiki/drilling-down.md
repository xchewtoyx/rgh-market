---
type: concept
title: Drilling Down
description: Adding a dimension attribute as a row header to an existing query's GROUP BY to see data at a finer level of detail.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
---

Drilling down is the most fundamental dimensional analysis technique: adding a row-header attribute — any attribute attached to the [fact-table](fact-table.md) via a [dimension-table](dimension-table.md) — to the `GROUP BY` of an existing query. Drilling up removes a row header instead. Neither operation requires predefined hierarchies or drill-down paths; any dimension attribute is a valid drill target, whether it belongs to an explicit hierarchy (e.g., product → brand → category) or to none at all (e.g., a product's fat content).

This is only possible because atomic-[grain](grain.md) fact tables carry the maximum available dimensionality — a fact table summarized above its atomic grain cannot be drilled into further, since the detail needed to add a finer row header was never captured. Drilling down within one fact table is distinct from [drilling across](drilling-across.md), which combines results from multiple fact tables via their shared conformed attributes.
