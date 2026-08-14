---
type: concept
title: Splitting Wide Dimension Tables
description: Why arbitrarily halving an overly wide dimension table is a bad fix, and the real alternatives for controlling its width and change-processing load.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 6"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

A dimension table with 100+ attributes is common for a business's one or two major dimensions (often variants of product or customer). Excessive width becomes a real concern for two audiences: DBAs, for whom row length affects space allocation and block sizing, and ETL developers, for whom a table with scores of [slowly changing dimension type 2](slowly-changing-dimension-type-2.md) attributes becomes a change-detection processing bottleneck — every load must compare every tracked attribute against its prior value.

A dimension that is simultaneously deep (many millions of rows — most often a B2C customer dimension), wide (many descriptive attributes), and volatile (frequent attribute changes) is sometimes called a **monster dimension**: the combination, not any one factor alone, is what defeats ordinary dimension design and calls for the techniques below. Employee and product dimensions can run into the same problems, typically at smaller scale.

## Arbitrary splitting doesn't work

The instinctive fix — splitting the table in half by column (e.g. `customer_part1` / `customer_part2`), with both halves sharing the same surrogate key in a one-to-one relationship — reduces row length but creates new problems without solving the underlying bottleneck:

- **Multiple join paths.** Fact-to-part1, fact-to-part2, or part1-to-part2-to-fact all look superficially valid, risking inconsistent use across a team and confusing BI tools that auto-generate SQL. The correct pattern, if this were done, is the fact table joining to *each* part directly (a star join), with part1-to-part2 joined directly only when browsing "customer" as one logical entity.
- **Foreign key declaration.** An RDBMS foreign key can reference only one table, but the conceptual `customer_key` needs to reference both parts — worked around by storing two duplicate FK columns on the fact table (`customer_key_part1`, `customer_key_part2`), functionally required but inelegant since both always hold the same value.
- **No ETL relief.** ETL developers must still treat the two physical tables as one logical row and evaluate every type 2 column on every source change, regardless of which physical table the column lives in — so the change-detection bottleneck that motivated the split isn't actually solved. A side effect: a type 2 change to only one part produces two rows in the *other* part that are identical except for surrogate key.

## Real alternatives

- **Split into two genuine dimensions**, if the wide dimension is really two distinct entities collapsed together — apply the same [single vs. multiple dimension tables](single-vs-multiple-dimension-tables.md) tests: if the relationships between the two attribute groups are volatile or multi-context, they belong in separate tables with their own surrogate keys, related via the fact table (not sharing a key one-to-one the way arbitrary splitting does).
- **Relocate free-form text to an outrigger.** Large unstructured operational-carryover text fields, occasionally used to filter reports, can move to a separate table referenced by foreign key — an instance of the [outrigger dimension](outrigger-dimension.md) technique. This may impede some DBMS optimizers, but a query already constrained on free-form text is impacted by that regardless of where the text lives.
- **Look for subtypes.** When large attribute groups each apply only to a subset of rows (e.g. product attributes that differ by book vs. magazine vs. CD), build a [supertype and subtype schema](supertype-subtype-schema.md): a core dimension of shared attributes plus separate custom dimensions per subtype.
- **Move volatile attributes into a mini-dimension** — see [slowly changing dimension type 4](slowly-changing-dimension-type-4.md), which is particularly effective against both uncontrolled row growth and the type 2 change-detection bottleneck at once, since the split-off attributes stop being evaluated against the main dimension's change-detection process entirely.
