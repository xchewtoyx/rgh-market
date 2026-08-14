---
type: concept
title: Shrunken Dimension
description: A conformed dimension containing a strict row and/or column subset of a base dimension, used when a fact table's grain is coarser than the atomic dimension.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 5"
---

A shrunken dimension is a [conformed dimension](conformed-dimensions.md) that is a subset of the rows and/or columns of an atomic base dimension. It is required whenever a fact table naturally captures data at a higher grain than the base dimension — for example, an [aggregate fact table](aggregate-fact-table.md), a forecast captured by month and brand rather than by date and product, or a monthly inventory snapshot rolled up from a daily one.

A **hot level** — a hierarchy level stakeholders name when asked where plans, budgets, forecasts, or targets are set (see [hierarchy chart](hierarchy-chart.md)) — is the discovery-time signal that a rollup dimension at that level will be needed, since planning data is rarely captured at the same atomic grain as the transactions it gets compared against.

Two variants:

- **Row-and-column subset (rollup):** the shrunken dimension holds fewer attributes than the atomic dimension. It still conforms as long as the attributes it does carry (e.g., brand, category descriptions) are identically labeled, defined, and valued in both tables. The atomic and rollup tables have separate primary keys.
- **Row subset:** the shrunken dimension holds the same attributes as the atomic dimension but only a subset of rows (e.g., a single business line's products out of the corporate product dimension). A fact table joined to a row-subsetted dimension must itself be limited to the same row subset, or referential integrity is violated and results become unpredictable.

A month dimension derived from a daily [date dimension](date-dimension.md) is a common example of combined row-and-column subsetting: it keeps only month-end date rows, and drops columns that don't apply at monthly grain (weekday/weekend indicator, week-ending date, holiday indicator).

On the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md), a shrunken dimension is not given its own column — the atomic dimension's cell is marked, with the rollup/subset grain noted textually within the cell, or the column is subdivided to show the common grains that occur (e.g., day and month).

## Content requirement for the rollup variant

A row-and-column-subset (rollup) dimension has exactly one column absent from its base dimension: its own surrogate key — every other shared attribute must match the base dimension in both structure and content. The content requirement is strict: instance values must be identically expressed (e.g. "January" spelled the same way in both the atomic dimension's month attribute and the rollup's month attribute), and **every distinct combination of shared-attribute values present in one table must be present in the other** — otherwise a [browse query](browse-query.md) against each table disagrees, and [drilling across](drilling-across.md) on the shared attribute silently loses or skews rows. Best practice is to designate the base (atomic) dimension as the rollup's authoritative source — either processing base-then-rollup sequentially, building one ETL routine that updates both simultaneously, or normalizing through a staging area at the atomic level before applying changes to both.

One ETL quirk to plan for: a [type 1 change](slowly-changing-dimension-type-1.md) applied to the base dimension can force two rows in the rollup dimension to merge (e.g. two products in different categories get corrected to the same category, collapsing what were two distinct category rollup rows into one). Because the surrogate keys of the now-merged rollup rows may already be referenced by existing facts, this forces foreign-key updates in every fact table that references the rollup — rollup tables are sometimes deliberately permitted to keep rows that are identical except for surrogate key, purely to avoid that extra processing.
