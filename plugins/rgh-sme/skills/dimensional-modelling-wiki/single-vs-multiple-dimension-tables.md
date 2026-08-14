---
type: concept
title: Single vs. Multiple Dimension Tables
description: Decision framework for whether two closely related entities (e.g. customer and sales rep) should be combined into one dimension or kept as separate dimensions.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 6"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 6"
---

Two entities that are closely related but conceptually distinct (a customer and its assigned sales rep, a ship-to and its bill-to location) can be modeled either as a single combined [dimension-table](dimension-table.md) or as two separate dimensions joined only through the [fact-table](fact-table.md). Combining is viable, and often convenient, when the relationship is fixed, time-invariant, and strongly correlated — a one-to-one or many-to-one relationship lets the combined dimension end up no larger than the bigger of the two, and lets the relationship be browsed directly without touching the fact table.

## Why: explicit versus implicit relationships

Unlike an entity-relationship model, a dimensional model doesn't expose every relationship between attributes as a join — this underlies the decision above. Two attributes relate either:

- **Explicitly**, via a join that intersects in a [fact-table](fact-table.md), which supplies the specific context for the relationship (every fact table is, in ER terms, an intersect table resolving a many-to-many relationship). Explicit relationships can be numerous and volatile, and the same pair of dimensions can be related in several different contexts through different fact tables — this is exactly the multi-context case that favors separate dimensions, below.
- **Implicitly**, by simply co-locating both attributes in the same dimension table (e.g. product and brand). This implies a natural affinity rather than a relationship tied to any particular context, tends to be more stable, and is directly browsable without a fact table in the middle; when an implicit relationship does change, history can still be preserved via a [type 2](slowly-changing-dimension-type-2.md) change.

**The browsability test**, useful whenever the choice is unclear: would users want to browse the values of the two attributes together, independent of any transaction? Splitting product and brand into separate tables (each with its own surrogate key, joined only via the fact table) would destroy this — a product with no orders yet would have no discoverable brand, since the two could then only be studied together in the context of an order. Even when a business does formally assign salespeople to customers, merging those two attributes is usually still wrong, because salespeople and customers engage in other multi-context activities too (calls, visits, proposals, returns) — if only the assignment relationship itself needs tracking, a [factless fact table](factless-fact-table.md) is the appropriate tool, not a merged dimension.

Factors favoring **separate** dimensions instead:

- The relationship is genuinely many-to-many as the norm, not just a rare exception.
- The relationship varies over time, or is influenced by another dimension.
- One of the two dimensions is extremely large (millions of rows) — don't force all analysis of the smaller entity through a huge combined table.
- The two entities participate independently in other fact tables (a merged dimension can't be reused cleanly there).
- The business genuinely thinks of them as separate things — hard to quantify, but shouldn't be overridden by a design that merges them anyway.

A small correlation table holding just the two keys is usually unnecessary: the fact table itself already represents the correlation between dimensions and is efficient at it, since it holds only keys, measures, and occasional [degenerate dimension](degenerate-dimension.md)s. This decision is weighed against the general guideline of not accumulating too many dimensions on one fact table — if a schema already carries around 25 dimensions, look for opportunities to combine rather than add more.

## Handling a relationship that isn't cleanly many-to-one

When the two entities are *usually* many-to-one but have occasional exceptions (e.g. a ship-to location that is normally billed to one place, but is sometimes billed to two), two options preserve the same information without losing data:

- If exceptions are rare, generalize the combined dimension's grain to unique combinations of the two entities — accepting, for example, two rows for one ship-to location that has two bill-tos.
- If the many-to-many relationship is common rather than a rare exception, split the two entities into separate dimensions, linked only through the fact table.
