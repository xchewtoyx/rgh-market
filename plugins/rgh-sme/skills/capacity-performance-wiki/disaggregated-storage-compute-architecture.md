---
type: concept
title: Disaggregated Storage-Compute Architecture
description: Separating a data platform's storage tier from its compute tier lets each be sized and scaled independently, avoiding the contention-versus-tunability trade-off forced by older shared-disk and shared-nothing designs.
sources:
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 3"
---

Data platforms have historically forced a choice between two capacity-constrained architectures:

* **Shared-disk architecture** centralizes storage and exposes it to multiple independent compute clusters over a network. Compute clusters can be sized independently per workload, but every cluster contends for the same central disk — the most important resource in the system becomes the shared bottleneck, and adding more compute capacity makes the contention worse, not better.
* **Shared-nothing architecture** gives each compute cluster its own attached disk, eliminating that central contention point. The cost: because storage is physically tied to a specific cluster, storage and compute can't be sized independently — a workload needing heavy compute against a small dataset (e.g., data science) and a workload needing heavy I/O against a large dataset (e.g., bulk ETL) can't each get the resource mix they actually need without over-provisioning the other dimension. Clusters also have to transfer data between each other to share information, adding a network-bound latency cost shared-disk designs don't pay.

## The Disaggregated Alternative

Modern cloud-native platforms (Snowflake is the example this note draws on) resolve the trade-off by physically keeping data on disk but **logically separating the storage layer from the compute layer**, so compute clusters get centralized-storage access without the shared-disk contention penalty:

* **Storage layer** — billed and scaled purely on data volume, independent of how much compute is provisioned. No capacity planning is needed on this axis beyond monitoring total stored volume.
* **Compute layer** — independently provisioned clusters (Snowflake calls them warehouses) that read from the same shared storage. Because compute is decoupled from storage, a cluster can be sized for its specific workload's CPU/memory needs without that choice affecting or being constrained by how much data exists.

This is the practical resolution of the [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) trade-off applied to a specific capacity problem: it adds a **third scaling axis** (which resource tier to scale) on top of the usual up/out choice, letting a platform decouple "more data" from "more query capacity" entirely — a workload that needs more compute doesn't force paying for more storage, and vice versa.

## Two Ways to Scale the Compute Tier

Once compute is its own independently-provisioned tier, the same two directions from [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) reappear at the cluster level, with clean, cost-linear semantics:

* **Scale up** — resize a cluster to a larger size class; each step up roughly doubles both its resource count and its cost. Improves the speed of a single workload's queries.
* **Scale out** — add more clusters of the same size rather than growing one cluster. Improves *concurrency* — more simultaneous workloads can run without queueing behind each other — without changing any single query's individual speed.

Because these are independent levers, a capacity plan can target latency (scale up) and throughput/concurrency (scale out) separately, rather than being forced to over-provision one to get more of the other — the same distinction as [throughput vs. latency trade-off](throughput-vs-latency-tradeoff.md), but resolved here by adding capacity along the axis that actually matches the bottleneck rather than picking one lever for both problems.
