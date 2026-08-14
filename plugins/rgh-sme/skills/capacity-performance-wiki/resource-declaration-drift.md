---
type: concept
title: Resource Declaration Drift
description: Engineer-supplied CPU and memory declarations for scheduled workloads drift from actual usage as programs evolve, silently consuming the slack meant for spikes and outages until an incident exposes the gap.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 27"
---

In a [bin-packed, scheduler-managed fleet](multitenancy-bin-packing-motivation.md), each program declares resource requirements (CPU, RAM, disk) that the scheduler uses for placement and limits. Early Borg-era scheduling (circa 2006) relied entirely on engineer-supplied replica counts and these declarations — but **humans are bad at estimating** resource needs, the cost of determining correct numbers scales with the number of services in the organization, and programs typically **grow organically** over their lifetime.

The result is **resource declaration drift**: the declared configuration stays static while actual usage creeps upward. The gap is invisible until an outage or spike exposes that the slack provisioned for bursts and failures has already been eaten by normal growth.

## Why Drift Is a Capacity Problem

*   **False headroom.** Dashboards showing "40% of declared CPU used" look healthy while actual need has grown to 90% of what the program truly requires — the remaining 60% "declared slack" was never real.
*   **Bin-packing lies.** The scheduler packs replicas assuming declarations are accurate; under-declared programs become [noisy neighbors](container-multitenancy-noisy-neighbor.md); over-declared programs strand capacity on every host they occupy (see [fleet rightsizing bin-packing](fleet-rightsizing-squeeze-optimize-migrate.md)).
*   **Outage-triggered discovery.** Drift is often found only when redundancy or spike capacity is needed and isn't there — the worst time to discover a sizing error.

## Mitigation: Automated Rightsizing

Automating rightsizing — observing actual usage and adjusting declarations — is "surprisingly tricky to do well" (some workloads resist one-size-fits-all automation), but at Google's scale it had reached the point where automation determined resource usage for **more than half of total fleet resource consumption**, meaning a majority of configurations no longer required hand-tuning. See [automated rightsizing at scale](automated-rightsizing-at-scale.md) for the scope and limits of that automation.

Manual rightsizing workflows ([squeeze, optimize, migrate](fleet-rightsizing-squeeze-optimize-migrate.md)) remain necessary for workloads too complex for automated sizing — the principle is "easy things should be easy, complex things should be possible," not "automate everything."

## Practical Discipline

*   **Treat declarations as living data**, not install-time constants — revisit on every significant traffic or code-path change.
*   **Measure actual usage vs. declared limits** per replica, not just aggregate fleet utilization.
*   **Reserve explicit slack** for spikes and failures separately from "room left in the declaration" — if organic growth consumes declaration headroom, redundancy headroom disappears silently.
