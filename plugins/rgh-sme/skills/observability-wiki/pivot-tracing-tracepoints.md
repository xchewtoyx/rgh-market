---
type: concept
title: Pivot Tracing Tracepoints
description: In Pivot Tracing, tracepoints are externally defined instructions on where and how to inject runtime instrumentation — resembling aspect-oriented pointcuts rather than fixed probes compiled into the target system.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §2.2"
---

Pivot Tracing queries refer to variables exposed by one or more **tracepoints** — places in the system where the framework can insert instrumentation at runtime. Tracepoints are not part of the application source; they are instructions on where and how to change the running system to export identifiers and values. They resemble **pointcuts** from aspect-oriented programming: a named location in code (a class method, a protocol handler) that advice can attach to when a query demands it.

Tracepoints are defined by someone with system knowledge — a developer or expert operator who knows which internal methods expose the quantities a diagnosis will need. The resulting query vocabulary can be defined, installed, and shared or disseminated at any time, without waiting for an upstream project to merge new metrics. Besides any explicitly declared exports, every tracepoint automatically exposes `host`, `timestamp`, process id, process name, and the tracepoint's own definition. This is a different notion of "tracepoint" from kernel [stable vs. dynamic instrumentation points](stable-vs-dynamic-instrumentation-points.md): Pivot Tracing tracepoints live in the application/JVM layer and are installed on demand by the monitoring framework, not pre-declared in kernel source or USDT macros.

A worked example: intercepting `DataNodeMetrics.incrBytesRead(int delta)` on HDFS DataNodes exposes `incr.host` and `incr.delta` for local aggregation; intercepting client-protocol methods (`DataTransferProtocol`, `ClientService`, `ApplicationClientProtocol`) exposes `cl.procName` for [cross-tier attribution](attributing-shared-service-load-to-callers.md) via a [happened-before join](happened-before-join.md).
