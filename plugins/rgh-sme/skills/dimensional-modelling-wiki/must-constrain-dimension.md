---
type: concept
title: Must-Constrain Dimension
description: A dimension whose distinct values represent overlapping or redundant copies of the same underlying facts, so every query must filter it to a single value or risk double-counting.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
---

Most [dimension-table](dimension-table.md) attributes can be freely summed across without special care — summing sales across every store, or every product, gives a meaningful total. A **must-constrain dimension** is the exception: its distinct values represent overlapping or redundant views of the same underlying activity, so a query that fails to filter it down to a single value silently double- (or multi-) counts the facts.

The canonical example is a **ledger dimension** on a general ledger fact table, used to distinguish multiple sets of books tracked against the same underlying transactions (for example, a tax-reporting ledger and a regulatory-reporting ledger, or a "draft" versus "final approved" ledger). Every query against such a fact table must constrain the ledger dimension to a single value (e.g., "Final Approved Domestic Ledger") — omitting the constraint sums the same facts once per ledger value, producing an inflated total with no obvious error. The same risk arises with any dimension whose values are alternate, coexisting representations of one reality rather than a genuine partition of distinct activity (a scenario or version dimension carrying draft and final copies of the same data is another instance).

The recommended mitigation is to release separate BI-layer views to business users with the must-constrain dimension pre-filtered to the single appropriate value baked in, rather than relying on every user or report author to remember the constraint themselves.
