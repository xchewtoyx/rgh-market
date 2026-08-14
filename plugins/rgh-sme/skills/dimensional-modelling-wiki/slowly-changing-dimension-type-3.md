---
type: concept
title: "Slowly Changing Dimension Type 3: Add New Attribute"
description: Adding a new column to hold the prior attribute value while the original column is overwritten, so both values can be queried simultaneously.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 5"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 8"
---

Type 3 adds a new column to hold a prior attribute value rather than issuing a new row; the original attribute is overwritten (as in [type 1](slowly-changing-dimension-type-1.md)) to the current value, while the new "prior X" column retains the old value. This enables querying fact data by *either* the new or the prior value at the same time — "alternate realities." It differs fundamentally from [type 2](slowly-changing-dimension-type-2.md): type 2 strictly partitions history by time (a fact row is associated with exactly one version, the one in effect when the event happened), while type 3 regards the current and prior values as both true simultaneously. Because every fact row keeps pointing at the same, unchanged dimension surrogate key across the change, type 3 does *not* preserve which value was actually in effect at the moment any individual fact occurred — that question still requires type 2.

## An ill-advised alternative: natural key as the fact table's foreign key

A tempting but broken way to get "query by either value" behavior is to type-2 the dimension as usual, but store the entity's *natural* key (not its surrogate key) as the fact table's foreign key, letting a query join to whichever dimension version it wants via an explicit filter. This requires every query against that fact table to carefully qualify the dimension join, or risk silently double-counting facts across the multiple dimension rows that now share one natural key — a trap that untrained users cannot be expected to avoid. Model the requirement as type 3 (or a [type 6](slowly-changing-dimension-type-6.md) hybrid) instead of reaching for this shortcut.

Type 3 is infrequently used — the technique numbering in [slowly changing dimension](slowly-changing-dimension.md) is not a good/better/best ranking. It is not useful for attributes that change unpredictably (e.g., a customer's home state), since there's no benefit to a single prior-value column when different rows changed at wildly different times — type 2 fits unpredictable changes better. Type 3 is best suited to a significant, en-masse change affecting many dimension rows at once (a product line or sales force reorganization), where users want both pre- and post-reorg views for a transitional period. Prior-value columns should be labeled to clarify the pre-change grouping (e.g., "2012 department," "pre-merger department") — labeling can ripple into the BI layer. If the type 3 attribute is a hierarchical rollup attribute, an [olap-cube](olap-cube.md) built on it likely needs reprocessing, as with type 1.

## Multiple type 3 attributes

For attributes that change on a predictable rhythm (e.g., a product line recategorized every year), the technique generalizes to keeping a current attribute (overwritten each cycle) plus one column per historical designation ("2012 department," "2011 department," ...). Values are "Not Applicable" for periods before the entity existed. The most recent/current column should be clearly labeled "current X" so it doesn't need renaming every cycle; on each reassignment, a new year column is added, populated from the outgoing current value, and the current column is overwritten with the new assignment.

Naming the historical columns by absolute year (`region_2009`, `region_2008`, ...) is workable but forces a DBA column rename/add every cycle and forces every dependent report to be redesigned each year to reference the new column name. Relative naming (`region_current`, `region_last_year`, `region_two_years_ago`) is generally preferable — the columns' meanings stay fixed release over release, and only their contents shift, so reports built against them keep working without redevelopment; the ETL process itself simply shifts each column's contents down one slot before loading the new current value.
