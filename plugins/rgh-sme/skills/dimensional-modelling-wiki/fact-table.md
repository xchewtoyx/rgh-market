---
type: concept
title: Fact Table
description: The central table in a star schema storing quantitative measurements and foreign keys to dimensions.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1-3"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 3"
---

In a [star-schema](star-schema.md), a fact table is the central event table that records quantitative measurements or metrics of a [business process](business-process.md).

Characteristics of a fact table:
*   **Structure:** Typically contains a set of foreign keys referencing surrounding [dimension-table](dimension-table.md)s, alongside numeric measurement columns (e.g., price, quantity, duration), plus optional [degenerate dimension](degenerate-dimension.md) keys and date/time stamps.
*   **Dimensions:** Attributes are often wide (potentially 100+ columns), representing a complex set of foreign keys. Most business processes can be represented with fewer than 20 dimensions; a much larger number usually signals correlated dimensions that should be combined — see [centipede fact table](centipede-fact-table.md).
*   **Volume:** Contains the vast majority of the data in the schema — typically 90%+ of total space — often scaling to billions or trillions of rows of historical events. Fact tables are deep (many rows) but narrow (few columns), and should not be padded with rows for non-events; only true activity is recorded. This property is called **sparsity**: a fact table holds only rows for combinations of dimension values where a measurement event actually occurred, not one row for every theoretically possible combination — a fully dense fact table would explode in size. (Denser fact tables built by design exist too — see [periodic snapshot fact table](periodic-snapshot-fact-table.md).)

Each row in a fact table represents a specific measurement event at a defined [grain](grain.md), providing the raw measurements that are aggregated in analytical queries. "The idea that a measurement event in the physical world has a one-to-one relationship to a single row in the corresponding fact table" is a bedrock principle of dimensional modeling — the table corresponds to a physical observable event, not to a report's demands. See [grain](grain.md) for how this constrains which dimensions and facts belong on a given fact table.

## Keys and referential integrity

A fact table has two or more foreign keys referencing dimension tables' primary keys; when every fact table key correctly matches a dimension primary key, the tables satisfy referential integrity. The fact table's own primary key is usually a composite key made of a subset of its foreign keys — as a rule of thumb, "every table that has a composite key is a fact table; all others are dimension tables." A fact table thereby expresses a many-to-many relationship between its dimensions; dimensions not part of the grain-defining subset still take a single value in the context of the row's key — they "go along for the ride." Null values are never permitted in fact table foreign keys, since this would violate referential integrity; instead the referenced dimension table carries a default row representing "unknown" or "not applicable." See [null handling in dimensional models](null-handling-in-dimensional-models.md).

## Fact vs. dimension attribute

Whether a column belongs in the fact table or in a dimension comes down to one test: is it a measurement that takes on many values and participates in calculations (a fact), or a discretely valued, more-or-less-constant description that participates in constraints and labels (a dimension attribute)? Continuously valued numeric observations are almost always facts; discrete numeric observations drawn from a small list are almost always dimension attributes. True textual facts are rare (e.g., freeform comments — see [text comments dimension](text-comments-dimension.md)) and hard to analyze; descriptive text drawn from a discrete list belongs in a dimension, not the fact table. Some ambiguous numeric values (e.g., a product's standard list price) are used mainly for calculation in some contexts and mainly for filtering/grouping in others — see [numeric value as fact or dimension attribute](numeric-value-as-fact-or-attribute.md) for how this is resolved, including storing the value in both places when justified.

## Facts by additivity

Facts are classified by how they behave under aggregation: [additive fact](additive-fact.md)s can be summed across any dimension, [semi-additive fact](semi-additive-fact.md)s can be summed across some dimensions but not others (typically not across time), and [non-additive fact](non-additive-fact.md)s cannot be summed at all.

## Fact table types

Every fact table grain falls into one of three categories: [transaction fact table](transaction-fact-table.md), [periodic snapshot fact table](periodic-snapshot-fact-table.md), or [accumulating snapshot fact table](accumulating-snapshot-fact-table.md).
