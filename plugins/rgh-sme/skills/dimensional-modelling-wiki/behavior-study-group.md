---
type: concept
title: Behavior Study Group
description: A physical table of customer durable keys captured from a complex analysis, used to constrain any schema sharing that customer dimension without rerunning the analysis.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8"
---

Some analytic questions are too complex for a single SQL statement — "customers who bought more this month than their average monthly purchase last year." A behavior study group runs the complex query (or series of queries) once to identify a customer set, then persists the customers' [durable key](durable-key.md)s as a physical, single-column table. Using durable keys rather than [surrogate key](surrogate-key.md)s makes the study group immune to subsequent [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) changes in the customer dimension.

The study group table equijoins to the customer dimension's durable key, and can be hidden under a clearly labeled view (e.g., "top 100 customers") so the schema still presents as an uncomplicated star to any BI tool, with no special syntax needed. Because study group tables are simple sets of keys, they support union, intersection, and set-difference combination — for example, intersecting this month's and last month's "problem customer" sets to find customers who were problems in two consecutive months. Adding an occurrence date column alongside the durable key enables panel studies: tracking customers who exhibit an initiating behavior (e.g., switching brands) and a follow-on behavior afterward, with accurate time-stamping to preserve sequence.

Trade-off: study group tables require a UI for capturing, creating, and administering them, and must live in the same database space as the primary fact table, since they join directly to the customer dimension — this affects DBA responsibilities beyond a normal read-only reporting schema.
