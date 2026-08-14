---
type: concept
title: Pivot Tracing Baggage
description: Baggage is a per-request container for tuples that propagates alongside execution across thread, application, and machine boundaries, enabling happened-before joins to be evaluated in situ during request execution rather than by global post-hoc aggregation.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §4"
---

The naive strategy for evaluating a [happened-before join](happened-before-join.md) treats it as a global equijoin or θ-join — aggregating tuples cluster-wide before joining. Temporal joins as implemented in Magpie use this expensive global evaluation strategy.

[Pivot Tracing](pivot-tracing.md) avoids global evaluation via **baggage**: a per-request container for tuples propagated alongside the request as it traverses thread, application, and machine boundaries. [Advice](pivot-tracing-advice.md) `Pack` and `Unpack` operations store and retrieve tuples from the current request's baggage. Tuples follow the request's execution path and therefore *explicitly* capture the happened-before relationship — no need to reconstruct causality after the fact.

Baggage generalizes end-to-end metadata propagation from prior [causal tracing](trace-anatomy-and-spans.md) systems (X-Trace, Dapper). Using baggage, Pivot Tracing evaluates happened-before joins **in situ**, during request execution, rather than by aggregating tuples centrally and joining afterward.

If too many tuples end up packed, Pivot Tracing can revert to an alternative plan where all tuples are emitted instead of packed, keeping baggage size constant by storing only enough information to reconstruct causality — à la X-Trace, Stardust, or Dapper. To estimate overhead before running a query, Pivot Tracing can execute a modified version that counts tuples explicitly rather than aggregating them.

See [context propagation](context-propagation.md) for the general baggage concept in distributed tracing, [instrumentation overhead](pivot-tracing-instrumentation-overhead.md) for measured baggage serialization costs, and [baggage branch/rejoin versioning](pivot-tracing-baggage-branch-rejoin.md) for correct handling of parallel execution paths.
