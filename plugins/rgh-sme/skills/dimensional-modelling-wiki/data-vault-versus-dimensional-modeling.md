---
type: concept
title: Data Vault versus Dimensional Modeling
description: How Data Vault's hub/link/satellite storage layer relates to and differs from dimensional modeling, and why the two are typically combined rather than competing.
sources:
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 9, 17"
  - title: "Deciphering Data Architectures"
    resource: "Deciphering Data Architectures (James Serra), ch. 8"
---

Data Vault 2.0 is a warehouse-storage methodology, not a substitute for dimensional modeling — it targets a different layer of the architecture and is typically paired *with* a [star-schema](star-schema.md) or [snowflake-schema](snowflake-schema.md) presentation layer rather than replacing one.

## What Data Vault stores, and why

Data Vault emerged to address the same extensibility pressure that motivates [atomic grain](grain.md) in dimensional design and drives [dimensional model extensibility](dimensional-model-extensibility.md) — the need to absorb new sources, new relationships, and changed business rules without redesigning existing tables — but pushed further, for large enterprises integrating many independently evolving source systems. Its core philosophy is auditability: the raw layer is strictly **insert-only**, applying no cleansing or business rules, so the warehouse can always answer "what did the source actually send us," independent of any downstream reinterpretation. This is often summarized as "Data Vault is a source of facts, not a source of truth" — since "truth" depends on which business rules are applied, but the raw facts don't change underneath them.

The raw layer decomposes into three object types:

- **Hubs** — one row per distinct **business key** (natural key) for an entity, recording only the first time each key was ever observed, from whichever source introduced it.
- **Links** — the intersection of business keys across two or more hubs, structurally identical to an many-to-many associative table *regardless of the relationship's actual cardinality*. This is deliberate: if a one-to-many relationship later needs to become many-to-many (a business rule change allowing an order to have multiple customers, say), the link absorbs it with no structural redesign — a flexibility dimensional fact tables don't have, since a [fact-table](fact-table.md)'s grain and dimensionality are meant to be declared up front and held stable.
- **Satellites** — attributes and their change history, keyed by the parent hub or link's key plus a load timestamp. A satellite is functionally a [slowly changing dimension type 2](slowly-changing-dimension-type-2.md): a new row is inserted whenever an attribute value changes, and a hash of all tracked attributes (the same "diff hash" technique used to detect type 2 changes efficiently) speeds up change detection. The difference from a Kimball type 2 dimension is architectural, not conceptual — a satellite is deliberately kept in the raw, unconformed layer rather than built as a business-facing conformed dimension.

## Relationship to dimensional modeling

Because hubs and links store only keys and satellites store only raw attribute history, none of the Raw Vault is meant for direct business-user query — it isn't conformed, isn't cleansed, and carries none of a dimensional model's business-readable structure. Star and snowflake schemas remain the standard shape for the reporting/self-service layer downstream, built from Data Vault data the same way a dimensional layer would be built from any other source: applying the [four-step dimensional design process](four-step-dimensional-design-process.md), conforming dimensions, and declaring grain. In effect, Data Vault answers "how do we store and audit data from many changing sources," while dimensional modeling answers "how do we present that data for business analysis" — the two operate at different layers and are commonly deployed together rather than chosen between.

## When the trade-off matters

Data Vault's insert-only discipline and key/link/satellite decomposition pay off most in large, multi-source environments with frequently changing relationships and a hard auditability requirement, at the cost of needing real training to execute correctly and adding an extra transformation layer between raw storage and the dimensional marts business users actually query. For a single-source or moderately-sized warehouse without that auditability or multi-source-integration pressure, going straight to a dimensional design is simpler and avoids the extra layer's ETL and modeling overhead. See also [Kimball versus Inmon architecture](kimball-vs-inmon-architecture.md) for the related trade-off between conformed-dimension-based integration and a normalized central warehouse.

Beyond the architectural trade-off, Data Vault carries real adoption cost worth weighing against its benefits: the hub/link/satellite decomposition typically produces many more physical tables than an equivalent 3NF or dimensional design, splitting what would be one entity's data across several tables and duplicating business keys into every hub, link, and satellite that references them — raising both storage and query complexity, since a query that would be a single join elsewhere may need several here. It also remains a comparatively specialized skill: it's a much newer and less standardized technique than dimensional modeling, and finding engineers already familiar with it is correspondingly harder — a real factor in a team's ability to build and maintain it without dedicated training.
