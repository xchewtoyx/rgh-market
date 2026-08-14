---
type: concept
title: Snowflake Schema
description: A variation of the star schema where dimension tables are normalized into multiple related tables.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 3"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 7"
---

The snowflake schema is a variant of the [star-schema](star-schema.md) where [dimension-table](dimension-table.md)s are further normalized into sub-tables. This normalization is called **snowflaking**.

For example, instead of storing a flat list of brands and categories directly within a product dimension table, a snowflake schema splits them into separate tables:
$$\text{product} \rightarrow \text{brand} \rightarrow \text{category}$$

When visualized, the normalized dimensions branch out from the central [fact-table](fact-table.md), resembling a snowflake.

### Trade-offs
*   **Storage Efficiency:** Normalization reduces data redundancy and saves storage space, but the saving is typically trivial — replacing a 20-byte department description repeated thousands of times in a 300,000-row product dimension with a 2-byte code plus a lookup table might save only a few megabytes against a fact table that could be many gigabytes; dimension tables are geometrically smaller than fact tables regardless of internal normalization, so the space argument for snowflaking rarely holds up.
*   **Query Complexity:** Because attributes are scattered across multiple tables, analytical queries require additional joins, and most optimizers handle the added complexity worse — more joins generally mean slower queries and a higher chance the optimizer picks a poor plan.
*   **Browsing:** Snowflaking hurts the ability to constrain on one or more attributes and see the distinct values of another. A single-table lookup (e.g., a list of category descriptions) still works fine, but cross-hierarchy questions (brands within a category; package types per brand within a category) require traversing multiple normalized tables, producing complex SQL even before the rest of the schema is touched.
*   **Bitmap indexes:** Snowflaking defeats bitmap indexes, which are effective on low-cardinality dimension columns (like category or department) but require those columns to live directly in the dimension table rather than in a separate normalized lookup table.
*   **Usability:** In data warehousing and Online Analytical Processing ([OLTP vs. OLAP](oltp-vs-olap.md)), star schemas are generally preferred over snowflake schemas because they present a simpler, easier-to-understand model to analysts and optimize query engine scan performance. Fixed-depth hierarchies should be flattened in dimension tables — see [fixed-depth hierarchy](fixed-depth-hierarchy.md).

### When snowflaking is acceptable

Two categories of exception are recognized:

1. **Technology-driven.** Some BI tools or RDBMS products function better with, or outright require, a snowflaked design — for example a BI tool that needs a snowflake to support aggregates or to automate [drilling across](drilling-across.md). Refusing to snowflake in these cases is counterproductive, but it's a strategic decision, not a purely technical one: tuning the model to one product's requirements limits future flexibility, since switching database or BI tools later means inheriting snowflake infrastructure that may no longer be needed.
2. **Modeling challenges a pure star can't meet.** When a fact attribute takes on more than one instance value at once (e.g. an order with several collaborating salespeople), the standard one-to-many dimension-to-fact relationship breaks down — resolved with a [bridge table](bridge-table.md), itself a limited, deliberate form of snowflaking. Recursive [instance hierarchies](ragged-hierarchy.md) among a dimension's own rows (companies owning companies, employees reporting to employees) present a similar problem, resolved with a [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md). Repeating attribute groups within one dimension table are the third case — resolved with an [outrigger dimension](outrigger-dimension.md), used sparingly and only when justified by a genuine secondary filtering or ETL-consistency need.

### Why normalization doesn't transfer from OLTP

Snowflaking is the analytic-schema analog of **normalization**, the entity-relationship technique for operational ([OLTP](oltp-vs-olap.md)) systems — but the reasoning behind normalization doesn't carry over. Normalization matters operationally because an OLTP system handles simultaneous insert/update/delete/query transactions on individual records and must satisfy ACID properties with minimal performance impact: confining an update (e.g. a brand name change) to a single row means minimal rollback resource use and no need to lock unrelated rows (every product sharing that brand) during the update. Saved storage space is only an incidental side effect of normalization, not its purpose. An analytic database is instead dominated by large-scale queries, not atomic multi-user transactions, and its inserts/updates/deletes come from a single controlled ETL process that can guarantee integrity on its own — so normalization's concurrency guarantees are simply unnecessary there, leaving only its costs (more joins, worse browsability, more ETL surface area to maintain) with none of its benefit.

For the same reason, avoid describing a star schema as "denormalized" and a snowflake as "normalized" — both are imprecise, since there are multiple normal forms (1NF, 2NF, 3NF, ...) and a star's dimension tables typically were never normalized to begin with (so "not normalized" is the more accurate description), while a snowflaked dimension frequently still falls short of 3NF itself (e.g. address fields left denormalized within a customer-level table).
