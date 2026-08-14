---
type: concept
title: Natural Key
description: The operational source system's business identifier for an entity, retained as a dimension attribute rather than used as the dimension's primary key.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 3"
---

A natural key (also called a business, production, or operational key) is the identifier a source system uses for an entity — an employee number, a SKU. Natural keys are typically retained as ordinary attributes on a [dimension-table](dimension-table.md), not used as the table's primary key; see [surrogate key](surrogate-key.md) for why. If a dimension is sourced from multiple systems, prepend a source code to each natural key (e.g., `SAP|43251`, `CRM|6539152`); if the same real-world entity appears in two source systems, carry two separate natural-key attributes rather than merging them. Meaningful sub-parts of a natural key (e.g., a line-of-business or country-of-origin code embedded in a multipart product code) should be split out into separate, filterable attributes alongside the whole code.

## Confirming a discovered natural key is valid

When discovering a dimension's natural key during requirements gathering, ask stakeholders directly: "What uniquely identifies each [dimension]?" / "How do you distinguish one [X] from another?" A candidate answer must then be confirmed — with stakeholders first, and later against the real data through profiling — against three criteria before it can be trusted as the dimension's natural key:

- **Mandatory** — every member always has one.
- **Unique** — no duplicates, and no reuse of a lapsed identifier for a new member.
- **Stable** — never reassigned or changed once given.

A natural key that fails stability is exactly the case that calls for a [durable key](durable-key.md) instead, below. Customer identifiers are a common source of trouble here: data pulled from multiple source systems may have no single key that is universal across all of them unless a master data management system supplies one, in which case multiple alternate natural keys may need to be modeled side by side rather than collapsed into one.

Natural keys are subject to business rules outside DW/BI control — an employee number, for instance, may change if an employee resigns and is later rehired, and organizational mergers, duplicate-entry cleanup, or multi-source integration can all cause a supposedly stable natural key to shift unexpectedly. When the warehouse needs one persistent identifier per real-world entity across such changes, and the natural key isn't guaranteed stable, a [durable key](durable-key.md) is required instead.
