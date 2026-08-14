---
type: concept
title: Wide Denormalized Table
description: A single very-wide table blending fact and dimension attributes together, trading star-schema structure and conformance for join-free query simplicity.
sources:
  - title: "Fundamentals of Data Engineering"
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

A wide table is a single, highly denormalized table — potentially thousands of columns, versus the handful a [fact-table](fact-table.md) or [dimension-table](dimension-table.md) typically carries — organized around one or more keys tied to the data's grain, with everything a [star-schema](star-schema.md) would otherwise split across a fact table and its surrounding dimensions folded into that one table instead. It is usually **sparse**: most fields are null for most rows.

## Why it is viable at all

Two shifts in modern columnar warehouses make this practical where it once wasn't: storage is cheap enough that redundant, sparse columns cost little, and columnar storage makes sparsity itself nearly free (nulls take almost no space, and a query only scans the columns it actually selects, unlike a row-oriented database that must allocate fixed space per field per row and read every row's full contents regardless of which columns are queried). Wide tables also tend to accrete organically through incremental **schema evolution** — adding a column is a cheap metadata change in a columnar system, unlike the more disruptive schema changes required in a normalized relational design.

## The trade-off against a star schema

Removing joins entirely can make analytics queries against a wide table outrun equivalent heavily-joined star-schema queries, since join elimination is often the single biggest performance lever available. Against that: a wide table has no explicit [conformed dimensions](conformed-dimensions.md), no declared [grain](grain.md) contract separating facts from context, and no structural distinction between additive measures and descriptive attributes — the business logic and modeling discipline a star schema makes explicit (what's a fact, what's a dimension, which dimensions conform across processes) is instead implicit in however the wide table happened to accrete. Updating a single value buried inside a wide table's nested or array-valued fields can also be markedly more costly than updating a narrow, well-grained dimension row.

## When it fits

A wide table suits situations where rigorous dimensional design isn't worth the modeling investment: highly exploratory or flexible-schema data, single-consumer tables that will never need to conform against other [business process](business-process.md)es, or a deliberate performance-first denormalization of a specific known access pattern (the same motivation behind a [consolidated fact table](consolidated-fact-table.md) or a prejoined view, just taken to an extreme). It fits poorly wherever cross-process integration, a stable audited grain, or [slowly changing dimension](slowly-changing-dimension.md) history matter — those are exactly the guarantees a disciplined star schema exists to provide, and a wide table has to reconstruct them ad hoc, per table, if it needs them at all.
