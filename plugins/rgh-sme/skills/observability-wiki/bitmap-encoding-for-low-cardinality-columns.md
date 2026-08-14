---
type: concept
title: Bitmap Encoding for Low-Cardinality Columns
description: A column with few distinct values can be encoded as one run-length-compressed bitmap per distinct value, letting a query engine answer filters with cheap bitwise AND/OR over compressed data instead of scanning and comparing raw values row by row.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
---

For a column with few distinct values across many rows — a status enum, a boolean flag, an environment name — a columnar store can encode it as *n* separate bitmaps, one per distinct value, with one bit per row marking whether that row holds that value. These bitmaps compress extremely well with run-length encoding, since a low-[cardinality](cardinality.md) column tends to have long runs of the same value. Query execution then answers filters (`WHERE status = 'error' AND env = 'prod'`) with bitwise `AND`/`OR` directly over the compressed bitmaps, which is far cheaper than decompressing and comparing raw values row by row.

This is the low-cardinality counterpart to [skip indexes for high-cardinality lookups](skip-indexes-for-high-cardinality-lookups.md): bitmap encoding works because a low-cardinality column has few enough distinct values that indexing every one is cheap, while a high-cardinality column (a request ID, a raw error message) needs a probabilistic or range-based skip index instead, because indexing every distinct value would be as large as the data itself. Choosing between the two is really a question of where a given column falls on the [cardinality](cardinality.md) spectrum, not a single one-size-fits-all indexing strategy for a columnar observability store.
