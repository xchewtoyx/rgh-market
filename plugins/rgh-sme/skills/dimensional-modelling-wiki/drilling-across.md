---
type: concept
title: Drilling Across
description: Combining results from two or more fact tables by running separate queries and aligning their answer sets on shared conformed dimension attributes.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 4"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 4"
---

Drilling across makes separate queries against two or more [fact-table](fact-table.md)s, each using identical [conformed dimensions](conformed-dimensions.md) attributes as row headers, then aligns the answer sets via a sort-merge (typically a full outer join) on those common attributes so rows appear even if present in only one result set. BI vendors call this technique "stitch," "multipass," or "multi-fact" querying; implementations differ in where the join actually happens (temp tables, application server, or the report itself). Cross-fact calculations (e.g., actual vs. forecast variance) generally must happen in the BI application after the separate conformed results return. The term is unrelated to a BI tool's drill-up/drill-down/drill-through features ([see drilling down](drilling-down.md)) — it describes crossing from one star to another, not moving between levels of one hierarchy.

Drilling across is only valid because the dimensions being aligned are conformed — if the row-header attributes aren't identically labeled, defined, and valued across the source fact tables, the sort-merge silently produces meaningless results. Conformance must hold both in *structure* (the attribute exists, identically named, in each star) and in *content* (the same values are represented the same way in each — e.g. both sources spell periods "Q1"–"Q4," not "Q1" in one and "First Quarter" in the other). This is why conforming dimensions is treated as the essential integration mechanism for an enterprise DW/BI environment.

A BI application must never join two fact tables directly on their foreign keys, or indirectly through a shared dimension — the cardinality of the resulting answer set is uncontrollable in a relational database and produces incorrect results in two distinct ways at once: a dimension row acts as "parent" to many fact rows ("children") in each fact table, and joining fact-table "siblings" that share a parent produces a Cartesian product between them (a product with 1 matching order row and 2 matching shipment rows gets its order double-counted, paired against each shipment in turn), while simultaneously *losing* rows that have no sibling on the other side (a product that was ordered but never shipped disappears entirely, since there's no shipment row to join against). Substituting outer joins on the dimension tables does not fix this — the query is still joined within the fact-to-fact relationship itself. Drilling across via separate, sort-merged queries is the correct alternative to such a fact-to-fact join.

This failure mode is also known as the **fan trap** or **chasm trap**: it arises specifically whenever the tables being joined have a many-to-many (or one-to-many, on the "many" side) relationship between them. It is dangerous precisely because it's invisible in a query's row-level output — a BI query's own `GROUP BY`/aggregation step hides the inflated row count that caused the wrong total, since SQL evaluates joins (the `WHERE`/`FROM` clause) before it evaluates `GROUP BY`: two fact tables sharing an employee, one with 3 matching salary rows and the other with 2 matching absence rows for that employee, join into 6 combined rows before any summing happens, silently doubling or tripling both totals once they're aggregated. The only fact-to-fact join that's actually safe is a strict 1:1 relationship — rare, hard to guarantee holds for every row, and still liable to perform poorly at scale even when it does hold.

## The two-phase procedure

1. **Phase 1** — query each fact table *separately*, applying the same filters/constraints to each, and aggregating each result to a common (identical) level of dimensional detail, so each intermediate result set has at most one row per distinct combination of the shared dimension values.
2. **Phase 2** — merge the intermediate result sets with a full outer join on the common dimension attributes, computing any cross-process ratios or comparisons at this stage.

This generalizes to any number *n* of fact tables: run *n* Phase-1 queries at the same shared grain, then combine the *n* result sets pairwise in any order (order doesn't matter, since they all share grain). It works across separate database instances and even across RDBMS vendors, given conformance as described above. Drilling across can even be applied to a single star — e.g. a "this year vs. last year" comparison built from two queries against the same fact table, merged on a shared dimension like region. See [drill-across implementation approaches](drill-across-implementation-approaches.md) for how the two phases get realized physically, and what to do when a BI tool can't drill across at all.

Powerful cross-process metrics that only exist via drilling across (e.g. "yield" = orders ÷ sales calls) don't correspond to a column anywhere, or even to a single table — they're easy to lose track of in design documentation, so designers should document them explicitly at design time rather than leaving them as tribal knowledge.

Related: [consolidated fact tables](consolidated-fact-table.md) combine facts from multiple processes into one physical table at a shared grain, trading extra ETL effort for eliminating the need to drill across at query time for that specific combination.
