---
type: concept
title: Special-Case Dimension Row
description: A dedicated dimension row with a real surrogate key and non-null attribute values, used in place of a null foreign key whenever a fact can't be related to a real dimension member.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 6"
---

Whenever a fact row can't be related to a real [dimension-table](dimension-table.md) row, the fix is to add a special-case row to the dimension rather than storing a null foreign key on the fact — see [null handling in dimensional models](null-handling-in-dimensional-models.md) for why nulls in fact-table foreign keys and dimension columns cause silent, hard-to-catch reporting errors. The special-case row gets a real [surrogate key](surrogate-key.md) (e.g. `0`) and non-null values in every column (e.g. "n/a"), avoiding both the foreign-key-null problem and the column-null problem simultaneously.

## Browsability impact and fix

A special-case row still shows up in plain [browse queries](browse-query.md) and confuses users ("what is this 'n/a'?"). Add a `row_type` column (values like "standard"/"special", or more specific labels such as "Salesrep"/"No Salesrep") so browse queries can filter it out (`WHERE salesrep.row_type = "Salesrep"`) — but this filter must be *removed* when querying the fact table, or the special-case fact rows would be wrongly excluded from results that should include them.

## Four uses

1. **Optional relationships** — legitimate when the dimension isn't part of the fact table's stated [grain](grain.md) (e.g. "one row per order line" with an optional salesperson). If a stated grain itself *requires* an optional dimension, that signals a confused design that will hamper analysis — see [single vs. multiple fact tables](single-vs-multiple-fact-tables.md) for the related grain-mismatch problem.
2. **Invalid data** — when a source transaction references a natural key absent from the dimension (e.g. an unvalidated product code from an order-entry system), point the fact at a special "Invalid" row (e.g. surrogate key `0`) rather than dropping the transaction or using null. Store the transaction identifier as a [degenerate dimension](degenerate-dimension.md) on the fact table so a cleanup query can find and correct the affected transactions later.
3. **Late-arriving data** — in a real-time or frequent-load warehouse, a transaction may arrive referencing a dimension value not yet loaded (e.g. a brand-new product code). Rather than hold the transaction, point it at an "Unknown" special row (e.g. surrogate key `1`); again store the transaction identifier so the row can be corrected with the real surrogate key once the dimension catches up. Contrast with [late arriving facts](late-arriving-facts.md), where the dimension member already exists but the fact needs to be matched to the historical version of it that was in effect at event time.
4. **Future events (no expiration)** — for fact rows carrying an effective/expiration date pair, an unexpired row has no natural expiration date. A null expiration date breaks range comparisons (`effective_day.full_date <= X AND expiration_day.full_date >= X`) even under an outer join. Fix: a special [date dimension](date-dimension.md) row (e.g. surrogate key `0`) using an arbitrary far-future date (e.g. 12/31/9999) for unexpired rows — a small-scale analog of the Y2K problem, so any query computing duration or tenure from the date pair must special-case unexpired rows to use the actual current date rather than the sentinel date.

The star should always record sufficient transaction identifiers alongside a special-case reference to allow the anomalous record to be identified and corrected in the future — the goal is to avoid excluding facts from the warehouse entirely, not merely to avoid nulls.

A related but distinct need is a [multi-level dimension](multi-level-dimension.md), which adds special rows representing entire higher hierarchy levels (not missing or invalid data) for a business process whose events genuinely vary in which level of detail they describe.
