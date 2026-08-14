---
type: concept
title: Pivot Tracing Advice
description: Advice is Pivot Tracing's compiled intermediate representation — a fixed set of tuple-manipulation operations (Observe, Unpack, Filter, Pack, Emit) installed at tracepoints to execute a query's logic at runtime without recompiling the target system.
sources:
  - title: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems"
    resource: "Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems (Mace, Roelke, Fonseca), §3"
---

When an operator submits a [Pivot Tracing query](pivot-tracing-query-language.md), the compiler produces **advice** — an intermediate representation specifying the operations to perform at each [tracepoint](pivot-tracing-tracepoints.md) used in the query. Advice eventually materializes as the monitoring code agents install at those tracepoints. Advice operations:

| Operation | Role |
|---|---|
| `Observe` | Construct a tuple from variables exported by a tracepoint |
| `Unpack` | Retrieve one or more tuples produced by prior advice along the causal chain |
| `Filter` | Evaluate a predicate on all tuples |
| `Pack` | Make tuples available for use by later advice (via [baggage propagation](context-propagation.md)) |
| `Emit` | Output a tuple for global aggregation |

`Pack` and `Emit` can group tuples by matching fields and perform simple aggregations (`Sum`, `Count`). `Pack` has temporal variants: `First` packs the first tuple and ignores subsequent ones; `Recent` overwrites with the most recent; `FirstN`/`RecentN` generalize to N tuples. Advice code has no jumps or recursion and is guaranteed to terminate.

**Worked example** — a cross-tier disk attribution query compiles to:

- **A1** at `ClientProtocols`: `Observe procName; Pack-First procName`
- **A2** at `DataNodeMetrics.incrBytesRead`: `Observe delta; Unpack procName; Emit procName, Sum(delta)`

A1 captures the upstream process name once; A2 unpacks it when bytes are recorded, emitting per-caller totals.

**Compilation procedure:** instantiate one advice specification per `From` clause; add `Observe` for each tracepoint variable referenced. For each `Join` clause, add `Unpack` for variables from the joined query, recursively generate advice for that query, and append `Pack` at its end for the unpacked variables. `Where` → `Filter`; output variables → `Emit` (respecting `Select`); `Aggregate`/`GroupBy`/`GroupByAggregate` → handled by `Emit` and `Pack`.

Agents **weave** advice into tracepoints by: (1) loading code implementing the advice operations; (2) configuring the tracepoint to execute that code with its exported variables; (3) activating the tracepoint at all relevant locations in the system.
