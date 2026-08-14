---
type: concept
title: Pivot Tracing Query Optimizations
description: Pivot Tracing reduces monitoring cost by performing intermediate local aggregation before global emission and by rewriting queries to push projection, selection, and aggregation close to source tracepoints, minimizing tuples packed in baggage.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §4"
---

[Pivot Tracing](pivot-tracing.md) optimizes along two cost metrics: tuples emitted for global aggregation, and tuples packed in [baggage](pivot-tracing-baggage.md) during a request's execution.

**Local intermediate aggregation:** for queries containing `Aggregate` or `GroupByAggregate`, emitted tuples are aggregated within each process; results are reported globally at a regular interval (default: once per second). Worked example: a cross-tier disk attribution query (Q2) drops from ~600 tuples/second to ~6 tuples/second per DataNode.

**Query rewrite rules:** projection, selection, and aggregation terms are pushed as close as possible to source [tracepoints](pivot-tracing-tracepoints.md), following distributive-operation optimizations Fay outlined for merging tuple streams. Rewrite rules for [happened-before joins](happened-before-join.md) include (where `Combine` is an aggregator's combiner function, e.g. `Sum` for `Count`):

- `Π_{p,q}(P ⋈ Q)` → `Π_p(P) ⋈ Π_q(Q)`
- `σ_p(P ⋈ Q)` → `σ_p(P) ⋈ Q`
- `σ_q(P ⋈ Q)` → `P ⋈ σ_q(Q)`
- `A_p(P ⋈ Q)` → `Combine_p(A_p(P) ⋈ Q)`
- `GA_p(P ⋈ Q)` → `G_pCombine_p(GA_p(P) ⋈ Q)`
- `GA_q(P ⋈ Q)` → `G_qCombine_p(P ⋈ GA_q(Q))`
- `G_pA_q(P ⋈ Q)` → `G_pCombine_q(Π_p(P) ⋈ A_q(Q))`
- `G_qA_p(P ⋈ Q)` → `G_qCombine_p(A_p(P) ⋈ Π_q(Q))`

Pivot Tracing does not inherently bound packed tuple count — a query could accumulate a new tuple per tracepoint invocation, analogous to a database query risking a full table scan. In practice, aggregation operators restrict propagated tuples, and queries typically propagate only aggregations, most-recent, or first tuples. See [in-kernel aggregation over event streaming](in-kernel-aggregation-over-event-streaming.md) for the same push-aggregation-closer-to-source principle in eBPF contexts.
