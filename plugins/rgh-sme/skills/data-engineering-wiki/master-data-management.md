---
type: concept
title: Master Data Management (MDM)
description: >
  Building consistent "golden records" for core business entities across a
  growing or merging organization, and why a pipeline engineer needs to know
  it exists even without owning it.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Master data management is the practice of building consistent "golden
records" for business entities — employees, customers, products, locations —
across an organization, especially one that has grown or merged and ended up
with the same entity represented inconsistently in multiple systems. A
typical example: an MDM effort standardizing address format and then building
a matching/deduplication system across company divisions.

MDM is primarily a business-process discipline enabled by technology; it may
or may not sit under data engineering organizationally. Either way, a pipeline
engineer needs to be aware it exists, because a pipeline that joins across
systems on an entity key (customer ID, product ID) is implicitly depending on
however good or bad that entity's MDM currently is — inconsistent golden
records upstream become silent join failures or duplicate rows downstream, and
no amount of pipeline-level [data quality](data-quality-dimensions.md)
checking fixes an entity-resolution problem that MDM was supposed to solve.

When a pipeline itself is responsible for producing the golden record —
rather than consuming one MDM already maintains — that work happens as
[deduplication and survivorship](deduplication-and-survivorship.md) inside
the load.

**The round-trip through an MDM product**, when one exists, is itself a
pipeline a data engineer builds and operates: source records are copied into
the MDM tool, which cleans, standardizes, and matches them into one master
record per entity — automatically for most duplicates, with a manual review
queue for near-duplicates the matching rules can't resolve confidently — and
the resulting golden records are copied back out into the lake or warehouse.
When building a star schema, those mastered records become the dimension
tables, typically joined against fact tables that were never themselves
run through MDM (transaction-grain data has no "master" version to
converge on). Treat the MDM round-trip as an extraction/load stage like any
other: it needs the same [extraction/transfer](extraction-transfer-method.md)
and scheduling treatment as a source-system pull, just with the MDM product
sitting in the middle of the flow instead of at either end.
