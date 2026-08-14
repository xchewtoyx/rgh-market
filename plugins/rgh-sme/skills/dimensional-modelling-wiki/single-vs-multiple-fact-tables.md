---
type: concept
title: Single vs. Multiple Fact Tables
description: Decision framework for whether a set of related transactions along a value chain should be blended into one fact table or split into several.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 5"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 4"
---

When several related transaction types sit along a [value chain](value-chain.md) (for example, purchase requisitions, purchase orders, shipping notices, receipts, and vendor payments in procurement), there is "no simple formula" for deciding whether to blend them into a single [transaction fact table](transaction-fact-table.md) or split them into separate ones. Weigh:

- **Users' analytic requirements** — which structure matches how business users naturally think about and query the data, minimizing complexity for them.
- **Are these really multiple distinct [business process](business-process.md)es?** Each having its own unique control number (its own [degenerate dimension](degenerate-dimension.md), such as a separate PO number and payment check number) is a strong clue that they are separate processes, favoring separate fact tables. Conversely, varied transactions that are really steps within one process (e.g. all the movement types in an inventory process) favor a single blended fact table.
- **Do the transaction types originate from different source systems with different granularities?** Distinct source systems favor separate fact tables.
- **Does the dimensionality differ per transaction type?** Attributes that apply to only some transaction types (e.g. "discounts taken" applying only to vendor payments, or a receiving-employee attribute applying only to receipts) favor separate fact tables — forcing everything into one blended table pushes dimension and attribute names toward lowest-common-denominator generalizations (e.g. "purchase order date" and "receipt date" collapsed into one generic "transaction date"), which reduces legibility for business users.

An embellished [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md) — with atomic grain and metrics columns added per row — helps surface these trade-offs on paper before building the schema.

Splitting into multiple fact tables means more tables to load, index, and aggregate, which is sometimes argued to add ETL complexity. In practice, loading each source system independently into its own fact table is usually *less* complex than integrating multiple heterogeneous sources into one blended table. Later fact tables along the chain typically inherit [conformed dimensions](conformed-dimensions.md) from earlier steps, and separate fact tables can still be tied together via [drilling across](drilling-across.md) or by a complementary [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) that tracks a pipeline instance across all the steps.

## A sharper test: apply it to a pair of facts, not a whole process

A more mechanical way to decide, applied to any two candidate facts rather than to the process as a whole: do they belong in the same fact table only if the answer to *both* of the following is "yes"?

1. **Do the facts occur simultaneously?** `quantity_ordered` and `quantity_shipped` fail this — an order and its shipment don't happen on the same day.
2. **Are the facts available at the same [grain](grain.md)?** Extending the example, `quantity_shipped` needs a Shipper dimension that doesn't apply to orders at all, so the facts also differ in grain.

If either test fails, the facts represent different processes and belong in separate fact tables if each is to be studied individually. This is a pairwise test, not a whole-process one — not every fact table must correspond to exactly one process; a multiple-process fact table can still be useful for *comparing* processes, but it is a derived table built on top of the single-process tables, not a replacement for them.

### Why forcing mismatched facts into one table backfires

A grain statement containing "and/or" (e.g. "shipments and/or orders by day/product/customer") is a warning sign of this mistake. Concretely:

- **Missing facts as zero or NULL rows.** When an order has no same-day shipment (or vice versa), the missing fact must be represented as 0 or NULL — but the row still appears. A report focused on just shipments then shows spurious rows for products that were ordered but never shipped, confusing users. This is a violation of a fact table's normal [sparsity](fact-table.md) (it should hold rows only for events that actually occurred). A `HAVING SUM(...) > 0` clause bolted onto every affected query is a common workaround, but it must be remembered everywhere (counts, averages, subqueries), a maintenance burden the author calls "boiling the frog" — schema design time is the chance to fix the grain instead of pushing the problem downstream into every report.
- **A generic fact-type table.** An alternative is one fact row per event, keyed by a `fact_type` dimension (e.g. "order" vs. "shipment"). This avoids the zero-row problem, but pushes the pain into reporting instead: every query must qualify on fact type, and results come back in an unpivoted, row-per-fact-type shape that needs extra formatting — worse for reports that compare the two processes.

The fix in both cases is the same: separate fact tables per process, sharing the common conformed dimensions (day, product, customer) but each storing only its own facts at its own grain, with a [role-playing dimension](role-playing-dimension.md) (e.g. separate order-date and ship-date roles for Day) linking them where needed. This pairwise grain/timing mismatch is distinct from a single fact having a merely *optional* relationship to a dimension (e.g. some orders get supervisory approval, some don't) — an optional relationship doesn't change that fact's grain and isn't a reason to split the table.
