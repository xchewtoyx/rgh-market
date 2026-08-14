---
type: concept
title: File Format Selection for Pipelines
description: >
  Why the choice between row-based and columnar serialization formats is a
  real performance lever in pipeline design, not an interchangeable detail.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), appendix A"
---

The serialization format a pipeline reads and writes is a genuine
performance lever, not an interchangeable formality — switching a job from
CSV to Parquet has produced 100x throughput improvements in practice.

**Row-based formats** store each record as one unit, which suits
semistructured, nested, schema-variable data well:

- **CSV** is really a catchall term for delimited text with no single fixed
  convention for escaping, quoting, or delimiters — it's genuinely error
  prone and poor-performing, but often unavoidable when exchanging with
  external systems outside a pipeline's control. If it must be used for
  archival, always store the exact serialization configuration alongside
  the files, since CSV carries no self-describing schema.
- **JSON** is the modern default for API exchange; **JSONL** (line-delimited
  JSON) suits staging bulk semistructured data immediately after ingestion,
  but columnar formats outperform it enough that JSONL is best treated as an
  early-pipeline staging format, not a serving format.
- **Avro** encodes data in binary with JSON-specified schema metadata —
  common in the Hadoop ecosystem.

**Columnar formats** split each column into its own files, so a query can
read only the columns it needs — a large win for analytics workloads that
scan wide tables but touch few columns per query — and compress far better,
since adjacent values in a column tend to be similar. The trade-off is
symmetric with [OLTP vs. OLAP](oltp-vs-olap.md): reconstructing a single
record means reading across many column files instead of one row lookup,
and updating even one field means decompressing, modifying, and recompressing
the whole affected column file — the same [copy-on-write cost](copy-on-write-load-cost.md)
problem shows up here at the format level, which is exactly why columnar
formats are a poor fit for transactional workloads.

- **Parquet** is the dominant columnar interchange format for data lakes —
  it natively encodes schema and nested structures (solving CSV's two worst
  problems) and is genuinely portable across engines, unlike a warehouse's
  proprietary internal columnar format, which performs excellently inside
  that warehouse but costs a deserialize/reserialize round trip to hand off
  to an external tool like Spark or Presto.
- **ORC** is a Parquet-like predecessor with weaker modern cloud support.
- **Apache Arrow** is an in-memory columnar format designed so the same byte
  layout works for both in-memory processing and export, eliminating the
  serialize/deserialize step between them entirely — a file can be mapped
  directly into a program's address space and queried with no conversion
  step, which is what lets tools built on Arrow move data between languages
  (Python, Scala, and others) as if passing a shared object.

A pipeline commonly needs **reserialization** — converting between these
formats mid-pipeline — whenever data crosses from a system optimized for one
format into a system optimized for another; budgeting for that conversion
cost explicitly, rather than treating format choice as a detail to decide
later, is what avoids surprises like a job that's slow purely because of
avoidable format conversion overhead.
