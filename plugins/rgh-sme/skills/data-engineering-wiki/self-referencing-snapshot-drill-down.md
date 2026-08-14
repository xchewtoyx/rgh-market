---
type: concept
title: Self-Referencing Snapshot Drill-Down
description: >
  Letting a periodic-snapshot fact table represent a rollup hierarchy by
  having each row point to its own parent row in the same table, instead of
  requiring a separate hierarchy structure.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 7"
---

When a periodic-snapshot fact table's own organizational or account
dimension is arranged in an ascending rollup hierarchy (department → division
→ enterprise), a query needing to drill down from a high-level total to its
contributing detail rows can't do that with the fact table's normal
dimension foreign keys alone — those describe *what* each row measures, not
*which other row it rolls up into*.

The load-time fix is a **self-referencing surrogate key**: give the fact
table its own single-column, sequentially assigned [surrogate
key](surrogate-key-range-recovery.md), and add a second column — a parent
key — pointing at the surrogate key of whichever other row in the *same*
table this row's amount rolls up into. Drilling down from a summary row then
means grabbing its surrogate key and querying for every row whose parent key
matches it, which finds the next level of contributors without a separate
hierarchy or bridge table at all — the hierarchy is expressed entirely
within the fact table's own rows.

This differs from ordinary parent/child fact table designs, where the parent
key references a row in a *different*, higher-grain fact table: here both
the summary and detail rows are the same kind of measurement, in the same
table, at the same grain, related only by which organizational level they
represent.
