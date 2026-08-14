---
type: concept
title: Aggregated Facts as Dimension Attributes
description: Placing a precomputed summary metric, often banded, directly on a dimension row as a constraint target and report label.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 6"
---

Selected aggregated performance metrics — for example, a customer's total spend last year or lifetime — can be placed directly on a [dimension-table](dimension-table.md) row as constraint targets and report row labels, often as banded ranges rather than raw values. This moves ETL work (computing and refreshing the aggregate) onto the back room in exchange for easing the BI-layer analytic burden, since users can then filter or group on the metric like any other dimension attribute instead of computing it from the [fact-table](fact-table.md) at query time.

Because the value is recomputed periodically rather than continuously, this technique suits metrics where some staleness is acceptable — contrast with [dynamic value bands](dynamic-value-bands.md), which bands a fact value at query time instead, and [slowly changing dimension type 4](slowly-changing-dimension-type-4.md), which is the appropriate technique when a banded attribute needs point-in-time historical accuracy on the fact table rather than just a current dimension attribute.

## Behavioral dimensions, more generally

This is one of three techniques for answering a **behavioral question** — a question that groups or filters facts based on the *past behavior* of dimension members, effectively using a fact as if it were a dimension attribute (e.g. "are customers who generate over $1 million in orders receiving better discounts than those who generate less?"). Answered directly at query time via a correlated subquery or procedural SQL, behavioral questions perform poorly (often forced into scheduled batch windows, breaking the normal ask-a-new-question cycle) and are beyond the skill of most end users and even junior analysts. A **behavioral dimension** pushes that computation into ETL instead, extending an existing dimension table with precomputed columns, via any of:

1. **Past association with another dimension** — store a date (or other reference) marking a past event of interest directly on the dimension row, e.g. `first_order_date` and `last_order_date` on customer, so a query can filter on a customer's most recent activity without touching the fact table at all.
2. **Historic fact** — the technique described above: an aggregated or qualified fact value (e.g. `annual_sales`) stored directly on the dimension row.
3. **Categorizing facts ("banding")** — bucketing a historic fact into named ranges as a separate attribute (e.g. `annual_sales_group`), better suited to `GROUP BY` than the raw value.

## Design constraint: behavioral attributes must be type 1

A behavioral attribute must always be handled as [slowly changing dimension type 1](slowly-changing-dimension-type-1.md) (overwrite), never type 2 — versioning `last_order_date` as type 2, for instance, would generate a new dimension row on every single order, defeating any control over table growth. If a genuinely historic version of a behavioral attribute is needed (e.g. "what was each customer's last order date as of last February?"), fall back to querying the fact table directly rather than trying to version the behavioral column.

Refresh frequency also needs deliberate design: recomputing a behavioral attribute too often can overload ETL (e.g. recomputing a trailing year of sales for every customer nightly may be excessive) — define the attribute on a coarser cadence instead (e.g. "sales for the prior four quarters," refreshed quarterly) and document that cadence clearly for users, so the column's currency isn't misinterpreted. As with the type 1 constraint above, genuinely up-to-the-moment figures remain available by querying the fact table directly when that rare need arises.
