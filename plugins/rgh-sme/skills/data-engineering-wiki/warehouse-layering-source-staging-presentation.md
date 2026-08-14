---
type: concept
title: Warehouse Layering (Source, Staging, Presentation)
description: >
  Splitting a warehouse into a raw source layer, a working staging layer, and
  governed presentation layers, each with a different owner and a different
  trust level.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 10"
---

A warehouse benefits from deliberate schema layering rather than one
undifferentiated pile of tables, with each layer serving a distinct purpose
and audience:

- **Source (raw) layer**: holds data loaded unaltered from source systems —
  no renaming, no transformation. Keeping this layer untouched means a
  change to downstream transformation logic never requires re-extracting
  from the source. Access should generally be restricted to the engineering
  team, since unconformed raw data is hard for business users to interpret
  correctly. This is the natural place to attach standardized load metadata
  to every table — a load identifier (so a bad load's rows can be found and
  removed), the load date/time (which can differ from the source's own
  extract timestamp), the source filename, which tool performed the load,
  and the load type — giving every downstream problem a starting point for
  tracing back to exactly which load introduced it. This is the concrete
  mechanism behind [pipeline metadata categories](pipeline-metadata-categories.md)'
  operational metadata and [data lineage](data-lineage.md) at the point data
  first enters the warehouse.
- **Staging layer**: a temporary working schema holding transformed source
  data en route further downstream, off-limits to end users and reporting
  tools. A dedicated staging schema cleanly separates provisional data from
  trusted data and lets schema-level defaults (shorter retention, a
  [transient table type](data-retention-and-lifecycle-management.md)) apply
  uniformly instead of per-table.
- **Presentation layers**: governed schemas built for actual consumption,
  which can take either or both of two shapes. A **normalized, conformed**
  layer serves business users literate enough to write their own joins
  without hand-holding — [conformed dimensions](data-mesh.md) here means
  keeping column names and meaning identical for the same concept across
  every table it appears in, so an ID column doesn't drift into a
  differently-named field by the time it reaches reporting. A
  **denormalized reporting** layer instead serves plug-and-play consumption
  of curated metrics in single wide tables, appropriate even for literate
  users when an analysis is too complex or too consequential to leave to
  ad-hoc self-service — this is where a
  [semantic/metrics layer](semantic-metrics-layer.md)'s governed definitions
  actually get materialized.

The layering matters because trust and access control naturally differ by
layer: raw data is unvalidated and engineering-only, staging is provisional
and consumer-off-limits, and presentation layers are where governance
(consistent business-rule definitions, documented ownership) is worth the
investment because many people will actually query them directly.
