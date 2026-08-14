---
type: concept
title: Semi-Additive Fact
description: A numeric fact that can be summed across some dimensions but not across time, such as a balance or inventory level.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-4"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 11"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 8"
---

A semi-additive fact can be summed across most dimensions attached to its [fact-table](fact-table.md), but not across the date/time dimension. Financial account balances and inventory quantity-on-hand are the canonical examples: a balance sums validly across accounts or products, but summing balances across dates produces a meaningless number — it's the same underlying error as adding a checking account's daily balances across a week. The dimensionally correct aggregate across time is an average over the number of time periods, not a sum.

This matters most in [periodic snapshot fact table](periodic-snapshot-fact-table.md)s, where a row records a level or balance at a point in time rather than an event. A common pitfall: SQL's `AVG` function averages over every row returned by a query, not just the number of distinct dates represented — averaging inventory across 3 products × 4 stores × 7 dates via a naive `AVG` divides by 84 instead of the correct divisor of 7. [OLAP cube](olap-cube.md) products that support cube-level aggregation rules handle semi-additive measures more gracefully than plain SQL aggregation.

An enhanced inventory snapshot often stores a semi-additive balance (quantity on hand) alongside fully [additive fact](additive-fact.md)s such as quantity sold, so that velocity metrics (turns, days' supply) can be computed without mixing additivity types in the same aggregation. Some schemas instead store beginning balance, delta, and ending balance per row — the balances stay semi-additive, while the delta is fully additive across all dimensions including time.

## Stored counts are often semi-additive or worse

A count fact (order count, distinct-customer count) stored in a [periodic snapshot fact table](periodic-snapshot-fact-table.md) for query efficiency is frequently semi-additive, or even non-additive, in a way that isn't obvious from the column looking like an ordinary number. A count of orders per product per day sums correctly across days or stores as long as the query stays constrained to a single product — but summing it across products double-counts any order that contained more than one of them, since that order was already counted once under each product it touched. Unlike the balance-across-time case, there is no valid dimensional aggregate that fixes this within the snapshot itself: a count that was correct only at the specific grain and dimensional combination it was captured at cannot be safely re-aggregated across a dimension that combination didn't already account for. The only correct fix is to go back to the underlying atomic-grain [transaction fact table](transaction-fact-table.md) and compute `COUNT(DISTINCT ...)` on the natural identifier in the query's actual context — a snapshot's stored count is a convenience for the specific slices it was built for, not a substitute for a real distinct count at a different slice. A [degenerate dimension](degenerate-dimension.md) transaction identifier is a useful way to think about this: it can never be summed as a fact, but it can always be counted distinctly at the atomic grain to produce a correct additive count, which is exactly why atomic-grain fact tables are required to answer unique-count questions reliably where a pre-aggregated snapshot cannot.

## The "problem" dimension isn't always time

Date/time is the most common non-summable dimension, but it isn't the only one a semi-additive fact can have. Any dimension that distinguishes otherwise-comparable versions of the same measurement behaves the same way — for example, a sales-goal fact that sums cleanly across months or territories, but not across sales-plan versions: two different plans both targeting the same month can't have their goal dollars added together, since doing so blends two competing hypotheses about the same period rather than describing anything real. Budget versions in financial systems follow the identical pattern. The general rule stays the same regardless of which dimension plays this role: never sum across it, but summarize across it with `MIN`, `MAX`, or `AVG` instead, and query/reporting tools should either force a single-value constraint on that dimension or group by it explicitly, including inside subtotals and grand totals.

Contrast with fully [additive fact](additive-fact.md)s and [non-additive fact](non-additive-fact.md)s.
