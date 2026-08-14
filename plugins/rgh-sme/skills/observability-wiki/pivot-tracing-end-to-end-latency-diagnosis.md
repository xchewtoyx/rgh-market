---
type: concept
title: Pivot Tracing End-to-End Latency Diagnosis
description: Pivot Tracing decomposes request latency across components by packing timestamps at one tracepoint and unpacking them at a later one along the same causal chain, enabling per-component latency breakdown and anomaly comparison without pre-defined latency metrics.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §6.2"
---

[Pivot Tracing](pivot-tracing.md) can express queries about time spent by a request across the components it traverses, using the built-in `time` variable every [tracepoint](pivot-tracing-tracepoints.md) exports. [Advice](pivot-tracing-advice.md) packs the timestamp at one event and unpacks it at a subsequent event along a [happened-before join](happened-before-join.md), enabling direct timestamp comparison:

```
From response In SendResponse
Join request In MostRecent(ReceiveRequest) On request -> response
Select response.time - request.time
```

`MostRecent` selects only the most recent preceding `ReceiveRequest` whenever a `SendResponse` occurs. Queries compose: a follow-on query joins this latency with `JobComplete` events to measure average request latency experienced by Hadoop jobs — reminiscent of transaction tracking in Timecard and transactional profiling in Whodunit.

**Worked example — network limplock:** during Pivot Tracing's own development, a faulty network cable caused a link to downgrade from 1 Gbit to 100 Mbit. An HBase workload hit latency spikes on this bottleneck. Diagnosis decomposed requests into per-component latency and compared anomalous requests (>30s end-to-end) against the average case, identifying time blocked on the network in the HDFS DataNode on the affected host as the bottleneck. Measuring latency/throughput for all workloads at that component then revealed the host's uncharacteristically low network throughput. The same approach replicated diagnosis of rogue garbage collection in HBase RegionServers and an overloaded HDFS NameNode caused by exclusive write locking.

This is [cross-tier observability](cross-tier-observability-gaps.md) applied to latency: the symptom (slow HBase requests) and the root cause (degraded network link on a DataNode) live in different tiers, joined by causal metadata rather than a pre-defined end-to-end latency metric.
