---
type: concept
title: Dimension Triage Checklist
description: A checklist of commonly overlooked dimension types to review when a fact table's dimension count looks suspiciously thin.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 10"
---

Most dimensional models end up with somewhere between 5 and 20 dimensions on a [fact-table](fact-table.md). A design that lands at or below the low end of that range should raise suspicion that dimensions were inadvertently collapsed into a single catch-all dimension or simply omitted — the mirror-image failure mode to the [centipede fact table](centipede-fact-table.md), which results from having too many. When a design looks too thin, check it against these commonly overlooked candidates:

- **[Causal dimension](causal-dimension.md)s** — promotion, contract, deal, store condition, weather — anything believed to cause a change in the measured outcome.
- **Multiple [date dimension](date-dimension.md)s** via [role-playing dimension](role-playing-dimension.md)s, especially on an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md) with several milestone dates.
- **[Degenerate dimension](degenerate-dimension.md)s** identifying operational control numbers — order, invoice, bill of lading, ticket.
- **Role-playing dimensions** more generally, wherever a single transaction has several associated instances of the same business entity, each needing its own foreign key.
- **Status dimensions** identifying the current status of a transaction or snapshot row (e.g., account status) within a larger context, rather than embedding a cryptic status code directly in the fact table or overloading a larger dimension with it.
- **[Audit dimension](audit-dimension.md)** for data lineage and quality metadata.
- **[Junk dimension](junk-dimension.md)s** of correlated low-cardinality indicators and flags — these can typically be added gracefully even after a schema is already in production, since adding one doesn't change the fact table's grain, doesn't alter any existing dimension key or measured fact, and leaves existing applications running unchanged.

The general test behind all of these: any descriptive attribute that takes a single value in the presence of the fact table's measurements is a good candidate to become its own dimension, or to be added to an existing one — it should not be left stranded as an unmodeled attribute buried inside a larger, unrelated dimension.
