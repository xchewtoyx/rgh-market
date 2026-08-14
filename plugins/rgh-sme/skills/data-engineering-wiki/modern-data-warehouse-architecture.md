---
type: concept
title: Modern Data Warehouse Architecture (Lake + RDW)
description: >
  Blending a data lake with a relational data warehouse via mandatory
  replication between them, and the five-stage journey data takes through it.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 10"
---

A modern data warehouse (MDW) combines a [data lake](data-lake-architecture.md)
with a [relational data warehouse](data-warehouse-architecture.md), each
covering what the other is weak at: the lake's schema-on-read ingestion
absorbs any data type/velocity cheaply and supports ML training directly off
raw or lightly cleaned data, while the RDW's schema-on-write structure gives
business users fast, secure, self-service reporting the lake alone can't
match. The defining, distinguishing feature is that **at least some data must
physically replicate from the lake into the RDW** — without that duplication
step the architecture is [a lakehouse](data-lakehouse.md) instead, which adds
warehouse-style controls on top of one storage layer rather than
duplicating data across two.

**The five-stage journey**: ingestion (any source type/cadence lands in the
lake), storage (into the lake's
[quality zones](data-lake-zone-layering.md)), transformation (raw formats
converted to one common format, then cleaned, then joined/aggregated for the
presentation zone), data modeling (some or all presentation-zone data is
copied into the RDW and relationally modeled — often third normal form,
sometimes a star schema), and visualization (business users query the RDW
through familiar BI tooling). Each stage's output can also be consumed
directly — data scientists train against the raw, cleaned, or presentation
lake zones, or a dedicated sandbox zone, without necessarily waiting for data
to reach the RDW at all.

**Division of labor between the two halves** follows from their different
audiences: the lake serves data scientists and power users who can navigate
its more complex structure and need schema-on-read speed and cheap
experimentation space, while the RDW serves non-technical business users who
need low query latency, mature BI tooling, fine-grained (row- and
column-level) security, and a model built by someone who already knows what
questions will be asked of it. Because the RDW copy trails the lake by
however long the copy-and-model step takes, self-service BI against the RDW
is trading immediacy for consumability — the same trade-off
[data federation and virtualization](data-federation-and-virtualization.md)
makes in the opposite direction by querying live instead of materializing a
copy at all.

The practical cost this architecture accepts deliberately: every byte
replicated into the RDW is paid for twice — once in the lake, once in the
RDW — plus the pipeline work to keep the copy current with schema and content
in the lake. Whether a specific source's data is worth replicating into the
RDW at all, or should skip the lake and go straight there, is its own
decision — see
[bypassing the lake for clean relational sources](lake-bypass-for-clean-relational-sources.md).

Few organizations reach this architecture in one migration — see
[stepping-stone architectures toward a modern data warehouse](stepping-stone-architectures-to-mdw.md)
for the interim states most migrations pass through on the way here.
