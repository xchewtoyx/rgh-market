---
type: concept
title: Pivot Tracing Hadoop Instrumentation
description: Enabling Pivot Tracing on Hadoop-ecosystem systems required only 50–200 lines of manual code per system to propagate baggage across RPC and thread boundaries, after which arbitrary queries needed no further modification.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §6"
---

[Pivot Tracing](pivot-tracing.md) was evaluated on four widely-used Hadoop stack systems: HDFS, HBase, Hadoop MapReduce, and YARN. Typical deployments co-locate processes from several applications on the same machine (DataNode, NodeManager, Map/Reduce tasks, RegionServer).

One-time modifications propagated [baggage](context-propagation.md) along request execution paths. The prototype stores baggage in a thread-local variable, so the only required changes set/unset baggage at execution boundaries:

- **Across RPCs** — manually extend each system's protocol definitions.
- **Within a process** — AspectJ instrumentation automatically modifying common interfaces (`Thread`, `Runnable`, `Callable`, `Queue`).

Each system required only **50–200 lines** of manual code modification. Once modified, systems could support arbitrary Pivot Tracing [queries](pivot-tracing-query-language.md) with no further changes. Evaluation queries used [tracepoints](pivot-tracing-tracepoints.md) on both client and server RPC protocol implementations (HDFS `DataTransferProtocol`, NameNode `ClientProtocol`) plus tracepoints piggybacking on existing metric-collection mechanisms (`DataNodeMetrics`, `RPCMetrics` in HDFS; `MetricsRegionServer` in HBase).

This instrumentation cost is the main upfront investment for [causal metadata propagation](context-propagation.md); a system without baggage support can still use Pivot Tracing's dynamic instrumentation alone, resembling DTrace or Fay. See the [HDFS replica-selection bug case study](pivot-tracing-hdfs-replica-selection-bug.md) for a worked diagnosis using these tracepoints.
