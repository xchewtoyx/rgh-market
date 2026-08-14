---
type: concept
title: Single-Repository Lakehouse vs. Dual-Repository Warehouse Copy
description: >
  Weighing a lakehouse's one-repository simplicity against the query speed,
  security, and metadata reliability an RDW copy still buys.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 12"
---

A [lakehouse](data-lakehouse.md) and a
[modern data warehouse (MDW)](modern-data-warehouse-architecture.md) answer
the same underlying question — how to give lake-scale data warehouse-grade
reliability — with structurally opposite architectures: the lakehouse keeps
one repository and adds warehouse-like controls on top of it; the MDW keeps
two repositories and pays a replication cost to get genuine warehouse
behavior in the second one. Choosing between them (or, in practice, deciding
per-dataset which pattern to follow) means weighing what collapsing to one
repository buys against what it gives up.

**What one repository buys, directly from having no copy step at all**:

- No **reliability** risk from a copy job failing or silently misplacing
  data, and no risk of a report against the copy diverging from a report
  against the original.
- No **staleness gap** — an RDW copy is always at least as old as however
  long the last copy job took (itself throttled to avoid hurting production
  query performance); collapsing to one repository removes that gap entirely
  rather than just shrinking it.
- Native support for **advanced analytics/ML tooling**, which mostly targets
  lake-native files rather than warehouse tables.
- Lower **total cost of ownership** — no compute for the copy job, no second
  copy's storage cost, no separate (typically pricier) warehouse compute, and
  no need to staff for two distinct skill sets.
- Simpler **governance** — one copy under one security model, rather than
  keeping quality and transformation rules consistent across two.
- Lower **operational complexity** overall — one system to run instead of
  two.

**What the second repository still buys, and what's given up by skipping
it**:

- **Query speed**: a genuine RDW, especially an MPP-based one, still
  outperforms schema-on-read query engines on the query-optimization features
  it's had decades to mature — advanced indexing, materialized views, cost-
  based join optimization, native caching. Lakehouse performance techniques
  (data skipping, Z-order clustering, predicate pushdown) narrow this gap but
  don't close it.
- **Security surface**: mature RDW features — row- and column-level security,
  at-rest and column-level encryption, dynamic data masking, workload
  management, audit trails built for compliance certification — often have no
  lakehouse-native equivalent, or only a partial one.
- **Concurrency**: RDWs support far more concurrent readers/writers through
  locking, isolation levels, and transaction management built specifically
  for that workload.
- **Metadata reliability**: an RDW's [schema-on-write](schema-on-write-vs-schema-on-read.md)
  forces metadata and data to stay locked together by construction — they
  can never silently drift apart. A file-based lakehouse's metadata can live
  in separate files, be embedded inconsistently, or simply be wrong, since
  nothing enforces a one-to-one relationship the way a warehouse's metastore
  does. This is the same gap a [relational serving layer](relational-serving-layer.md)
  is built to paper over, not eliminate.
- **Tooling lock-in**: some lakehouse table-format features tie a team to a
  specific compute engine (e.g., Spark); migrating off it later means
  rewriting stored procedures, views, and dashboards, and retraining users
  away from the relational tools and mental model they already know.

None of these gaps is individually disqualifying, and they narrow every year
as lakehouse table formats add more warehouse-like features. The practical
approach: default to a single-repository lakehouse, and copy a *specific*
dataset out to an RDW only once a concrete trade-off from the second list
becomes a measured blocker for that dataset's actual consumers — e.g., a
dashboard that needs millisecond response when lakehouse queries average
several seconds — rather than deciding for or against a second repository for
an entire platform up front.
