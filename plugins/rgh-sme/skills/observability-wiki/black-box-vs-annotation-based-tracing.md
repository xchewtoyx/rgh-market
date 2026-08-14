---
type: concept
title: Black-Box vs. Annotation-Based Distributed Tracing
description: Distributed tracing systems associate scattered message records with the request that caused them either by statistically inferring the association from unmodified message traffic (black-box) or by having every hop explicitly tag records with a shared identifier (annotation-based) — the latter needs instrumentation but is far more precise with far less data.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §1"
---

A distributed tracing system's core problem: given a stream of message identifiers and timestamped send/receive events scattered across many machines, associate the ones belonging to the same originating request. Two fundamentally different families of solution:

- **Black-box schemes** assume no extra information beyond the message records themselves, and use statistical regression to infer which records belong together. More portable — nothing needs to be added to the applications generating the traffic — but the inference needs substantially more data to reach acceptable accuracy, since it's reconstructing structure the system doesn't actually know.
- **Annotation-based schemes** rely on applications or middleware to explicitly tag every record with a global identifier (a trace ID) linking it back to the originating request — this is [context propagation](context-propagation.md). Far more precise and needs far less data per request, but its key disadvantage is that it requires instrumenting the programs generating the traffic.

The annotation-based disadvantage — needing to instrument every program — can be neutralized rather than accepted: if a small number of libraries (a common RPC framework, a common threading/control-flow library) already carry effectively all the traffic in an environment, instrumenting just those libraries achieves annotation-based precision while pushing the instrumentation burden down into shared infrastructure instead of onto individual application developers. This is what makes [automatic instrumentation](automatic-vs-custom-instrumentation.md) of common frameworks a way to get annotation-based tracing's accuracy without annotation-based tracing's usual cost.
