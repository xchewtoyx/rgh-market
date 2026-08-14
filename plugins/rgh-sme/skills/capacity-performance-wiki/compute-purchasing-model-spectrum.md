---
type: concept
title: Compute Purchasing Model Spectrum
description: Cloud compute options form a spectrum trading developer effort and per-unit cost against utilization efficiency, from owned/reserved capacity through persistent and interruptible VMs to serverless.
sources:
  - title: "Observability Engineering, 2nd Edition"
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 20"
---

Cloud compute is not a binary choice between "own it" and "rent it" — it spans a spectrum of purchasing models, each striking a different balance between how much *idle* capacity you pay for and how much engineering effort is required to use it well.

## The Spectrum

Roughly ordered by increasing [utilization efficiency](utilization-vs-efficiency.md) and increasing required engineering effort:

1.  **Capital expenditure / owned datacenter.** Maximum control, maximum idle-capacity risk — you pay for peak-provisioned hardware whether or not it's in use, and lead time to add capacity is procurement-scale, not minutes.
2.  **Reserved capacity.** A committed, discounted long-term purchase from a cloud provider — cheaper than on-demand in exchange for a utilization forecast you're now committed to, whether or not it holds.
3.  **Persistent defined capacity (always-on VMs).** You pay for the instance whether it's busy or idle; in exchange you can keep warm connections, in-memory caches, and long-lived state that a spun-down instance would lose.
4.  **Interruptible defined capacity (spot instances).** Same VM model, but the provider can reclaim the instance on short notice at a steep discount — appropriate for workloads that tolerate a few minutes of migration/restart.
5.  **Persistent elastic (e.g., managed container platforms).** Scales instance count to load automatically while still holding warm state per instance; less idle waste than a fixed VM fleet, less control than raw VMs.
6.  **Interruptible and fully elastic (serverless / functions-as-a-service).** Pay only for actual execution time — the best achievable utilization — at the highest per-CPU-second unit cost, and with cold-start latency whenever no warm instance is available to reuse.

## The Core Trade-Off

Moving down the list buys near-perfect utilization (you stop paying for idle capacity) at the cost of losing the ability to keep warm state, and at a higher unit price per second of actual compute. Moving up the list buys cheaper compute and persistent warm state at the cost of paying for capacity that sits idle between bursts of work. Neither end is universally correct — it is the same [utilization vs. headroom cost trade-off](efficiency-investment-vs-resource-cost.md) applied to the choice of *how* capacity is purchased, not just how much of it to hold.

## Hybrid Allocation Is Normal

Real systems routinely mix models by component rather than picking one for an entire architecture: a database on persistent VMs (to keep its cache warm and avoid cold-start penalties on a stateful, latency-sensitive resource), a request-serving frontend on serverless or elastic containers (bursty, stateless, tolerates cold starts), and batch/offline processing on interruptible spot capacity (tolerant of restarts, price-sensitive, not latency-critical). The right split is workload-specific, and observed utilization data — concurrent execution counts, per-instance idle time, cold-start frequency — should drive *when* a component migrates from one model to another, rather than the choice being made once at design time and never revisited.

## A Caveat on "Serverless Is Always Cheapest at Low Traffic"

Provisioned concurrency (paying to keep a serverless function's instances warm ahead of traffic) is often the worst of both worlds for a workload sitting at the boundary: it still requires the same manual capacity-planning judgment call as a persistent VM (how many instances to keep warm), it rarely delivers a meaningful cost discount over normal on-demand serverless pricing, and it can't amortize per-invocation setup cost across a long-lived process the way a genuinely persistent instance can. Non-compute costs (e.g., storage read/write request volume) can also come to dominate a serverless workload's total bill, so purchasing-model comparisons need to account for the whole cost surface, not just compute-second pricing.

## Batch and Analytics Workloads

Batch MapReduce-style jobs map differently onto the spectrum than request-serving frontends:

*   **Serverless functions** suit small batch jobs whose **final reduced output fits in one invocation's memory, disk, and time limits** — see [serverless MapReduce capacity limits](serverless-mapreduce-capacity-limits.md). The map phase scales by adding invocations; the reduce phase does not.
*   **Query engines over object storage** (e.g., Athena-style SQL over S3) minimize operational overhead for ad hoc analytics when data is already structured, at the cost of requiring a separate ETL step to extract structure from raw inputs.
*   **Managed batch clusters** (e.g., EMR, Dataproc) charge for cluster uptime rather than per-invocation limits, making them appropriate when [reduce-phase single-node bottlenecks](reduce-phase-single-node-bottleneck.md) exceed FaaS ceilings. On-demand cluster create/destroy via automation approximates serverless economics for intermittent large jobs without giving up Hadoop/Spark-scale shuffle infrastructure.

The migration trigger is usually observed job failure against FaaS limits (reducer timeout, OOM, `/tmp` exhaustion), not arrival rate — the opposite signal from a latency-sensitive online service migrating *toward* serverless for burst utilization.
