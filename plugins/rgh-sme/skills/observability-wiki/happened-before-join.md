---
type: concept
title: Happened-Before Join in Causal Queries
description: A happened-before join correlates telemetry events along a causal execution chain — "this measurement happened after that context was established" — rather than by a shared timestamp or trace ID alone, and requires propagating captured context from the earlier event to the later one.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §2.1"
---

In Pivot Tracing's [query language](pivot-tracing-query-language.md), the `->` operator denotes a **happened-before join** (⋈): one tracepoint's event is joined to another's because the first causally preceded the second along the same execution, not because they share a key or occurred at the same time.

**Formal semantics:** for events *a* and *b* anywhere in the system, *a → b* ("*a* happened before *b*") if *a*'s occurrence causally preceded *b*'s occurrence **and** both occurred as part of the execution of the **same request**. If *a* and *b* are not part of the same execution, *a ⊬ b*. If *a*'s occurrence did not lead to *b*'s (e.g. two parallel, non-communicating threads), *a ⊬ b*. If *a → b*, then *b ⊬ a*. (This definition does not capture all possible causality — e.g. one request's processing influencing another's — but could be extended.)

For queries Q1 and Q2, Q1⋈Q2 produces tuples *t1t2* for all *t1 ∈ Q1*, *t2 ∈ Q2* such that *t1 → t2* in the execution of the same request. Temporal filters (`First`, `MostRecent`, `FirstN`, `MostRecentN`) restrict which tuples from the joined query participate.

Magpie demonstrated that under certain conditions — 'start'/'end' events demarcating a request's execution on a thread, or a unique identifier present on both sides of a send/receive boundary — causality can be *inferred after the fact* using temporal joins over explicitly encoded causal boundaries. Any Pivot Tracing happened-before-join query has an equivalent formulation using only temporal joins, but that formulation cannot exploit Pivot Tracing's runtime optimizations and requires global evaluation over stored events.

A query like `Join cl In First(ClientProtocols) On cl -> incr` says: take the client-protocol context captured at the first invocation along this causal chain, and attach it to each subsequent `incrBytesRead` event on a DataNode — so bytes read can be grouped by upstream client process name even though the DataNode itself has no visibility into which application initiated the load.

Implementing a happened-before join requires two pieces beyond a simple local aggregation:

1. **Capture at the earlier tracepoint** — record the join key (e.g. `cl.procName`) the first time execution passes through the upstream [tracepoint](pivot-tracing-tracepoints.md); compiled as `Pack`/`Pack-First` in [advice](pivot-tracing-advice.md).
2. **Propagate via baggage** — carry that captured value forward through [Pivot Tracing baggage](pivot-tracing-baggage.md) until the later tracepoint's advice runs, where `Unpack` makes it available for grouping or selection.

This is the mechanism that makes [attributing shared-service load back to individual callers](attributing-shared-service-load-to-callers.md) possible at query time: the shared lower layer emits only anonymous load events, but baggage from an upstream tracepoint supplies the caller identity when those events are processed. Pivot Tracing's query optimizer determines when such propagation must occur and installs the necessary dynamic instrumentation; queries that aggregate entirely at one tracepoint need no join or propagation at all.
