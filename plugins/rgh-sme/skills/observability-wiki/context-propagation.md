---
type: concept
title: Context Propagation
description: Context — a trace ID, span ID, and baggage — is the glue that lets every telemetry signal correlate back to the same unit of work, and has to be carried both across process/service boundaries (interprocess) and within a single process across async/thread boundaries (intraprocess).
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §2.2"
---

Every span's identity depends on **context** — its trace ID, span ID, and any "baggage" (arbitrary key-values meant to travel with the request) — being available wherever the next piece of work happens. Context propagation is how that context gets there. Two distinct mechanisms are needed:

- **Interprocess propagation** — carrying context across a network call, via carriers like HTTP headers (W3C TraceContext is the standard format), message envelopes, or gRPC metadata.
- **Intraprocess propagation** — carrying context across boundaries *within* one process, e.g. through thread-locals or async-local-storage as execution hops between callbacks/coroutines.

Most languages and [auto-instrumentation](automatic-vs-custom-instrumentation.md) libraries handle both automatically for common frameworks, but propagation frequently breaks in unusual cases: fire-and-forget background jobs, custom thread pools, and any hand-rolled async pattern the auto-instrumentation doesn't recognize. When it breaks, spans that should share a trace ID end up as disconnected, orphaned root spans instead. Because automatic propagation can never cover every non-standard control-flow pattern a large, heterogeneous codebase will eventually contain, it's worth also exposing a small manual-propagation API as an escape hatch — letting a developer explicitly carry context across the specific gap the automatic mechanism missed, rather than leaving that one code path permanently untraceable. Google's Dapper achieves near-transparent propagation precisely by narrowing the surface it needs to cover: it instruments a small number of libraries used almost universally in its environment — a common threading/callback library (which re-attaches a callback's captured context to whatever thread eventually executes it) and a single company-wide RPC framework (which carries trace/span ids in the RPC's own request headers for the interprocess hop) — rather than trying to handle arbitrary user code.

Context propagation is the mechanism that makes [distributed tracing](trace-anatomy-and-spans.md) possible at all — without it, spans from different services would have no way to know they belong to the same request. See [span links vs. parent-child nesting](span-links-vs-parent-child.md) for how correlation is handled in architectures (streaming/fan-out pipelines) where a strict single-trace-tree model doesn't fit.
