---
type: concept
title: Skip Indexes for High-Cardinality Lookups
description: A skip index (e.g. a bloom filter or a per-granule min/max range) lets a query engine cheaply rule out whole blocks of data that can't contain a match, without needing a full traditional index over every value — but it only helps when the positive-match rate within a block is low.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
---

Finding a specific value in a huge, high-[cardinality](cardinality.md) column (a particular request ID, a specific error string) without scanning every row needs some kind of index — but a traditional per-value index over a high-cardinality field can be as large as the data itself (see [cardinality explosion in TSDBs](cardinality-explosion-in-tsdbs.md) for the same underlying cost problem in a different context).

A **skip index** takes a cheaper approach: rather than indexing every value, it stores a small summary per block of rows (a *granule*) that lets the query engine decide, block by block, whether that block *could possibly* contain a match — and skip scanning it entirely if not. Two common forms:

- **Bloom filter variants** — a probabilistic membership test (e.g. on `RequestId`), or a tokenized full-text variant for substring/keyword search within a text column (e.g. `Message`).
- **MinMax index** — stores each block's minimum and maximum value for a numeric column (e.g. `Duration`), letting the engine skip any block whose range can't contain the value being searched for — a cheap way to hunt for outliers.

Skip indexes only pay for themselves when a block's positive-match rate is low — if most blocks actually contain a match, the index adds storage and lookup overhead without meaningfully reducing how much data gets scanned. They're a targeted optimization layered on top of [time-partitioned columnar storage](time-partitioned-columnar-storage.md), not a replacement for it.

At the opposite end of the cardinality spectrum, a column with only a handful of distinct values doesn't need a skip index at all — see [bitmap encoding for low-cardinality columns](bitmap-encoding-for-low-cardinality-columns.md) for the cheaper technique that applies there instead.
