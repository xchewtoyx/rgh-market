---
type: concept
title: Data Temperature Tiering
description: >
  Classifying data as hot, lukewarm, or cold by access frequency to choose
  the right storage tier and control cost.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Storage choice should follow access frequency, not just data size:

- **Hot data** is accessed many times a day, sometimes multiple times a
  second — it needs fast retrieval, where "fast" is relative to the use case,
  not an absolute number.
- **Lukewarm data** is accessed weekly or monthly.
- **Cold data** is rarely queried and belongs in archival storage — historically
  shipped to offsite tape, and in the cloud offered as tiers that are cheap to
  store but comparatively expensive to retrieve.

There is no universal storage recommendation: every storage technology trades
off differently depending on use case, data volume, ingestion frequency,
format, and size. Temperature tiering is one input into partitioning and
retention design (see [data retention and lifecycle management](data-retention-and-lifecycle-management.md)),
not a replacement for it — a dataset can be "cold" by access pattern while
still being subject to a legal retention requirement.

**A concrete split worth naming**: a warehouse can keep only its hot window
natively (e.g., the last three years of order history) and let a
[data lake](data-lake-architecture.md) hold everything older, cheaply, as the
cold tier — avoiding both the warehouse storage cost of retaining everything
forever and the performance hit of an ever-growing hot table. Most warehouse
engines can query lake-resident data directly via SQL (through
[data federation](data-federation-and-virtualization.md)), at a real but
acceptable latency cost for the rare query that needs to reach back past the
hot window, without requiring the older data to ever be reloaded into the
warehouse itself.
