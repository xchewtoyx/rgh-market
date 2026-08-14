---
type: concept
title: Browse Query
description: A query that explores the distinct values within a single dimension table without touching the fact table.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 1"
---

A browse query selects distinct values from one [dimension-table](dimension-table.md) alone (e.g. `SELECT DISTINCT category FROM product`), without joining to the [fact-table](fact-table.md). It answers "what values exist here?" rather than "how do measurements break down?"

Browse queries serve several purposes: producing standalone reference data or pick lists, letting a user preview available filter values before writing a larger fact-table query, and letting users explore relationships between dimension values (e.g. which categories exist within a department) — observations that can themselves inform how attributes should be grouped into dimension tables.
