---
type: concept
title: Null Handling in Dimensional Models
description: Rules for when nulls are acceptable in a star schema — never in fact table foreign keys, avoided in dimension attributes, but fine in fact measures.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 6"
---

A star schema treats nulls differently depending on where they'd occur:

- **Fact table foreign keys** — nulls are prohibited. A null foreign key would violate referential integrity and prevents users from joining on it. Instead, give the referenced [dimension-table](dimension-table.md) an explicit default row (e.g., surrogate key 0 or -1) representing "Unknown," "Not Applicable," or "No Promotion" — every transaction that lacks real dimensional context still gets a valid key to join on. A default row built this way is one case of the more general [special-case dimension row](special-case-dimension-row.md) technique, which also covers invalid data, late-arriving data, and open-ended date ranges.
- **Dimension attribute values** — nulls should be avoided in favor of a descriptive string ("Unknown" or "Not Applicable"). Databases handle null grouping and constraining inconsistently: nulls effectively disappear from pull-down filter lists and report groupings unless special SQL syntax is used to surface them, and comparing a report grouped by an attribute with real nulls against one without silently changes aggregate totals — undermining user trust. Some OLAP products outright prohibit null attribute values.
- **Fact measurements** — null-valued facts behave gracefully and should be left null (not zero): `SUM`, `COUNT`, `MIN`, `MAX`, and `AVG` all handle nulls correctly, whereas substituting zero would skew every one of those calculations.

The same "no null foreign keys, no null attributes" pattern also governs dates with no known value: reserve a special surrogate date key for "date unknown at load time" in the [date dimension](date-dimension.md), and reserve default surrogate keys in any other dimension for conditions with no operational code — see [surrogate key](surrogate-key.md).
