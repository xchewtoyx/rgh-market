---
type: concept
title: Cardinality Explosion in Time-Series Databases
description: Time-series databases amortize cost by reusing the same time-series/tag combination repeatedly, so adding a high-cardinality tag like user ID creates a new time series per unique value instead of reusing one, with storage overhead proportional to event count rather than amortized — this is the structural reason TSDBs are a poor fit for unified, wide-event observability.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 13"
---

A time-series database's cost model depends on the same time-series/tag combination recurring many times, so its storage cost can be amortized across all the data points that share that combination. Adding a high-[cardinality](cardinality.md) tag — `user_id`, `request_id` — breaks this assumption: instead of many data points sharing one series, each unique tag value spawns its own new series, so overhead becomes proportional to the number of distinct values (potentially the number of events) rather than amortized across them. This is **cardinality explosion**, and it's the core reason TSDBs fail as a backing store for the [unified wide-event model](three-pillars-vs-wide-events-model.md) even though they work well for genuinely low-cardinality infrastructure metrics.

General-purpose NoSQL stores fare similarly poorly for a related reason: pre-built indexes can't support arbitrary ad hoc multi-dimensional queries, and indexing every column can make the index bigger than the data itself. Systems built specifically for high-cardinality, high-[dimensionality](dimensionality.md) observability data instead use approaches like [row vs. column storage trade-offs](row-vs-column-storage-tradeoff.md) tuned around this workload, rather than a general-purpose time-series or document store.
