---
type: concept
title: Fixed Depth Positional Hierarchy
description: A many-to-one hierarchy with a consistent number of agreed-upon levels, modeled as separate flattened attributes on a single dimension row.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3, 7"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 7"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

A fixed-depth (positional) hierarchy is a series of many-to-one relationships with a consistent number of levels, all with agreed-upon names — product → brand → category → department, or day → month → year. It should appear as separate positional attributes directly on the [dimension-table](dimension-table.md) row at the hierarchy's lowest grain, denormalized rather than split into separate lookup tables per level (that alternative is [snowflaking](snowflake-schema.md), which the fixed-depth technique exists to avoid). This is the easiest hierarchy shape to understand and navigate, and is predictable and fast to query.

Many dimensions contain more than one natural hierarchy at once, and multiple hierarchies coexist cleanly as parallel attribute sets on the same dimension row — for example, a [date dimension](date-dimension.md) simultaneously supporting day → week → fiscal period and day → month → year, useful when fiscal periods and calendar months don't line up simply, or a store dimension carrying both a geographic hierarchy (ZIP → county → state) and an internal organizational hierarchy (district → region). Attribute names and values must stay unique across the multiple hierarchies sharing one dimension table.

Watch for attributes that look hierarchical but aren't: within the US, city and state do not form a hierarchy on their own, because many states share identically named cities. A geographic dimension needs a combined city-state attribute (or an equivalent composite) as the actual hierarchy level, not city and state modeled as if state alone determined a unique parent for each city.

**Warning**: avoid fixed-position hierarchies with abstract level names ("Level-1," "Level-2," ...) as a way to dodge properly modeling a [ragged hierarchy](ragged-hierarchy.md). Abstract names give business users no way to know where to constrain or what a level's values mean in a report — if a ragged hierarchy is hiding behind abstractly labeled fixed levels, those levels are effectively meaningless.

When a hierarchy isn't consistently many-to-one, or its levels lack agreed-upon names across all instances, it isn't a good fit for a fixed-depth positional design — use a [ragged hierarchy](ragged-hierarchy.md) technique instead.

**Multi-parent variant**: a child value that legitimately rolls up to more than one parent at the same level (a product belonging to more than one product type, for example) breaks the strict many-to-one assumption a fixed positional attribute depends on, and needs careful revenue/measure allocation to avoid double-counting whenever facts are rolled up to the parent level — see the [bridge table](bridge-table.md)'s weighting-factor technique for how that allocation is done. A multi-parent relationship can also be ragged or variable-depth at the same time as being multi-parent.

Levels are discovered and positioned using a [hierarchy chart](hierarchy-chart.md) and its paired cardinality questions.

**Anti-pattern: mixing atomic and rollup rows in one dimension table.** A dimension table should not hold both atomic-level rows and higher hierarchy-level rows together, distinguished by a "level" attribute (for example, individual product rows mixed with brand-level summary rows in the same product dimension). This confuses users, who can't tell at a glance which rows are real entities versus rollups, and risks silent overcounting whenever a query fails to constrain on the level indicator, since a sum would then double-count a brand's rollup row alongside the very product rows it already summarizes. Use a genuine [shrunken dimension](shrunken-dimension.md) — a separate table at the rolled-up grain, paired with its own [aggregate fact table](aggregate-fact-table.md) — instead of blending grains within one dimension table.

## Attribute hierarchy vocabulary

This kind of hierarchy — successive many-to-one, or master-detail, relationships among a dimension's *attributes* — is also called an **attribute hierarchy**, to distinguish it from an **instance hierarchy** (a recursive relationship among the *rows* of a single dimension, such as an employee reporting to another employee — see [ragged hierarchy](ragged-hierarchy.md)). An attribute hierarchy is conventionally diagrammed top-to-bottom, most-summarized to most-detailed, often with a conventional top level such as "All Products" added purely for convenience, representing complete summarization (querying by it yields one row) and carrying no attributes of its own. When documenting cardinality per level, don't assume an even distribution across parents — real hierarchies are commonly skewed, with some parents (e.g. one product category) holding disproportionately more children than others.

A hierarchy diagram like this does double duty beyond drilling: the relationship between a base dimension and one of its [shrunken dimension](shrunken-dimension.md) rollups is itself an attribute hierarchy relationship, so the diagram can surface candidate rollups directly; and the hierarchy gives a compact shorthand for describing an [olap-cube](olap-cube.md)'s or [aggregate fact table](aggregate-fact-table.md)'s summarization level per dimension (e.g. "order dollars at the brand and quarter levels"), with a horizontal cut-line across several stacked hierarchy diagrams depicting a cube's overall grain. This is only a shorthand, though — any attribute can serve as a valid rollup or drill target regardless of its position in the nominal hierarchy (e.g. a low-cardinality attribute like product color sits at the hierarchy's most-detailed level but summarizes heavily on its own), so a hierarchy diagram documents *some*, not *all*, of the valid ways to roll up or drill into a dimension.
