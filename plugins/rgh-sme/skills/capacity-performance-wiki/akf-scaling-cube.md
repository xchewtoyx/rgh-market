---
type: concept
title: AKF Scaling Cube
description: Three orthogonal ways to add capacity to a system — replicating the whole thing, splitting by function, or splitting by data — that combine rather than compete, and that fail in different ways depending on how much coordination the split requires.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 5"
---

The **AKF Scaling Cube** (Abbott, Keeven, Fisher) organizes every way of adding capacity to a system into three independent axes, which combine rather than substitute for each other:

*   **X-axis — horizontal duplication ("scale out"):** replicate the whole system and spread load across the copies — the [horizontal scaling](horizontal-vs-vertical-scaling.md) pattern. Scales close to linearly *only* when replicas can complete transactions independently; it scales worse the more replicas must coordinate with each other (a write that must propagate to every replica before a related transaction can proceed is the limiting case, directly tied to the [CAP trade-offs](horizontal-vs-vertical-scaling.md) inherent in replicated state).
*   **Y-axis — functional/service split:** split *distinct functions* onto dedicated resource pools instead of replicating the whole monolith — this is [functional partitioning](horizontal-vs-vertical-scaling.md). This isn't limited to subsystems; it applies just as well to *transaction types* — isolating latency-sensitive interactive traffic from latency-tolerant batch traffic, or isolating a rare-but-expensive transaction type onto its own pool so it doesn't degrade a shared cache or connection pool for everyone else — and to *user types*, routing a small high-value segment to a dedicated pool sized and tuned differently from the general population.
*   **Z-axis — data/lookup split:** split the *data* rather than the processing — this is [sharding](fixed-partition-count-scaling-ceiling.md). Unlike X-axis replication, each shard holds only a fraction of the total data, so per-shard indices stay small and query load spreads across shards; unlike Y-axis splitting, every shard runs the *same* logic against a different data subset rather than different logic against the same data.

## Why the Order Matters

The three axes have different implementation cost, and that cost ordering drives a practical sequencing rule: X-axis replication is usually cheapest to add (no application changes, just more copies behind a load balancer); Y-axis splitting requires loosening coupling between the parts being separated, but is still a bounded, one-time refactor; Z-axis data splitting is the most invasive, because it usually requires the application itself to become shard-aware (routing every query to the right partition) — a change that's expensive to retrofit once a system has grown up assuming a single, unsplit data store. This is why teams typically exhaust X- and Y-axis options first and reach for Z-axis sharding only once those are no longer enough — not because sharding is technically superior for that stage, but because it's the axis that's hardest to undo a bad early decision about.

## Combining Axes

Real systems blend all three rather than picking one: a segment (Z-axis) that turns out to be disproportionately hot can be replicated (X-axis) more deeply than cold segments, gaining both extra aggregate capacity and better hot-path latency for exactly the part of the data that needs it; replica counts within a segment can then be adjusted dynamically based on observed latency or utilization signals, independent of how other segments are scaled. Choosing where a given bottleneck should be resolved — replicate more, split by function, or split by data — is itself a diagnostic step: see [the law of bottlenecks](law-of-bottlenecks.md) for why that diagnosis has to be repeated after every scaling change rather than done once.
