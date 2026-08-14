---
type: concept
title: Dimensional Model Extensibility
description: The symmetry property that lets dimensional models absorb new facts, dimensions, and attributes without altering existing queries or applications.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1-3"
---

Dimensional models are resilient to changing data relationships because every [dimension-table](dimension-table.md) is a symmetrically equal entry point into the [fact-table](fact-table.md) — there is no built-in bias toward expected query patterns. None of the following changes require altering existing BI queries, applications, or the results they return:

- **New dimension attributes** — added as new columns; backfill older rows with "Not Available" if the attribute is only available from some point forward. Tracking *historical* changes to a newly identified attribute is more involved — see [slowly changing dimension](slowly-changing-dimension.md).
- **New dimension foreign keys** — added as a new foreign-key column on the fact table, without altering the grain, populated from the new dimension's primary key. Historical rows can default to a placeholder surrogate key (e.g., "Prior to Program" or "Not Identified") using the same [null handling](null-handling-in-dimensional-models.md) pattern used elsewhere.
- **New facts** — added as new columns, provided they are consistent with the existing [grain](grain.md) (nulling older rows if only available from some point forward). Facts at a genuinely different grain belong in a separate fact table.
- **Restating a fact table at a lower grain** — making the grain more atomic by adding dimension attributes, while preserving existing column names, so existing queries and their results are unaffected.

This extensibility depends entirely on the original grain having been atomic. A dimension added years after a fact table's initial rollout can only be retrofitted onto historical rows if the grain was atomic from the start — a fact table pre-summarized above the atomic grain has no consistent place to attach the new foreign key. Premature summarization therefore creates an "analytic brick wall" for both users, who can't drill down, and developers, who can't easily extend the schema. See [grain](grain.md).
