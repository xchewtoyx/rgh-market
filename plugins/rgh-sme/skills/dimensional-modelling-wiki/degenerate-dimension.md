---
type: concept
title: Degenerate Dimension
description: A dimension with no attribute content beyond its key, placed directly in the fact table with no associated dimension table.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

A degenerate dimension has no content except its primary key. The classic example is a transaction control number — an invoice number, order number, or point-of-sale transaction number — where the header-level descriptive attributes it would otherwise carry have already been extracted into other, proper dimensions (date, store, customer), leaving the control number with no unique content of its own. It is still a valid dimension key, sitting directly in the [fact-table](fact-table.md) with an explicit acknowledgment that there is no associated [dimension-table](dimension-table.md).

Degenerate dimensions are most common on [transaction fact table](transaction-fact-table.md)s and [accumulating snapshot fact table](accumulating-snapshot-fact-table.md)s. They remain useful as the grouping key for a single multi-line transaction (a "market basket") and as a potential link back to the operational system, and often participate in the fact table's composite primary key alongside the other grain-defining foreign keys.

A warning sign that a degenerate dimension has been mistakenly built out into a full dimension table: if that table's row count ends up nearly as large as the fact table itself (common when many transactions each carry mostly-unique control numbers, e.g. one bill per service line), it likely holds no real descriptive content of its own and should be collapsed back down to a degenerate dimension, with any genuinely descriptive header attributes it was carrying (transaction date, customer, and the like) moved onto the fact table as their own proper foreign keys instead.

If leftover header attributes legitimately belong nowhere else, they form a normal dimension with a normal join — at which point the key is no longer degenerate. Surrogate keys aren't typically assigned to degenerate dimensions, but see [surrogate key](surrogate-key.md) for the cases where one is still warranted (non-unique or reused control numbers, bulky alphanumeric codes, or a BI tool that needs a real dimension table to drill across on the number).

A degenerate dimension shared by two fact tables can itself become a [conformed dimension](conformed-dimensions.md), anchoring [drilling across](drilling-across.md) between them. During requirements gathering, a degenerate detail shared this way across two candidate events — created by the first, merely referenced by the later ones — is also a discovery-time signal that the events form a process sequence; see [building the bus matrix collaboratively](enterprise-data-warehouse-bus-matrix.md) for how this surfaces during modelstorming.

## Deciding what to do with each degenerate once a fact table accumulates several

Most transaction fact tables have at least one legitimate degenerate — a control number too high-cardinality and description-free to justify its own dimension table — but a design that keeps accumulating degenerates one-by-one, as each new "how" detail surfaces, needs an explicit rule for what to do with each rather than defaulting every one of them into the fact table. Sort each candidate by what it's actually used for:

- Used together for grouping, filtering, or browsing → belongs as attributes of a [junk dimension](junk-dimension.md) rather than staying loose on the fact table.
- Holds free-text or lengthy comments → replace with a foreign key to a dedicated text/comment dimension rather than storing the text directly on the fact table.
- A Y/N flag frequently *counted* (not just filtered on) → remodel it as a low-cardinality additive 0/1 fact instead of a dimensional flag, so it can be summed directly and rolled into aggregate tables.
- A high-cardinality identifier that will be counted *distinctly* → keep it as a non-additive fact on the fact table (never as a dimension); it isn't summable, but `COUNT(DISTINCT ...)` against it is exactly what it's for.
- A flag that really describes the *type* of an adjacent fact (a `revenue_type` flag distinguishing "estimated" from "actual" revenue, say) → don't keep the flag at all; split the single ambiguous fact into two clearly named facts instead (`estimated_revenue`, `actual_revenue`), so the type is expressed by which column is populated rather than by a separate flag a query must remember to check.
- A degenerate can satisfy more than one of these at once (frequently counted *and* used for grouping) — in that case, model it both ways: as a fact for counting, and as an attribute of a dimension for grouping.
