---
type: concept
title: Decouple Ingestion from Query
description: Using a durable, ordered buffer (e.g. Kafka) between stateless ingestion and stateful indexing means an ingestion-side problem can't block querying of already-durable data, and vice versa — the two concerns fail independently instead of coupling into a single point of fragility.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 13"
---

A resilient observability data pipeline separates ingestion and query into independent processes that only share a durable intermediate store, rather than coupling them directly. A representative architecture: stateless receivers accept incoming telemetry and write it straight to a durable, ordered buffer (e.g. Kafka); separate stateful indexing workers consume from that buffer in order and write out the finalized [time-partitioned segments](time-partitioned-columnar-storage.md) that queries actually read.

The payoff is fault isolation: a spike in ingestion volume, or an ingestion-side bug, can't block queries against data that's already durable in the buffer or already indexed into segments — and a query-side slowdown or outage can't back up or drop incoming telemetry, since ingestion only needs the buffer to accept writes, not the query path to be healthy. This is a general resilience pattern for [observability data systems](telemetry-pipeline-stages.md), not specific to any one implementation — the same idea (buffer, then process asynchronously, with each stage able to fail independently) recurs across telemetry pipeline design generally.
