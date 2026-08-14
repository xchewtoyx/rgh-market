---
type: concept
title: Bypassing the Lake for Clean Relational Sources
description: >
  Loading already-structured source data straight into the warehouse instead
  of staging it through the lake first, and what that trade-off gives up.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 10"
---

In a [modern data warehouse](modern-data-warehouse-architecture.md), not
every source has to pass through the lake before reaching the RDW. For
already-structured, already-clean relational source data — reference or
dimension tables that need no cleaning, are pulled as
[full extracts](incremental-vs-full-extraction.md), and are cheap to
re-retrieve from source if a pipeline run fails — copying straight into the
RDW and skipping the lake entirely is often faster to build and simpler to
operate. Routing this kind of source through the lake first can even lose
information: a relational source's data types, constraints, and foreign keys
don't survive being staged as lake files and have to be re-inferred on
import into the RDW anyway.

This bypass is especially common in on-premises-to-cloud migrations that
already have many existing ETL packages copying relational-database source
data straight into an RDW: the minimal-effort migration path is to just
repoint each package's destination at the new cloud RDW, and migrate packages
to route through the lake gradually over time — typically starting with
whichever packages currently run slowest, since those benefit most from the
lake's cheaper, more elastic compute.

The trade-off is real, not free: skipping the lake gives up the lake's
implicit backup copy (useful if an ETL package needs to be rerun against the
same input later), puts more cleansing and transformation load directly on
the RDW instead of offloading it to the lake's compute, and creates a gap in
the lake's status as a single source of truth — some data now exists only in
the RDW, which downstream consumers who assumed "the lake has everything"
will not find there. The right default is still source-type-dependent:
messy, high-volume, or semi-structured data benefits from the lake's
schema-on-read absorption; clean, already-relational, low-volume reference
data often doesn't need it.
