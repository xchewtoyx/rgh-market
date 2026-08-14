---
type: concept
title: Pivot Tracing Agent
description: A Pivot Tracing agent thread in each enabled process receives weave instructions via a central pub/sub server, installs advice at tracepoints, and performs partial local aggregation before publishing query results at a configurable interval.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §5"
---

Each [Pivot Tracing](pivot-tracing.md)-enabled process runs an **agent thread** that:

1. Awaits instructions via a central pub/sub server to weave [advice](pivot-tracing-advice.md) into [tracepoints](pivot-tracing-tracepoints.md).
2. Accumulates tuples emitted by advice, performing partial aggregation according to their source query ([query optimizations](pivot-tracing-query-optimizations.md) push more aggregation here).
3. Publishes partial query results at a configurable interval — default: once per second.

This mirrors the collection-agent pattern in [telemetry pipeline agent/gateway architecture](telemetry-pipeline-agent-gateway-architecture.md): co-located collection with local reduction before global export, keeping network traffic proportional to query result cardinality rather than raw event rate.

Dynamic instrumentation weaves advice at runtime via Java's `java.lang.instrument` package and **Javassist** bytecode rewriting — similar in spirit to DTrace and Fay. New tracepoints can be defined at runtime; advice is dynamically woven and unwoven. Tracepoints support entry, exit, or exceptional return of any method, or insertion at specific line numbers, defined by class name, method name, signature, and weave location with pattern matching (e.g. all methods of an interface — modeled after AspectJ pointcuts).

**Zero-probe effect:** Pivot Tracing only modifies the system when advice is actually woven — methods are unmodified by default, so inactive tracepoints impose truly zero overhead until advice is installed. This contrasts with hard-coded predefined tracepoints that cost at least a conditional check even when unused.
