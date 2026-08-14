---
type: concept
title: Data Federation and Virtualization
description: >
  Querying multiple heterogeneous sources as if they were one, without
  first centralizing the data into a warehouse or lake — and why it's a poor
  substitute for a real ingestion pipeline against a live production source.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8-9"
---

A **federated query** lets an OLAP engine select directly from an external
source — object storage, an RDBMS — within a single query, combining results
transparently rather than requiring the data to be ingested first. **Data
virtualization** is the more extreme version: a query engine (Trino/Presto
are the prototypical examples) that stores no data internally at all and
always reads live from whatever sources it fronts. **Query pushdown** — 
pushing filtering and computation down into the source system itself rather
than pulling everything across the network first — is what keeps either
approach performant, since network transfer into the federation layer is
usually the real bottleneck.

Federation is a strong fit for exploratory, ad hoc analysis that needs to
blend sources quickly without standing up a full ingestion pipeline first —
and it has a genuine access-control advantage, since a consumer only ever
sees the specific slice of a live source they're permitted to query, without
a separate data dump or export step being provisioned for them.

The important caution: virtualizing a production database does **not** by
itself solve the problem [source system evaluation](source-system-evaluation.md)
already flags — "will reads impact source performance?" A virtualization
engine that stores nothing hits the live source on every single query, so
exposing it directly to ad hoc analytical traffic against a production OLTP
system risks exactly the load problem a proper pipeline is meant to avoid.
The better pattern is to use federation as a component *inside* a scheduled
pipeline — pulling from a source at a known low-load time and landing the
result in object storage for downstream use — rather than exposing a live
production source directly through a federation layer to end users.

**A zero-staging federated architecture also gives up whatever the pipeline
would otherwise have provided around the data it touches**: if nothing is
ever written to durable pipeline storage, there's no
[archived extract to reprocess](extract-archival-for-reprocessing.md) from,
and backup, recovery, and compliance responsibilities either fall through to
the production source system by default or go unmet entirely. That's a
decision worth surfacing to whoever owns those responsibilities explicitly,
not one to make implicitly by choosing a zero-staging design for latency
reasons alone.

**Choosing movement over virtualization for a given table** comes down to a
handful of concrete engineering trade-offs, not just latency preference:

- Aggregate-once-query-many workloads and cross-source joins needing fast,
  repeatable performance favor moving the data — paying build/maintenance
  cost once instead of pushdown cost on every query.
- Ad hoc, low-volume, or rapidly-prototyped queries favor virtualization —
  there's no [ELT job](etl-vs-elt.md) to build first, so iteration is faster,
  at the cost of ongoing per-query load on the source.
- Moving data duplicates it into a new store, widening the attack surface a
  security review has to cover; virtualization keeps one copy in one place,
  which can simplify that review but concentrates all query load on the
  source's own access controls.
- A moved copy goes stale the moment it's loaded and needs an
  [incremental](incremental-vs-full-extraction.md) or scheduled refresh to
  stay current; a virtualized read is always current because it hits the
  source live — the trade a scheduled pipeline is explicitly built to
  amortize.
- Data that must not cross a compliance or sovereignty boundary (data
  residency rules being the sharpest example) is a strong argument for
  virtualization or federation over movement, since a copy landing outside
  the boundary is itself the violation — no retention or masking policy
  downstream can undo it.

A single warehouse can mix both: move the tables that get aggregated and
joined repeatedly, and federate the ones queried rarely or that must stay in
place for compliance reasons, rather than treating the choice as all-or-
nothing across the platform.
