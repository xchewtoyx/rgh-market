---
type: concept
title: Scale-Driven Architecture Selection
description: The size of the data corpus and the number of concurrent users determine which search or query architecture is viable — from brute-force scan through local index to distributed cloud service — and picking the wrong tier wastes resources or fails outright.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 19"
---

For search, lookup, and scan workloads, **corpus size is the primary driver** of which architecture can meet a [latency budget](throughput-vs-latency-tradeoff.md). The viable options form a tiered ladder:

| Corpus scale | Typical approach | Why |
| :--- | :--- | :--- |
| Megabytes | Brute-force scan (e.g., grep) | Scanning the whole corpus fits in memory and completes within interactive latency. |
| Hundreds of megabytes | Simple local index on one machine | A pre-built index avoids full scans while staying on a single host. |
| Gigabytes to terabytes | Distributed, multi-machine index | Neither brute force nor a single-node index can serve concurrent queries at [interactive latency thresholds](interactive-latency-thresholds.md). |

The same pattern applies beyond code search: any workload whose naive implementation requires scanning the full dataset per query will hit a **brute-force capacity ceiling** long before the data reaches "big data" scale. A back-of-envelope at Google's Code Search scale (~1.5 TB indexed, ~200 queries/sec, ~50 ms server-side budget) illustrates the cliff: regex matching at ~100 MB/sec in RAM would need on the order of hundreds of thousands of CPU cores to scan the full corpus within the latency window under concurrent load — making indexing mandatory, not optional.

## User Count Amplifies the Requirement

The utility of a centralized, heavily optimized solution grows with both corpus size **and** the number of developers (or users) sharing it — each additional user multiplies query volume without multiplying the per-query engineering cost of the shared backend. A architecture that is overkill for a solo developer on a small repo becomes necessary when thousands of developers share a terabyte-scale monorepo.

## Capacity Planning Takeaway

When forecasting growth, treat the transition between tiers as a **step change in system complexity and fixed cost**, not a smooth extrapolation of the current design. Crossing from "local index suffices" to "distributed index required" is closer to a replatforming event than to adding another server — plan headroom against the next tier's architecture, not just the next increment of the current one. See [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) for the broader scaling-strategy context once a distributed tier is in play.
