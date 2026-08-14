---
type: concept
title: Data Lake Architecture
description: >
  The dump-everything-in-raw-form pattern for centralizing data without
  imposing structure up front, and the operational failure modes that made
  "data lake 1.0" a cautionary tale for many teams.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

A data lake centralizes all data — structured and unstructured — in one
location without imposing schema or structure at write time, in contrast to
[a data warehouse](data-warehouse-architecture.md)'s pre-modeled, centrally
organized approach. "Data lake 1.0" started on HDFS and later moved to cheap,
near-limitless cloud object storage, decoupling storage from compute (see
[compute/storage separation](compute-storage-separation.md)) and letting
engineers pick their own processing tool (MapReduce, Spark, Ray, Presto,
Hive) rather than being locked into one warehouse engine.

In practice, lake 1.0 accumulated well-documented failure modes that a
pipeline designer should treat as concrete risks, not historical trivia:

- **Data swamp / dark data / WORN** ("write once, read never"): without
  enforced structure or cataloging, a lake becomes a dumping ground where
  data is written but never usefully read again, because nobody can find or
  trust it.
- **Weak schema management, cataloging, and discovery**: unlike a warehouse,
  nothing forces schema to be tracked centrally, so
  [schema evolution](schema-evolution-in-source-systems.md) upstream becomes
  much harder to detect downstream.
- **Painful row-level updates and deletes**: basic SQL DML often required
  full table rewrites, which clashed badly with
  [retention and deletion requirements](data-retention-and-lifecycle-management.md)
  like GDPR's targeted-deletion obligations — a warehouse's native `DELETE`
  had no lake equivalent.
- **Ballooning operational cost**: managing the underlying cluster (originally
  Hadoop) at scale required large, expensive engineering teams, eroding the
  cost savings the lake was originally meant to deliver over licensed MPP
  systems.

Some large, resource-rich organizations made lakes work well; for many
others, an unmanaged lake became a costly, low-trust dumping ground. The
practical lesson for pipeline design: a lake needs the same schema
governance, cataloging, and update/delete tractability a warehouse gets by
default, or it needs [the lakehouse](data-lakehouse.md) pattern that adds
those controls back on top of object storage. Dividing the lake into
[quality zones](data-lake-zone-layering.md) is the concrete structural
counter to the data-swamp failure mode; some organizations also split into
[multiple physically separate lakes](multiple-data-lakes-rationale.md)
entirely, rather than zones inside one.
