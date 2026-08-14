---
type: concept
title: Time-Partitioned Columnar Storage
description: Observability datastores commonly partition data into time-bounded, immutable segments and store each field as its own column within a segment, so a query first prunes to the relevant time range and then scans only the specific columns it needs.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 13"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
---

A common pattern for [combining row and column storage strengths](row-vs-column-storage-tradeoff.md): data is first partitioned by time into append-only, immutable segments (finalized once a threshold is hit — a time interval, a record count, or a size limit). Within each segment, data is stored column-per-field, so a field can be scanned across every event in the segment without reading unrelated fields.

Query execution then follows a predictable pipeline: identify which segments overlap the requested time range → within those segments, scan only the columns the query actually references → reconstruct matching rows → aggregate within each segment → aggregate across segments in a final reduce step. Compression (dictionary encoding, run-length encoding, delta encoding) is applied per column and tuned for fast *decompression*, since with this design compute is pushed to read time rather than write time — a query can also define virtual/calculated columns computed only at read time (e.g. `COALESCE($new_field, $old_field)`), letting a schema evolve without rewriting already-stored data. See [schema evolution for wide events](schema-evolution-for-wide-events.md) for a related technique addressing the same underlying problem — new fields appearing over an event stream's lifetime.

Out-of-order data arrival is tolerated by tracking per-segment min/max timestamp metadata rather than requiring strict sort order on ingest, avoiding costly rewrites when a late event arrives. Recent, still-open segments must remain forcibly flushable/queryable so freshly-ingested data doesn't become invisible until a segment closes. See [tiered storage and log retention](tiered-storage-and-log-retention.md) for what happens to segments once they age out of the "recent" window, and [decoupled ingestion and query](decoupled-ingestion-and-query.md) for how this segment model interacts with the ingestion path.

This immutable-segment-plus-background-merge design is the same LSM-tree pattern used by write-optimized key-value engines: new writes land in small segments quickly, and a background process continuously merges smaller segments into larger ones (the same compaction idea behind [ClickHouse's MergeTree naming](row-vs-column-storage-tradeoff.md)). The trade-off that comes with it is **write amplification**: each record gets rewritten multiple times across successive compaction passes. Under sustained high write volume, background compaction can start competing with foreground ingest for disk write bandwidth, which shows up as p99/p99.9 tail-latency spikes on the write path even though average throughput looks fine — and if incoming writes outpace compaction for long enough, unmerged segments accumulate and can exhaust disk space. This is a standing operational risk in any observability backend built on this pattern, not just a one-time tuning problem.
