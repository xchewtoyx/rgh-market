---
type: concept
title: Cross-Tier Observability Gaps
description: In multi-tier, multi-application stacks, root causes and symptoms often appear in different processes, machines, and application layers — and may be visible to different teams — making correlation across tier boundaries the hard part of diagnosis.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §2.3"
---

The second core challenge in layered distributed systems is **crossing boundaries**: the root cause of an issue and its visible symptoms may live in different processes, on different machines, and in different application tiers, visible to different users. A user of one application may need to relate information from a dependent application they don't control to diagnose a problem that spans multiple systems.

Concrete examples from production issue trackers:

- **HBASE-4145** — MapReduce lacks per-task access to HBase metrics; the framework returns only aggregates across all tasks, hiding which task is responsible.
- **MESOS-1949** — task executors don't propagate failure information, making executor-level diagnosis difficult.

A developer quote captures the pain: "The actually interesting/useful information is hidden in one of four or five different places, potentially spread across as many different machines. ... There's a lot of information that is hidden in log files and is very hard to correlate."

End-to-end [distributed tracing](trace-anatomy-and-spans.md) was designed to navigate exactly this kind of issue, and systems like Dapper, HTrace, Cloudtrace, and Zipkin have materialized in production for troubleshooting, debugging, performance analysis, and anomaly detection. They obtain richer per-execution information than component-centric logs or metrics alone. However, most record or reconstruct traces for offline analysis — what gets recorded is still defined [a priori](developer-operator-telemetry-mismatch.md), so a trace schema that didn't anticipate a particular cross-tier question still can't answer it.

[Pivot Tracing](pivot-tracing.md) addresses cross-tier gaps at query time: [tracepoints](pivot-tracing-tracepoints.md) on client protocols and shared lower-layer services, linked by [happened-before joins](happened-before-join.md) and [baggage propagation](context-propagation.md), let operators define new cross-tier breakdowns (e.g. per-client disk throughput through HDFS) without redeploying any tier. See also [attributing shared-service load back to individual callers](attributing-shared-service-load-to-callers.md) for the attribution pattern this enables.
