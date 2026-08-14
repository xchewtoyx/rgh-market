---
type: concept
title: Collection-Side Sampling Controls Write Throughput Independent of Instrumentation
description: A second, independent sampling stage inside the collection pipeline — keyed on trace ID so whole traces are kept or dropped together — throttles total data volume reaching storage without requiring every already-deployed instrumented binary to change its sampling rate.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §4.6"
---

The [head-sampling](head-vs-tail-sampling.md) rate baked into instrumented binaries controls *application-side* overhead, but a separate concern is the total volume of data written to the storage/analysis backend — which can approach the backend's write-throughput limit even at a fixed instrumentation-side rate, especially once retention requirements (e.g. weeks of trace history) are added on top.

A second, independent sampling stage inside the collection pipeline — after data leaves the application but before it reaches storage — addresses this directly: for each span seen, hash the span's trace id to a scalar `z` in `[0, 1]` and keep the span only if `z` is below a configurable "collection sampling coefficient." Keying on **trace id, not span id**, is what keeps every span belonging to one trace — which may be scattered across thousands of hosts — either wholly kept or wholly discarded together, rather than fragmenting individual traces into partial, misleading records.

The operational payoff: because this coefficient lives in the collection pipeline's own configuration rather than in every deployed binary, the total write rate to the backend can be adjusted immediately with a single config change — whereas changing the instrumentation-side sampling rate would require redeploying every affected service, which is not a fast operation. In practice this motivates deliberately setting the instrumentation-side rate *higher* than the write-throughput budget requires, then using the collection-side coefficient as the fast-acting throttle for global coverage. This is a specific instance of the "reduce" stage in a [telemetry pipeline](telemetry-pipeline-stages.md) applying [sampling](sampling-rate-selection-strategies.md) a second time, downstream of instrumentation, rather than relying on emission-time sampling alone.
