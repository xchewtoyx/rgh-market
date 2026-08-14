---
type: concept
title: Hotspotting
description: A capacity failure mode where a workload pattern concentrates load onto a single resource instance (one worker, one record, one disk) instead of spreading it evenly across the available pool.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 13"
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 6"
---

**Hotspotting** occurs when a workload's access pattern concentrates load onto a single unit of a resource pool rather than distributing it evenly, so that one unit saturates while the rest of the pool has spare capacity. It is a distribution problem, not a total-capacity problem — the aggregate pool may have plenty of headroom while the hot unit is completely saturated.

## Common Causes

*   **Many workers hitting one serving task** — a shared coordinator, a single partition owner, or a popular shard that receives disproportionate traffic.
*   **CPU exhaustion on the machine holding a "hot" record** — a single frequently-updated or frequently-read key that all requests funnel through.
*   **Disk-head contention** on a single spinning disk from concurrent access patterns that aren't sequential (mitigated by moving to SSDs, which have no seek penalty).
*   **An oversized single work unit** in a batch or pipeline system — one unit of work large enough that it dominates its assigned worker's processing time regardless of how many workers are available.
*   **Monotonically increasing partition keys** — e.g. a timestamp-prefixed key in a range-partitioned data store. All writes for "now" fall into the same key range, so every current write lands on whichever single partition owns that range, even though older ranges (and the partitions serving them) sit idle. Prefixing the key with a more evenly distributed field (an entity or shard ID) before the timestamp spreads writes back across partitions.

## Why It's Distinct From Ordinary Saturation

Ordinary [resource saturation](use-method.md) means the aggregate demand exceeds aggregate capacity. Hotspotting means aggregate capacity is sufficient, but the workload's access pattern (not its volume) prevents that capacity from being reached by the units that need it — the fix is redistribution, not just adding more units, because adding more units to a pool that isn't being evenly used doesn't relieve the hot one.

## Mitigations

*   **Fine-grained blocking or skipping** of specific problematic records or work units, so one bad hotspot doesn't stall the whole pipeline.
*   **Restructure access patterns** to spread load across more keys/partitions (e.g., adding a randomized suffix to a hot key to split it across multiple physical partitions). This shifts cost rather than eliminating it: writes to the hot key now distribute across the split copies, but a read of the *logical* key must scatter the request across all of the split copies and gather the results, which trades a write-side hotspot for read-side [tail latency amplification](tail-latency-amplification.md) — worthwhile when writes dominate, but not free.
*   **Dynamic rebalancing** of work units across the pool as hotspots are detected, rather than relying on a static assignment made before the hot pattern emerged — but rebalancing is itself a load event, and fully automating it risks an [automated rebalancing failure cascade](automated-rebalancing-failure-cascade.md) if it's triggered too eagerly.
*   **Reduced lock granularity** so contention on a shared resource doesn't serialize work that doesn't actually need to be serialized.
*   **Retain an emergency shutdown/skip mechanism** for a specific bad record or pattern, so an operator has a fast way to stop a known hotspot from continuing to damage the system while a proper fix is developed.

This is a workload-shape problem that [autoscaling](autoscaling-safety-bounds.md) alone cannot fix — adding instances to the pool doesn't help if the routing that creates the hotspot doesn't change, the same limitation that applies to autoscaling a stateful system with poor task routing, discussed under [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md).
