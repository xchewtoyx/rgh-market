---
type: concept
title: Pivot Tracing HDFS Replica-Selection Bug Case Study
description: A worked diagnosis of uneven HDFS DataNode load — where per-DataNode metrics showed skew but couldn't explain why — resolved only by chaining happened-before joins across client, NameNode, and DataNode tracepoints to expose a static replica-ordering bug.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §6.1"
---

This case study is the paper's centerpiece example of using [happened-before joins](happened-before-join.md) to diagnose a bug in a **shared, multi-tenant lower-layer service (HDFS) whose own metrics cannot distinguish which upstream client is responsible for its load** — requiring correlation of client identity through the NameNode's routing decision down to which DataNode actually served each request.

**Background:** HDFS replicates each block onto several machines (typically 3). A client reading a block contacts the NameNode (`GetBlockLocations`) for replica hosts, then selects the closest: (1) a local replica; (2) else rack-local; (3) else random.

**Setup:** 96 stress-test clients on an 8-DataNode + 1-NameNode cluster with identical hardware. Each host ran closed-loop random 8kB reads from 10,000 128MB files, replication factor 3.

**Diagnosis walkthrough:**

1. Clients on hosts A and D had consistently lower throughput than others despite identical hardware. Machine-level network throughput showed substantial variation.
2. **Q3** — DataNode RPC tracepoint, grouped by host — showed HDFS request throughput highly skewed (host A ~150 ops/sec, host H ~25 ops/sec). Unexpected given uniform random reads.
3. **Q4** — [happened-before join](happened-before-join.md) correlating each `GetBlockLocations` call with the StressTest client that issued it — confirmed each client's file read distribution was normal/uniform; clients on A and D were skewed left in overall read count (consistent with lower throughput). Client behavior was as expected; anomaly was downstream.
4. **Q5** — join with `getloc.replicas`, grouped by (client host, replica set) — replicas near-uniformly distributed across DataNodes per client. Equal *opportunity* to read from every DataNode, yet Q3 showed they didn't.
5. **Q6** — join correlating which DataNode actually served each request, grouped by (client host, DataNode host) — clients clearly favoring particular DataNodes. Diagonal consistent with local-replica preference (39%), but non-local cases should pick rack-local replicas uniformly at random — clearly they did not.
6. Final steps: clients always selected the **first** location in the NameNode's returned list. **Q7** — three-way happened-before join across DataNode, NameNode, and client tracepoints, filtering out local reads — measured conditional probability of one DataNode preceding another in the returned list. Host A was always selected when it hosted a replica; host D always selected unless A was also a replica — a fixed, static precedence ordering.

**Root cause:** two conflicting behaviors — the HDFS client does not randomly select between non-local replica candidates, and the NameNode does not randomize rack-local replica order — produce a fixed global ordering concentrating load on whichever hosts sort first. Already reported as **HDFS-6268** ("Better sorting in `NetworkTopology#pseudoSortByDistance`").

**General pattern:** HDFS's own per-DataNode metrics (Q3-equivalent) show *that* load is uneven but not *why* — no visibility into upstream caller identity or NameNode routing decisions. The root cause became visible only by correlating identity and routing **across** three components (StressTest client → NameNode → DataNode), each seeing only its local piece. This is the same [attribution blind spot](attributing-shared-service-load-to-callers.md) and [cross-tier observability gap](cross-tier-observability-gaps.md) pattern, resolved at query time via [Pivot Tracing](pivot-tracing.md) rather than pre-defined metrics.
