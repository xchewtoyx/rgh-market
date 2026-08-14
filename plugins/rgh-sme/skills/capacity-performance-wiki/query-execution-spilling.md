---
type: concept
title: Query Execution Spilling
description: When a query operator's working set exceeds its allocated compute memory, the engine spills intermediate results to local disk and then to remote storage, silently converting an in-memory operation into a much slower one while still billing for the same compute.
sources:
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 12"
---

Analytical query engines (data warehouses, Spark, and similar systems) execute operators like sorts, joins, and aggregations by holding their working set in the compute node's memory. When that working set exceeds available memory, the engine doesn't fail the query — it **spills**: it writes the excess intermediate data to local disk first, and if local disk also fills, to remote network storage.

## Why It's Worse Than It Looks

Spilling is a doubly costly failure mode, not just a slower path: the query still consumes (and is billed for) the full compute allocation it was given, but its actual throughput drops to disk — or worse, network-storage — speeds for the spilled portion of the work. A query that spills to remote storage can take an order of magnitude longer than the same query run with enough memory to stay fully in-memory, while consuming compute capacity for that entire extended duration. This makes spilling a case where [resource saturation](use-method.md) on one dimension (memory) manifests as a latency and cost problem on a completely different dimension (compute time), which can make the root cause easy to miss if only compute utilization is being watched.

## Diagnosis

Query profiling/execution-plan tools typically expose spilling as a distinct diagnostic category, separate from raw execution time — look specifically for a query stage reporting bytes spilled to local or remote storage, not just elapsed time, since a spilling query can otherwise look like an ordinary slow query with no obvious cause.

## Mitigations

*   **Increase the memory allocated to the query** (a larger compute instance/cluster size) — the direct fix, trading cost for headroom, following the same [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) logic as any other resource-bound workload.
*   **Reduce the working set the operator has to hold at once** — filter or aggregate data down before the memory-intensive step, rather than after, so less data ever needs to be materialized in memory for the expensive operator.
*   **Break one large operation into staged, smaller ones**, deliberately materializing an intermediate result (a temporary table, or a cached prior query's result set) so that a later stage only has to hold its own, smaller working set in memory rather than the whole computation's cumulative footprint at once — bounding each stage's resource footprint by breaking a monolithic operation into sequential pieces, even though the total data processed doesn't change.

Because spilling is a memory-capacity problem wearing a performance-problem disguise, sizing a workload's compute purely from CPU or throughput benchmarks without validating peak memory usage under real data volumes will systematically underestimate what a query actually needs — see [benchmarking pitfalls](benchmarking-pitfalls.md) for the broader class of measurement gaps this belongs to.
