---
type: concept
title: Hot Swappable Dimension
description: A technique for pairing the same fact table with different copies of a dimension per consumer, each carrying its own proprietary attributes.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

A hot swappable dimension is used when the same [fact-table](fact-table.md) needs to be paired, at query or deployment time, with different copies of what is logically the same dimension — for example, a single stock-ticker-quote fact table exposed to multiple investors, each of whom sees a copy of the stock dimension carrying their own proprietary attributes assigned to the same underlying stocks. The fact table stays common; the specific dimension instance swapped in determines what each consumer sees. The same identical-column-names structure is reused for restricted-access row-level security, study-group or sample-population comparisons, national-language translation of the same dimension, and swapping between a current-value and historic-value view of the same [swappable dimension](supertype-subtype-schema.md).

In a relational implementation, formal referential integrity constraints between the fact table and the various per-consumer dimension tables typically must be disabled to allow this per-query swapping, since the database can't otherwise validate a foreign key relationship against several interchangeable candidate dimension tables at once.

## National-language dimension sets

A multinational deployment where users in different countries want descriptive labels in their own language is a direct application of this pattern: build one complete set of hot swappable dimensions per language — identical table names, identical column names, identical surrogate key values across every language, with only the descriptive text translated — and let each user's own login or schema context determine which language's dimension set their queries resolve against. A single report definition then runs unaltered for every language and office (an operational category labeled "Conference" in an English-language dimension set shows as "Congresso" against the Italian set, for the same underlying rows), and a new language can be added at any time by building one more parallel dimension set, with no changes needed to existing schemas or already-built reports.

Two details matter for this to work cleanly:

- **Cardinality must be preserved across every language version** — the same number of distinct members, in the same structure, or a translated report's row counts and aggregation levels stop matching the original.
- **Sort order can differ by language**, since alphabetic ordering isn't consistent across languages even for translations of the same underlying concept. Retaining an otherwise-unneeded, undisplayed business key on each language version — even after it's no longer needed for display purposes — is a simple way to give every language version a single, consistent sort order for standard reports.

Multilingual *presentation* of already-shared values — a date rendered as `MM/DD/YYYY` versus `DD-MM-YYYY`, for instance — is usually better handled through DBMS or BI-tool localization settings at the metadata layer than through separate swappable dimensions, since it changes only display formatting, not underlying content or structure.
