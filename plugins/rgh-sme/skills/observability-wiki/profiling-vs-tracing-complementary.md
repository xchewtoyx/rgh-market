---
type: concept
title: Profiling and Tracing Are Complementary, Not Interchangeable
description: Tracing gives a bird's-eye, request-level view across a distributed system and can validate hypotheses across millions of real requests, but it can't afford to instrument every function call; profiling fills in the function-level "why" once tracing has identified which request or endpoint is anomalous.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 20"
---

[Distributed tracing](trace-anatomy-and-spans.md) gives the request-level, cross-service view and lets you validate a hypothesis against millions of real production requests — but instrumenting every function call as its own span would introduce overhead rivaling the work itself, so tracing necessarily stops short of line-level or per-call granularity (see [deciding whether to create a span](deciding-whether-to-create-a-span.md)). [Profiling](fixed-counters-vs-profiling-vs-tracing.md) fills that gap: fine-grained, function-level sampling that's cheap precisely because it doesn't try to capture every call, only a statistical sample of where execution time actually goes.

A concrete illustration: a latency discrepancy between load-balancer-measured and application-trace-measured request duration was invisible to tracing itself, because the actual bottleneck (an HTTP router being reinitialized and its regex config reparsed on every single request) ran *before* the tracing hook fired. A flame graph from statistical CPU profiling found it immediately — 17% of CPU in a function that should only have run once at startup. **Tracing alone couldn't have caught this**, and profiling alone wouldn't have known which requests or endpoints were worth profiling in the first place.

The practical workflow: use tracing to identify *which* endpoint or call is anomalous at the system level (this is what the [core analysis loop](core-analysis-loop.md) is for), then profile to find *why* at the function level (see [CPU flame graphs](cpu-flame-graphs.md) and [observability operates at system scale, debuggers at function scale](observability-vs-debugging-granularity.md) for the same telescope/microscope split applied here). The most valuable optimization targets in a flame graph tend to be functions called often at medium individual cost, or functions near the graph's root with little time spent in their children.
