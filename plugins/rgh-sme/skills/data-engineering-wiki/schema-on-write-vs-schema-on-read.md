---
type: concept
title: Schema on Write vs. Schema on Read
description: >
  Whether a target enforces structure at load time or defers it to whoever
  reads the data later, and the flexibility/consumability trade-off between
  the two.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

**Schema on write** is the traditional warehouse pattern: a table has a
fixed, integrated schema enforced by a metastore, and every write must
conform to it. **Schema on read** defers that work — data is written in
whatever shape it arrives in, and the schema is worked out by the reader at
query time, ideally from a self-describing format like Parquet or JSON
rather than a format with no embedded structure (CSV is a particularly poor
fit for schema on read, being notoriously inconsistent about types and
column meaning across files).

The trade-off is symmetric: schema on write enforces standards up front,
which makes every future consumption easier because the shape is already
known and guaranteed; schema on read maximizes what can be written — almost
anything can land without a rejected write — at the cost of pushing the
interpretation burden onto every future reader, who has to independently
work out (or trust someone else's prior work on) what the data actually
means.

This choice is a major fork in [ETL vs. ELT](etl-vs-elt.md) design: an
ETL-style pipeline that models data before loading is implicitly choosing
schema on write for its target, while landing raw data first and modeling
later — the [data lake](data-lake-architecture.md) and ELT pattern — is
choosing schema on read, at least for the raw layer.

**Schema on read only postpones relational modeling — it doesn't eliminate
the need for it.** A semi-structured column lets a pipeline accept new or
missing fields without breaking on write, and a query against a path that
doesn't exist in a given record simply returns empty rather than erroring —
genuinely useful for absorbing upstream schema drift without a pipeline
failure. But someone still eventually has to work out what the nested
structure actually means, decide which nested level is a genuine entity
versus a descriptive attribute, and resolve semi-structured records into
whatever normalized or dimensional shape presentation-layer consumers need —
that work is deferred, not skipped, and it still needs the same
domain-expert input a conceptual model would.

