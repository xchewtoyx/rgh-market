---
type: concept
title: Reverse Balance (Mirror Image) Fact Table
description: A fact table pattern that records a correction as a negating row plus a new row, so plain SUM aggregation stays correct without window functions.
sources:
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 14"
---

Source systems routinely correct facts after the fact — an order line's quantity is edited, a booking is amended — and the warehouse must capture both the correction event and the fact's true history without distorting downstream totals. Naively landing every raw version of a changed record and summing over them double-counts: if a line item's quantity changes from 2 to 1, a plain `SUM(quantity)` over both raw rows yields 3, not the correct current value of 1 or the correct as-was value of 2.

## Mechanism

On any change, insert **two** rows instead of overwriting the original in place:

1. A **reverse balance row** that exactly negates the additive and semi-additive measures of the value being replaced (same [grain](grain.md) and dimensional context, but with sign flipped on the numeric measures).
2. The new ("after") row carrying the updated values.

A single change therefore produces three rows in total across the record's lifetime: the original, its negation, and the replacement — and any plain `SUM` over the table nets out to the correct answer at any point in its history, because the negation and the value it cancels always sum to zero once both are present.

Two structural additions distinguish this table from a plain append-only fact table:

- **As-at date/timestamp** — replaces an ordinary load date; represents the point in time for which a given row's value is asserted to hold, not merely when it was loaded.
- **Before/after-image flag** — included in the table's key, distinguishing a genuine after-image row from the reverse-balance row that negates the prior value.

Only additive and semi-additive measures get negated; non-additive measures (ratios, percentages, discount rates) are carried through unchanged on the reverse-balance row, since negating a non-additive value would be meaningless — see [additive fact](additive-fact.md), [semi-additive fact](semi-additive-fact.md), and [non-additive fact](non-additive-fact.md).

## Why this beats window-function reconstruction

Without this pattern, answering "what was the total as of the original as-at date" versus "what does the total look like today, incorporating corrections since" requires `LAG`/window-function comparisons across raw record versions at query time — expensive at scale and easy to get subtly wrong. With reverse-balance rows already materialized, both questions become plain `SUM(...) WHERE asat_date <= '<some date>'` filters, letting a columnar aggregation engine answer them directly. This trades ETL complexity (generating the negating row on every change) for query-time simplicity and correctness.

## Handling physically deleted source records

A related problem: fact tables are usually loaded incrementally (only changed or new rows since the last load), so a row that is physically deleted at the source simply stops appearing in the incremental feed — there is no explicit signal that it's gone, and the warehouse silently drifts out of sync with the source. Detecting this by looking backward (comparing the full fact table against the latest load to see what vanished) is expensive at fact-table scale.

The pattern resolves the same way as an ordinary correction: insert a **logical deletion row** — a reverse-balance row that zeroes out the deleted record's additive measures — stamped with the as-at date of the *next* load after the deletion was detected, rather than trying to reconstruct exactly when the deletion occurred at the source. This turns a deletion into an ordinary forward-flowing correction event instead of a special backward-reconciliation case, and it generalizes to any fact table design that needs to recover physically deleted source rows, not just tables using the reverse-balance pattern specifically.
