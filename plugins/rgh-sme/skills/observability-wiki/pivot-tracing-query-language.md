---
type: concept
title: Pivot Tracing Query Language
description: Pivot Tracing exposes a LINQ-like query language over tracepoint-exported variables, supporting relational operations plus happened-before joins that correlate events along causal execution chains rather than by shared keys alone.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §3"
---

Pivot Tracing queries are parsed from LINQ-like text and operate over tuples produced at [tracepoints](pivot-tracing-tracepoints.md). Supported operations:

| Operation | Syntax | Role |
|---|---|---|
| `From` | `From x In Tracepoint` | Use input tuples from a tracepoint set |
| Union | `∪` | Combine events from multiple tracepoints |
| Selection | `Where` (σ) | Filter tuples matching a predicate |
| Projection | `Select` (Π) | Restrict to a subset of fields |
| Aggregation | `Count`, `Sum`, `Max`, `Min`, `Average` | Aggregate tuple fields |
| GroupBy | `GroupBy` (G) | Group tuples on one or more fields |
| GroupBy aggregation | `GroupBy ... Select Sum(...)` (GA) | Aggregate within each group |
| Happened-before join | `Join ... On a -> b` (⋈) | Join tuples along the [happened-before relation](happened-before-join.md) |

Happened-before joins support temporal filters on the joined side: `First`, `MostRecent`, `FirstN`, and `MostRecentN` restrict which tuples from the joined query participate (e.g. join to the *first* client-protocol event in the same request's execution, not every one).

The language's key contribution over conventional monitoring query APIs is the happened-before join (⋈): it gives visibility into **relationships between events** across processes and tiers, not just independent aggregations at each tracepoint. Pivot Tracing is designed to efficiently support happened-before joins specifically; it does not optimize general equijoins.

Queries compile to [advice](pivot-tracing-advice.md) — an intermediate representation specifying operations at each tracepoint — which agents weave into running code at query installation time. See [Pivot Tracing](pivot-tracing.md) for the end-to-end dynamic monitoring flow.
