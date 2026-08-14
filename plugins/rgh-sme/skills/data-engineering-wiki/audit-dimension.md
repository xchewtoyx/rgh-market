---
type: concept
title: Audit Dimension
description: >
  Attaching the metadata context present at load time — as a real dimension
  row on the fact itself — so a fact's provenance and quality confidence
  travel with it rather than living only in separate operational logs.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

An audit dimension is assembled by the load process for each fact table, and
holds the metadata context present at the moment a specific fact row was
created — effectively promoting load metadata to real, queryable data instead
of leaving it in a load log nobody joins against. In the common case of a
clean, uneventful daily load, every fact row loaded that day shares a single
audit dimension row. When some rows trigger a [quality screen](quality-screens.md)
tag-and-pass-through response — say, a discount-dollars value flagged as
out-of-bounds — the load generates an additional audit dimension row so those
specific facts can be distinguished from the clean majority via a normal
dimension join, rather than requiring a separate lookup into an error log.

This is the fact-table counterpart to the load metadata that the [raw source
layer](warehouse-layering-source-staging-presentation.md) attaches at
ingestion (load ID, load timestamp, source filename): where that metadata
describes the load batch, an audit dimension describes the quality state of
an individual fact row within it, queryable with an ordinary join instead of
a side lookup.

**Route it through a foreign key, never inline columns on the fact row
itself.** Fact tables accumulate rows far faster than dimension tables, so
adding per-row creation/update metadata (process name, execution timestamp,
records-processed counts) directly as fact columns multiplies that overhead
across every single row. A dedicated audit/load-info dimension holding that
metadata once per load, referenced from fact rows via a single foreign key,
keeps the cost at one row per load instead of one copy per fact row — and if
a fact row's provenance is later corrected, only its foreign key needs to
change, not a set of inline columns.

**Resist generalizing this into a full change-log system.** A bitmap column
tracking exactly which fields changed on a given row, or a comprehensive
audit log of every historical value a row ever held, is tempting but adds
real ongoing ETL burden for a benefit that's usually marginal — most of what
it would capture is already sitting in the pipeline tool's own execution
logs. Keep the audit dimension scoped to what ETL support, QA reconciliation,
and data forensics actually need, not to "what could conceivably be useful
to know later."
