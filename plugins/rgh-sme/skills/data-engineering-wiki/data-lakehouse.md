---
type: concept
title: Data Lakehouse
description: >
  Adding warehouse-style structure, data management, and ACID transactions
  on top of object storage, closing the gap that made data-lake-1.0 fail.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

The lakehouse pattern (Databricks's framing) is the direct response to
[data lake 1.0's failures](data-lake-architecture.md): it layers
warehouse-style controls — schema enforcement, data management, and ACID
transactions — on top of cheap object storage, while still allowing the
varied query and transform engines a lake is valued for (Spark, Presto, and
similar). ACID transactions specifically close the row-level update/delete
gap that made retention and deletion obligations so painful in lake 1.0. This
guarantee is narrower than a relational database's, though: it holds within a
single table, not across tables — a multi-table DML operation gets no
cross-table atomicity guarantee the way a relational database's transaction
would, which matters for any load that has to keep two related tables
(e.g., a fact table and a bridge table it depends on) consistent with each
other.

At the same time, cloud data warehouses have grown lake-like in the other
direction — [separating compute from storage](compute-storage-separation.md),
scaling to petabytes, and supporting unstructured/semistructured data with
Spark/Beam integration. The practical effect for a pipeline designer is that
"warehouse vs. lake vs. lakehouse" is converging into a single "data
platform" choice (AWS, Azure, Google Cloud, Snowflake, Databricks are the
class-leading vendors) more than three genuinely distinct architectures —
the useful question is increasingly which specific capabilities (transaction
guarantees, engine flexibility, cataloging) a given platform offers, not
which category label it wears.

Two table-management technologies are what actually deliver these
capabilities on top of plain object storage, and it's worth knowing which
problem each one solves. **Apache Hudi** targets the specific case of a
table fed by a CDC stream from a transactional source: incoming changes land
in row-oriented files for fast writes, the bulk of the table stays columnar
for fast reads, queries transparently span both, and a periodic
**repacking** process merges the accumulated row files back into columnar
storage to restore full query efficiency — essentially a built-in answer to
[copy-on-write cost](copy-on-write-load-cost.md) for frequently-updated
tables. **Apache Iceberg** instead focuses on tracking every file and every
snapshot that has ever composed a table, which is what enables table time
travel, [dataset versioning](dataset-versioning-and-zero-copy-cloning.md),
and [schema evolution](schema-evolution-in-source-systems.md) at
petabyte scale without rewriting the whole table on a schema change.

Whether a lakehouse's single repository is actually sufficient for a given
dataset, or whether that dataset still needs an
[RDW copy alongside it](lakehouse-vs-warehouse-copy-decision.md), is a
separate, ongoing decision — not one this pattern settles once for an entire
platform.
