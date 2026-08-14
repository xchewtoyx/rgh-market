---
type: concept
title: Insert-Only Accumulating Snapshot
description: A variant of the accumulating snapshot that preserves full history by inserting a new row per status change instead of updating in place, at the cost of more complex load logic.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4, 16"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

Destructive in-place updating is what makes a classic [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) lose intermediate states — a process that can revisit an earlier status after moving forward (a claim moving opened → denied → closed → disputed → reopened → closed, for example) loses every state but the current one. Rather than reaching for a wholly separate companion table, the accumulating snapshot itself can be adapted using the same row-versioning discipline as a [slowly changing dimension type 2](slowly-changing-dimension-type-2.md): add a snapshot start date, snapshot end date, and a current-row flag to the table, and instead of updating a row in place, insert a new row for the changed status and update only the administrative start/end/flag columns on the row it supersedes. Most consumers just need a view filtered to the current-flag rows, behaving like the classic design; a minority who need "status as of any past date" filter on the start/end date range instead. This preserves full history at the cost of materially more complex load and maintenance logic than the classic destructive-update design.
