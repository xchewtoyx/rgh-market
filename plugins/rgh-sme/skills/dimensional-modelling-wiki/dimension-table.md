---
type: concept
title: Dimension Table
description: A table in a star schema that contains descriptive attributes representing the context of a business event.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

In a [star-schema](star-schema.md), dimension tables surround the central [fact-table](fact-table.md) and represent the context (the [7Ws](seven-ws-framework.md) "who, what, where, when, why, and how") of a business event.

Characteristics of a dimension table:
*   **Structure:** Contains descriptive, textual, or categorical attributes (e.g., product name, store location, date/time attributes). Dimension tables often have many columns — 50-100 attributes is not uncommon, though some have only a handful — and tend to have far fewer rows than fact tables even when individual rows are wide.
*   **Usage:** These attributes are primarily used to filter (via `WHERE` clauses), group (via `GROUP BY` clauses), and label reports in analytical queries — they are the "by" words in a business request (e.g., "dollar sales by brand" requires brand as a dimension attribute). Attributes should be real words rather than cryptic operational codes; the analytic power of a DW/BI environment is directly proportional to the quality and depth of its dimension attributes. Because dimension tables are geometrically smaller than fact tables, conserving dimension space by limiting verbose descriptors is a false economy — supply maximum descriptive context.
*   **Flags and indicators:** cryptic abbreviations, true/false flags, and operational indicators should be supplemented with, or replaced by, full text words meaningful in isolation (e.g., "Holiday"/"Non-holiday" rather than a bare Y/N) — decoded once in the dimension table so every BI tool and user sees the same consistent, self-explanatory label rather than each application decoding the flag independently. Operational codes with embedded meaning (e.g., a multipart product code) should be decomposed into separate descriptive attributes per code segment, in addition to being preserved whole.
*   **Denormalization:** Dimension tables are typically denormalized to avoid joins, prioritizing query speed and ease of use over storage efficiency. If normalized, the schema becomes a [snowflake-schema](snowflake-schema.md); the space saved by normalizing a dimension table is typically under 1% of total schema disk space, since fact tables dominate overall size — see [surrogate key](surrogate-key.md) for the related discussion of resisting normalization urges more broadly.
*   **Hierarchies:** Dimension tables typically represent many-to-one hierarchies (e.g., product rolls up to brand to category) as separate flattened, positional attributes on the same row rather than as separate normalized lookup tables. See [fixed-depth hierarchy](fixed-depth-hierarchy.md).

Every dimension table has a single primary key column — see [surrogate key](surrogate-key.md) — embedded as a foreign key in any fact table where that dimension row's descriptive context is exactly correct at the fact table's [grain](grain.md).

A dimension table can also be queried on its own, independent of any fact table — see [browse query](browse-query.md).

A candidate attribute earns its place on a dimension only if it passes the [dimension attribute belonging test](dimension-attribute-belonging-test.md) — single-valued for the dimension's subject at a moment in time.

## Smart keys should be decoded once, at load, not at query time

Operational business keys and other cryptic codes sometimes carry hidden, decodable meaning ("smart keys" — e.g., a customer ID whose digit pattern encodes business-vs-consumer type). Existing reports or spreadsheets that already decode such codes into readable labels are the signal to convert that decode logic into ETL-built descriptive attributes on the dimension, rather than leaving BI applications to decode the code independently at query time — smart keys rarely stay smart as operational processes evolve, and become overloaded with meaning the original design never anticipated. Once genuine descriptive attributes exist, the cryptic code itself can often be hidden or dropped from reporting, unless a consistent sort order across languages still depends on it.

## Handling change

Dimension attributes are relatively static but not fixed forever. How a dimension table responds when an attribute's real-world value changes is governed by [slowly changing dimension](slowly-changing-dimension.md) techniques.
