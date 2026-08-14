---
type: concept
title: Batch versus Serving Jobs
description: >
  Run-to-completion compute optimized for aggregate throughput versus
  long-lived request handlers optimized for per-request latency — different
  failure and scaling shapes on the same fleet.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Batch versus Serving Jobs

Managed-compute fleets run two broad job classes with different optimization
targets and lifetimes:

| | Batch | Serving |
| --- | --- | --- |
| Goal | Aggregate throughput | Per-request latency |
| Lifetime | Minutes to hours (run to completion) | Indefinite (restart on new release) |
| Work unit | [Dynamic chunks](dynamic-work-assignment.md), MapReduce-style stages | Individual RPCs/HTTP requests |
| Canonical examples | Log analysis, ML training | Search query serving |

**Batch jobs** (Global WorkQueue, MapReduce, Flume) benefit from
[dynamic work assignment](dynamic-work-assignment.md) because workers are
[ephemeral](ephemeral-compute-instances.md) and failures are expected at
fleet scale.

**Serving jobs** are often naturally failure-resistant: requests are already
small, independent units dynamically load-balanced across a cluster — the
pattern used since early internet traffic serving. Exceptions that resist
this shape:

- A **leader** holding in-memory or local-filesystem state a replacement
  cannot reconstruct.
- **Sharded data servers** where each replica owns a fixed partition —
  losing one loses that shard until recovery (static assignment problem).
- Servers **known by hostname** to other components — network loss to that
  host breaks callers regardless of internal request-level balancing.

Serving jobs more often pay **longer startup times** (warm indexes, cache
fills) because they are long-lived; batch jobs spin up, drain work, and exit.

Both classes share the cattle requirement: no hardcoded backends, durable
state off-machine, and [idempotent](idempotency.md) handling when the
scheduler duplicates or retries work after presumed failure.
