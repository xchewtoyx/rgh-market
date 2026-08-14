---
type: concept
title: Data Lake Zone Layering
description: >
  Dividing a data lake into raw, conformed, cleansed, and presentation zones
  of increasing quality, instead of dumping every file into one flat folder.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 5"
---

A [data lake](data-lake-architecture.md) imposes
[no structure on write](schema-on-write-vs-schema-on-read.md), which
is exactly what makes it prone to becoming a data swamp without a deliberate
counter-structure. The standard fix is logically dividing the lake into
zones of increasing data quality, each with a different owner and trust
level — conceptually the lake equivalent of a warehouse's
[source/staging/presentation layering](warehouse-layering-source-staging-presentation.md),
but with one extra step a warehouse doesn't need:

- **Raw zone** (also bronze, staging, landing): events stored exactly as
  ingested, unfiltered and untransformed, usually retained indefinitely as
  the historical record of what actually arrived.
- **Conformed zone** (also base, standardized): every raw file format —
  whatever mix of CSV, JSON, and other source-native formats arrived — gets
  converted to one common format, typically Parquet. This step is specific
  to lakes: a warehouse's loader already forces a single row-and-column shape
  on write, so there's no equivalent "reconcile the file formats" step to
  perform later. Nothing about the data's content changes here, only its
  encoding.
- **Cleansed zone** (also silver, transformed, refined, enriched): raw events
  transformed into directly consumable datasets — errors corrected,
  encodings and naming conventions unified, optionally enriched with
  reference data. This is the rough lake analogue of a warehouse's staging
  layer, and the zone boundary is what gives
  [centralized cleansing logic](centralized-cleansing-logic.md) a single
  place to live rather than letting each downstream consumer re-clean the
  raw zone independently.
- **Presentation zone** (also gold, curated, serving, consumption): business
  logic applied on top of the cleansed zone to produce end-user- or
  application-ready output — aggregations, summaries, a
  [star-schema](data-warehouse-architecture.md) layout for reporting.
- **Sandbox zone** (optional; also exploration, data-science workspace): a
  modifiable copy, usually of the raw zone, that data scientists can alter
  freely without risking the zones other consumers depend on.

Other designs merge zones (conformed and cleansed combined, for instance) or
add more — this is one workable layering, not a fixed standard.

**Folder structure** should generally differ per zone and can be organized by
any of several axes depending on what the zone needs to optimize for: time of
ingestion, subject area, source system, object/table, security boundary,
downstream consumer, data type (detail vs. summary), retention policy,
business criticality, ownership, access-recency, or confidentiality
classification. The choice matters for performance, access control, and
[lifecycle management](data-retention-and-lifecycle-management.md), not just
tidiness — a flat, unstructured folder hurts all three.

**Storage tier typically follows the zone**, mapping onto
[data temperature tiering](data-temperature-tiering.md): raw and conformed
zones (rarely re-read once processed) usually sit in an archive tier;
cleansed data in a cold tier; presentation and sandbox zones, which are
actively queried, in a hot tier.

**Cross-zone auditing** — a query summing a known metric (row count, a sales
total) and comparing it against the source and against the previous zone —
should run at each zone boundary, not only at the end of the pipeline. A
mismatch at a given zone boundary localizes exactly which transformation step
introduced the discrepancy, the same way
[audit statistics tie-back](audit-statistics-tie-back.md) does for warehouse
loads.
