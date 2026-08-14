---
type: concept
title: Timespan Tracking in Fact Tables
description: Adding row-effective and row-expiration date/time stamps to a fact table so one row can represent an unbroken span during which a status was constant.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8, 19"
---

In isolated cases it's useful to add a row-effective date/time, row-expiration date/time, and current-row indicator to a [fact-table](fact-table.md), analogous to a [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) row. This captures a **timespan** during which a status was constant, rather than forcing a fact row per period as a [periodic snapshot fact table](periodic-snapshot-fact-table.md) would — useful for scenarios like a slowly changing balance where a frequent snapshot would otherwise load many identical rows.

## Precise timespan pairs

A more precise form pairs each fact row with the exact moment of the transaction and the exact moment of the *next* transaction, forming an unbroken sequence with no gaps between rows. The span between the two stamps is a "quiet span" during which demographics or status were constant, and supports three query patterns directly:

- **Point-in-time**: `BeginEffDateTime <= target AND EndEffDateTime > target`.
- **Range overlap**: finding every row whose span overlaps a target date range at all.
- **Duration aggregation**: `SUM(LEAST(end, range_end) - GREATEST(begin, range_start))`, which correctly handles every way a row's span can straddle the query range (fully inside, spanning the start, spanning the end, or spanning both).

**Back-room administration**: don't set a row's end-effective stamp one "tick" before the next row's begin-effective stamp — the resulting gap risks losing a transaction that falls exactly within it. Instead set end-effective exactly equal to the next row's begin-effective stamp. Loading is a two-step ETL process: (1) the new row's end-effective is set to a fictitious far-future date/time (preferred over NULL, which complicates equality constraints and can error — see [null handling in dimensional models](null-handling-in-dimensional-models.md)), then (2) after the insert, the ETL process retrieves the prior row and updates its end-effective to the new row's begin-effective. This extra back-room ETL overhead is a deliberate trade-off for reduced front-room query complexity.

## Compliance-driven variant

The same insert-only, timespan-stamped structure can be applied to an entire fact table, not just to a status or balance fact, when the business has a compliance obligation to preserve a full chain of custody for every value a fact row ever held — showing exactly what the row contained at any point in time it was under warehouse control. A compliance-enabled fact table adds five columns to the original design: a fact table surrogate key (a single integer shared by every version of the same underlying row, distinct from the row-versioning columns), a begin-version date/time (when this version was created), an end-version date/time (a far-future placeholder until the row is superseded, then set to the exact superseding instant), a change reference (e.g., "original" for the first version, otherwise an explanation of why the row changed), and a source reference (the originating operational source, or the source of any revised columns). This effectively bans [slowly changing dimension type 1](slowly-changing-dimension-type-1.md)- and [type 3](slowly-changing-dimension-type-3.md)-style in-place overwrites on the fact table: every correction becomes an insert of a new row sharing the same fact table surrogate key, with the superseded row's end-version stamp set to that same instant — letting both "what did we believe as of date X" and "the full revision history of this one row" be reconstructed directly. Because it serves a different purpose than BI query performance, a compliance-enabled table can run alongside a normal, unaugmented operational fact table and need not carry the indexing the front-room table does.
