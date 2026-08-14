---
type: concept
title: Current-Value View Over a Type 2 Dimension
description: Deriving a current-value (or as-at) swappable dimension from an always-tracked type 2 dimension via a self-join, instead of choosing type 1 or type 2 upfront per attribute.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Stakeholders often want both "as was" reporting (facts grouped by the dimension values that were true at the time each fact occurred) and "as is" reporting (facts grouped by the dimension's values today) over the same attributes — an expense report by employee location needs the historically correct location, while a headcount report for "employees currently based in London" needs only today's location. Rather than deciding [type 1](slowly-changing-dimension-type-1.md) versus [type 2](slowly-changing-dimension-type-2.md) per attribute and losing history for whichever one is picked, build and maintain the dimension as fully [type 2](slowly-changing-dimension-type-2.md) (historic value, "as was" reporting), and derive a separate current-value view from it.

## The self-join technique

The current-value view is a self-join of the type 2 dimension against a copy of itself filtered to only current rows (`current = 'Y'`): every historical version of an entity joins, through its durable or natural key, to that entity's one current row. The result looks redundant at first glance — three historical rows for the same employee all showing that employee's present-day location and status — but each retains its own distinct historical [surrogate key](surrogate-key.md), so when this view is used in place of the base dimension, every fact from every era of that entity's history rolls up correctly to its current description. Because the current-value view shares identical column names and structure with the base historic-value dimension, the two are [hot swappable](hot-swappable-dimension.md) — a query or BI tool can substitute one for the other with no rewriting.

The same self-join technique, with the filter changed from "current" to a specific date (`'2011-04-04' BETWEEN effective_date AND end_date`), produces an **as-at** or year-end dimension instead — a frozen view of the dimension exactly as it stood on that date, useful for point-in-time comparisons (e.g., year-end organizational snapshots) without any extra ETL beyond the type 2 history the base dimension already carries.

## Materialization trade-off

Build the current-value view as an ordinary database view for simplicity — it costs nothing until first used and always reflects the latest current-flagged rows. If the self-join runs inside every query that uses it becomes a performance problem, materialize it as a real table or materialized view instead, refreshed whenever the base dimension's current flags change.

## Why defaulting to type 2 and deriving type 1 is the resilient choice

Building the base dimension as type 2 from the start and deriving a current-value view later, only once stakeholders actually ask for "as is" reporting, costs nothing extra if the view is built as a plain view — a genuinely deferrable decision with no rework. The reverse path is far more expensive: a dimension built type 1 from the start has already destroyed the history a later type 2 requirement would need, and retrofitting history onto an established warehouse can mean updating foreign keys on hundreds of millions of existing fact rows. Unless a dimension is large enough that type 2 tracking itself becomes the problem (see [monster dimension](splitting-wide-dimension-tables.md) techniques), defaulting to full type 2 history and exposing a current-value view is the safer bet in both directions.

## Combining current and historic values in one query

A historic-value dimension and its current-value view aren't mutually exclusive — both can be joined into the same query at once (for example, to group by historical city while filtering on current city). If this combination is common enough to be worth avoiding a second join, build a single **hybrid dimension** carrying both the historic-value and current-value versions of the relevant attributes side by side on one row, rather than joining the base dimension to its own current-value view every time.
