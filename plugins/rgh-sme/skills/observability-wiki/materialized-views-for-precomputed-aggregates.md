---
type: concept
title: Incremental Materialized Views for Precomputed Aggregates
description: An incrementally-maintained materialized view acts as a trigger that writes a filtered or aggregated result to a separate table at insert time, shifting cost from query time to insert time — useful for aggregates queried often enough that recomputing them on every query is wasteful.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
---

An incremental materialized view behaves like an `AFTER INSERT` trigger on a base table: every time new data is inserted, a filtered or aggregated derivative of it is written to a separate output table automatically, rather than being recomputed from scratch on every query against the base table. This shifts cost from query time to insert time, which is a good trade whenever a specific aggregate is queried often relative to how often the underlying data changes — e.g. a raw-logs table feeding an error-only-logs view, which in turn feeds an error-aggregates view, chaining several materialized views together.

This is a deliberate pre-aggregation, made with full knowledge of the trade-off described in [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md) — the raw data underlying a materialized view is still retained in the base table, so nothing is actually lost; the materialized view is an accelerator for a known-common query pattern, not a replacement for the raw event stream. It complements [skip indexes](skip-indexes-for-high-cardinality-lookups.md) and query-time projections (an auto-maintained alternate sort order/subset of a table) as ways to make a known access pattern cheap without redesigning the base table.
