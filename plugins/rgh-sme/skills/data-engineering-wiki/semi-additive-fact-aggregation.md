---
type: concept
title: Semi-Additive Fact Aggregation
description: >
  Why a level-or-balance measure (inventory on hand, account balance) sums
  correctly across every dimension except time, and the query pitfall that
  silently breaks its time aggregation if not handled deliberately.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 4"
---

A **semi-additive** fact records a level or balance at a point in time —
quantity on hand in a periodic inventory snapshot, a daily account balance —
rather than an event or a flow. It sums validly across every dimension
except the date dimension: summing five stores' end-of-day inventory for the
same day is correct, but summing one store's inventory across seven days is
not, since that's adding up seven separate snapshots of a level rather than
seven separate events. The valid aggregation across time is an **average**
over the number of time periods, not a sum — the same "correct-aggregate"
concern that makes a [non-additive ratio](ratio-decomposition-and-derived-fact-materialization.md)
need special handling, just for a different reason: here the fact itself is
additive along every dimension but one.

**Query pitfall**: `SELECT AVG(quantity_on_hand)` in SQL averages over
however many rows the query returns, not over the number of distinct dates
in scope — averaging inventory for 3 products across 4 stores over 7 dates
naively divides the sum by 84 (3 × 4 × 7) rows returned, not by the 7 dates
that's actually the correct divisor. Getting the average right requires
either pre-aggregating to one row per date first, or explicitly dividing by
`COUNT(DISTINCT date)` rather than relying on a bare `AVG`. This is a
correctness trap for both ETL logic that pre-computes rollups and any
downstream query or report built directly against the fact table.
