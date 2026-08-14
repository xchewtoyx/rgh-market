---
type: concept
title: Dynamic Value Bands
description: Defining varying-sized numeric ranges for a fact at query time, via a small banding dimension table rather than an inline CASE statement.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
---

A value-banding report defines progressive, varying-sized ranges of a target numeric fact — "Balance from 0 to $10," "Balance from $10.01 to $25" — at query time rather than during ETL. This can be implemented either via a small value-banding dimension table joined through greater-than/less-than range conditions, or via an inline SQL `CASE` statement. The dimension-table approach is likely higher performing, especially in columnar databases, since a `CASE` statement forces an almost unconstrained scan of the [fact-table](fact-table.md).

This is a query-time alternative to banding a value permanently at ETL time inside a dimension — see [slowly changing dimension type 4](slowly-changing-dimension-type-4.md), where continuously variable attributes like income are banded once into a mini-dimension precisely because that banding is more efficient than dynamic value banding for frequently-run queries.

## Band definition table

The dimension-table approach holds one row per band per **band group** — a labeling column that distinguishes multiple independent sets of reporting bands (different boundary choices or precision) stored side by side in the same table — so users or report authors can pick which band group to join against at query time rather than being locked into one predefined banding. The band table's rows carry a range name for the row header (e.g., "$10,001 and up") plus a sort-order attribute, since band ranges are of unequal size and their natural sort order doesn't match a simple alphabetical or numeric sort on the name.

## Performance note

Value-band queries are, by their nature, only lightly constrained — a query might scan the balances of every account in the base with only a coarse dimension like month constrained — so the range join to the band table itself provides little to no restricting power; it doesn't reduce how many fact rows must be scanned. The recommended mitigation is to place an index directly on the numeric fact column being banded, so the database can efficiently sort and compress that column during the scan. This kind of fact-column indexing was pioneered by early columnar databases and is now a standard option on modern columnar engines.
