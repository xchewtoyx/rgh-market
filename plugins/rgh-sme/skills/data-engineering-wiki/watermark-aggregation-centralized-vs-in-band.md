---
type: concept
title: Watermark Aggregation (Centralized vs. In-Band)
description: >
  How distributed streaming engines aggregate per-shard watermarks — via a
  central service or in-band with data — and the trade-offs each approach
  imposes on latency, availability, and debuggability.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 4"
---

Real pipelines shard each stage across workers with per-range watermarks for
each subcomponent (input buffers, state, output buffers). Those per-range
values must compose into a stage-level watermark. Two dominant patterns:

**Centralized aggregation (Cloud Dataflow style):** a dedicated aggregator
agent (itself shardable) collects per-range updates and is the single source
of truth. Correctness requires every range to report — a missing range blocks
advancement, treated as unknown rather than skipped — and updates must be
monotonic (never move backward). Because workers hold leases on key ranges,
the protocol must verify a worker still holds its lease before admitting its
watermark update, preventing stale updates from a worker that lost a range.

**In-band propagation (Apache Flink style):** sources emit watermark
checkpoints synchronously alongside data; downstream operators consume both,
advance their local watermark, and emit new checkpoints downstream. Advantages:
lower propagation latency (no extra aggregation hops), no single point of
failure stalling the whole pipeline, inherent scaling with the data path.
Disadvantages: no global queryable watermark for monitoring or input throttling;
each component sees only a partial view; some source watermarks need global
information (source idleness, sparse-data heuristics) that is easier to
compute centrally.

Choose based on operational needs: centralized aggregation favors
debuggability, monitoring, and sources requiring global signals; in-band
favors latency and resilience to partial unavailability.
