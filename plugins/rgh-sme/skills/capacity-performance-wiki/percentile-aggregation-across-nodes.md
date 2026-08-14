---
type: concept
title: Percentile Aggregation Across Nodes
description: Percentiles cannot be averaged; combining latency measurements from multiple servers or time windows requires merging histograms or streaming percentile estimators instead.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

A common mistake in monitoring fleets of servers is to compute a percentile (e.g., p99) independently on each node, then average those per-node percentiles to get a "fleet-wide p99." **This is not a valid aggregation.** The average of several p99 values is not the p99 of the combined population — it has no defined statistical meaning, and it can be badly wrong in either direction depending on how load and latency are distributed across nodes.

## Why Averaging Fails

Percentiles are non-linear order statistics. Two nodes can each report a p99 of 100ms while the combined population's true p99 (computed over every individual request across both nodes) is significantly higher or lower, depending on how many requests each node handled and the shape of each node's underlying distribution. There is no way to reconstruct that from the two summary numbers alone.

## Correct Approaches

To get a statistically valid combined percentile, [latency percentiles](latency-percentiles-vs-mean.md) must be aggregated from something richer than a single summary number per node:

*   **Merge exact histograms.** If every node records a full histogram of response-time buckets, the histograms can be summed bucket-by-bucket before computing the percentile on the merged result.
*   **Use a mergeable streaming estimator.** Structures such as **t-digest**, **HdrHistogram**, or **forward decay** are designed to be computed incrementally per node with bounded memory, and then merged across nodes (or time windows) while preserving accurate percentile estimates — without needing to retain every individual latency sample.

Either approach requires deciding on the aggregation mechanism *before* collecting the data — a bare per-node percentile, once computed, cannot be un-computed back into a form other nodes' results can be validly combined with.
