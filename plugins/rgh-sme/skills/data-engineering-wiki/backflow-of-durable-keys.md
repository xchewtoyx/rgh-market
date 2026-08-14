---
type: concept
title: Backflow of Durable Keys to Earlier Pipeline Stages
description: >
  Pushing enterprise surrogate keys and other derived enrichment back toward
  earlier, lower-latency stages of a multi-hop pipeline, instead of treating
  data flow as strictly one-directional toward the warehouse.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 21"
---

A pipeline with several staged caches of increasing latency and quality —
raw ingestion, a fast operational cache, a business-activity cache, a
warehouse — is usually pictured as one-directional: data gets progressively
more refined as it moves toward the warehouse. But some of what gets
produced deep in the pipeline is valuable earlier, not just later, and it's
worth deliberately flowing back:

- **Durable surrogate keys** are the clearest case. Once an entity has been
  assigned an [enterprise surrogate key](surrogate-vs-business-keys.md) — or,
  when the natural key itself isn't stable, a [durable key](durable-key.md) —
  the earliest pipeline stages benefit from having it too — every application
  operating on that entity, however early in the pipeline, can then refer to
  it consistently instead of only the warehouse layer having a stable
  identifier while everything upstream is still juggling incompatible
  natural keys from different sources.
- **Derived summaries** (historical aggregates, results from downstream
  analysis) can similarly be packaged and pushed back toward earlier stages
  or even the original source, as simple indicators or totals a
  fast-latency consumer can use without querying the warehouse directly.

The practical implication for pipeline design: don't assume the transform
step that assigns an identifier or computes a derived value is also the last
step that could use it. If an earlier stage of the same pipeline — or the
source system itself — has a legitimate use for a key or value that only
gets computed downstream, route it back rather than forcing every consumer
to be a downstream consumer.
