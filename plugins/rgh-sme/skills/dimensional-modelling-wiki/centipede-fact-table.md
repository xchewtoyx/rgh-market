---
type: concept
title: Centipede Fact Table
description: An anti-pattern where a fact table carries a separate foreign key for each level of a many-to-one hierarchy instead of one key to a denormalized dimension.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3"
---

A centipede fact table occurs when designers create separate, normalized dimensions for each level of a many-to-one hierarchy — date, month, quarter, and year dimensions, for instance, instead of one date dimension — and include all of them as [fact-table](fact-table.md) foreign keys, or embed numerous foreign keys to individual low-cardinality dimensions instead of combining them into a [junk dimension](junk-dimension.md). The result (affectionately named for its near-100 "legs") should be avoided.

This is the fact-table-side symptom of the same underlying discomfort that produces [snowflaking](snowflake-schema.md) on the dimension side: a modeler uncomfortable with denormalized dimension tables, but aware that snowflaking is discouraged, instead pushes the normalized hierarchy levels directly onto the fact table as separate keys. The fact table itself is already naturally highly normalized and compact — its dimensions aren't correlated with each other, so there's no way to further normalize its many-to-many key relationships — so adding centipede legs only makes things worse:

- It significantly increases fact table disk space, which matters far more here than at the dimension level, since the fact table is already the largest table by orders of magnitude.
- There is no effective way to index the resulting enormous multipart key.
- The numerous joins hurt both usability and query performance.

The fix is to collapse fixed-depth, hierarchically related dimensions back to their unique lowest grain, as a single denormalized dimension — see [fixed-depth hierarchy](fixed-depth-hierarchy.md). Most business processes can be represented with fewer than 20 dimensions in the fact table; 25 or more signals correlated dimensions that should be combined. The rule of thumb for combining: do it when the resulting single dimension is noticeably smaller than the Cartesian product of the separate dimensions — i.e., when the attributes are correlated, as hierarchy levels inherently are. Columnar databases tolerate wide centipede designs better than row-oriented ones, though cross-hierarchy browsing ability may still be compromised.

The opposite failure — a design with suspiciously few dimensions, from collapsing everything into one catch-all dimension or simply omitting dimensions — is just as much a problem; see the [dimension triage checklist](dimension-triage-checklist.md) for commonly overlooked dimension types to check for.
