---
type: concept
title: Pivoted Dimension
description: A wide dimension with one flag column per value, generated from a bridge table, to make AND-combination filtering across a multivalued attribute a plain column predicate.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

A [bridge table](bridge-table.md) handles a multivalued dimension well for `GROUP BY` reporting and for filtering on a single value, but struggles with combination questions phrased as an AND across several values at once — "products purchased with option 2, option 3, *and* option 14, but *without* option 4" — because SQL has no direct way to say a bridge-table column equals several different values simultaneously across its several rows; expressing it correctly needs one `INTERSECT`/`MINUS` subquery per condition, which most ad hoc BI tools cannot generate and which performs poorly even when hand-written.

When the total population of possible values is bounded and reasonably stable — on the order of a few hundred, not tens of thousands — pivoting the bridge table's rows into columns turns every one of those combination questions back into a plain, fast column predicate. Each distinct value gets its own meaningfully named Y/N flag column (an "option 2" bridge row becomes a `memory_upgrade = 'Y'` column, for instance) on a wide dimension table generated from the bridge; a combination query is then just `WHERE memory_upgrade = 'Y' AND touch_screen = 'Y' AND extended_warranty = 'N'`, ordinary SQL any BI tool can build.

## Relationship to the bridge table it's built from

The pivoted dimension and its source [bridge table](bridge-table.md) share the same surrogate key, so they are [swappable](supertype-subtype-schema.md) — a fact table that already carries the bridge's group key needs no schema change to also support the pivoted version, and either representation can be queried depending on the question being asked. The bridge-plus-member-dimension pairing stays the better choice for `GROUP BY` and single-value filtering; the pivoted dimension is the better choice specifically for multi-value AND/NOT combination filtering. Build the bridge table first regardless — it has simpler ETL and SQL to construct and maintain — and generate the pivoted table from it, rather than building the pivoted version as the primary source of truth. A comma-separated, human-readable list of the row's active values as a single text attribute makes the pivoted dimension easier to use directly in report headers or `GROUP BY`, alongside its individual flag columns.

Pivoting isn't limited to bridge-sourced multivalued cases — the same flag-column technique is also useful for combination filtering over an attribute set that's already single-valued at true line-item grain, just with more ETL work to build since there's no bridge table already supplying the source rows.

## Limits

A pivoted dimension is capped by the target database's maximum column count (typically a few hundred to just over a thousand), and its maintenance ETL gets complex once the underlying value set is volatile — new values mean new columns, a schema change most warehouses want to avoid on a routine basis. It suits a stable population of a few hundred values well but cannot scale to a population of tens of thousands (a diagnosis code set, for example) the way a plain bridge table can. Populate only the combinations actually observed, not every theoretically possible combination — even a modest number of flag columns implies a combinatorially large space of possible rows that will vastly outgrow the fact table if built exhaustively rather than as-needed.

If the underlying attribute carries a *quantity* rather than a simple presence/absence flag (two of a given option rather than just "has it"), the flag columns become count columns instead of Y/N flags, and the source bridge table needs its own quantity column to generate them from.
