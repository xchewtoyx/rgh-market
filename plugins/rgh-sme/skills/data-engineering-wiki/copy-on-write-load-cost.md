---
type: concept
title: Copy-on-Write Load Cost
description: >
  Why an upsert or merge is expensive in file-based columnar storage, and
  how to keep near-real-time update pipelines from overwhelming a warehouse.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

Upsert and merge were designed for row-based databases, where updating a
row in place is a natural, cheap operation. File-based columnar systems
instead rely on **copy-on-write (COW)**: changing or deleting even one
record in a file requires rewriting the entire file with the change
applied. This mismatch — not a lack of engineering effort — is a big part of
why early big-data and lake systems rejected in-place updates outright in
favor of pure [insert-only](table-load-patterns.md) patterns, deferring
"current state" resolution to query time instead.

Modern columnar systems hide this complexity behind native update/merge
support (scan affected files, apply changes, write new files, repoint table
references), but every merge still carries real cost proportional to how
much data it touches. Single-record updates can be surprisingly expensive;
merges over large update sets can be very performant, sometimes even
outperforming a transactional database. The COW granularity a system
rewrites at (partition, cluster-key group, or block) is set by
[partitioning and clustering](partitioning-and-clustering-for-query-pruning.md)
choices — a deliberate partitioning strategy directly determines how
performant a given update pattern will actually be.

**The concrete failure mode to avoid**: teams migrating off a source that
supported near-real-time CDC-driven merges sometimes try to replicate that
same merge cadence directly against a columnar warehouse — this will bring
most columnar warehouses to their knees, with real cases of pipelines
falling weeks behind where a simple hourly merge cadence would have worked
fine. If a target genuinely needs near-real-time freshness without paying
full merge cost on every event, two mitigations exist: streaming inserts
paired with a deduplicating materialized view that resolves "current state"
without a merge on every write, or a two-tier storage engine (fast SSD-backed
recent data plus a slower durable tier) purpose-built for frequent small
writes. The general lesson: match merge frequency to what the target's
storage model can actually absorb, not to what the source system happens to
produce.
