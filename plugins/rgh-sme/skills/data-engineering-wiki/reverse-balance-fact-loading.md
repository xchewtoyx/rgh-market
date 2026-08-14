---
type: concept
title: Reverse-Balance (Mirror-Image) Fact Loading
description: >
  Recording a fact change as two new rows — a negating reverse of the old
  value and the new value — instead of updating in place, so plain SUM
  aggregation stays correct at every point in time without window functions.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 14"
---

A fact table is supposed to be an append-only record of what happened, but
source systems do update facts after the fact — an order line's quantity
gets corrected from 2 to 1, say. Naively inserting both the original and
corrected rows (an [insert-only pattern](insert-only-history-pattern.md))
breaks plain aggregation: summing quantity across both rows gives 3 when the
true current total is 1, and there's no way to tell, from the rows alone,
which one superseded the other without a window function or a lookback
comparison at query time.

**The reverse-balance technique** fixes this at load time instead of query
time: on any change, insert *two* rows — the new value, and a **reverse
balance** row that exactly negates the prior value's additive measures. A
single update produces three rows total in the table: the original, its
negation, and the new value. Two structural additions make this work:

- An **as-at date** (or timestamp) marking the point in time each version
  became true, replacing a plain load date.
- A **before/after-image flag**, included in the table's key alongside the
  as-at date, distinguishing the negating row from the genuine new value.

With this structure, every business question becomes a plain `SUM` filtered
by `as_at_date` and the image flag — no window functions, no lag
comparisons — which matters because plain aggregation is exactly what
columnar OLAP storage is optimized for: total-to-date, the delta on a given
day, and "as it looked on date X as of what we knew on date Y" are all just
different filter combinations over the same rows.

One detail that matters for correctness: only **additive and
[semi-additive](semi-additive-fact-aggregation.md)** measures get negated in
the reverse-balance row — a non-additive measure
like a discount percentage is carried through unchanged, since negating it
would produce a meaningless value rather than a correct offsetting entry.

This pattern pairs naturally with a
[change stream](change-stream-consumption-pattern.md): a merge's captured
before-image is exactly the row that needs negating, so the reverse-balance
insert can read directly off the stream instead of computing "what was this
row before?" separately.
