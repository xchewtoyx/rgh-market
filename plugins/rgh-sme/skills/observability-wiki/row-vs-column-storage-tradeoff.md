---
type: concept
title: Row vs. Column Storage Trade-off for Observability Data
description: Row-oriented storage is fast for retrieving one whole record but poor at scanning one field across many records without expensive indexes, while column-oriented storage is the reverse — observability datastores typically combine both by partitioning on time first and storing columns within each partition.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 13"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
---

Two fundamentally different physical layouts for storing wide events, with opposite strengths:

- **Row-based storage** (e.g. Bigtable) — fast to retrieve a single whole record (a trace, a single event) by key. Poor at reading a scattered set of fields across many rows without secondary indexes, and those indexes are themselves expensive: Google's Dapper found that indexing just 3 fields cost 76% of the trace data's own storage size.
- **Column-based storage** (e.g. Dremel/ColumnIO, or ClickHouse's MergeTree engine) — fast for scanning one field's values across many rows (exactly the access pattern the [core analysis loop](core-analysis-loop.md) needs). Poor for reconstructing one specific row without extra bookkeeping to reassemble scattered column values back into a record.

Because observability workloads need both — fast full-trace retrieval *and* fast wide scans across many events for a specific field — practical systems use a **hybrid**: partition data by time first into segments/parts, then store data column-per-field *within* each segment. This is the approach both Honeycomb's Retriever and ClickHouse's MergeTree engine take (see [time-partitioned columnar storage](time-partitioned-columnar-storage.md)), and it's specifically what lets a query scan only the columns it actually needs within a time range, rather than reading whole rows or scanning entire tables.

Column storage's scan speed comes from more than just avoiding unneeded columns: because one column's values sit contiguously in memory, a query engine can process them with **vectorized execution** — iterating over blocks small enough to fit CPU L1 cache, using SIMD instructions to operate on many values per instruction, instead of a row-at-a-time loop that pays function-call and pipeline overhead per value. Low-[cardinality](cardinality.md) columns compound this further: see [bitmap encoding for low-cardinality columns](bitmap-encoding-for-low-cardinality-columns.md) for how a column with few distinct values can be scanned and filtered directly on compressed data.
