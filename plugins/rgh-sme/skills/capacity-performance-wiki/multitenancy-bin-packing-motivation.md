---
type: concept
title: Multitenancy Bin-Packing Motivation
description: Running one dedicated machine per program wastes capacity when job types outnumber machine types, acquisition is slow, and fleets grow heterogeneous — declaring resource requirements and bin-packing replicas onto a shared pool recovers utilization.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 27"
---

A **one-machine-per-program** model is workable at small scale (SSH in, compile, run) but wastes resources as an organization grows along three axes: number of distinct applications, replicas per application, and size of the largest application.

## Why Dedicated Machines Waste Capacity

*   **Job types outnumber machine types.** Machines get provisioned for the largest job they might host, so most programs run on hardware sized for someone else's peak.
*   **Slow machine acquisition.** When adding capacity takes weeks, teams [over-provision ahead of growth](capacity-headroom-safety-margin.md) rather than risk being blocked on hardware during a demand spike.
*   **Heterogeneous fleet persistence.** Old and new machine generations coexist; the fleet doesn't self-adapt to current workload shapes, leaving stranded capacity on mismatched hosts — the same [bin-packing and stranded capacity](fleet-rightsizing-squeeze-optimize-migrate.md) problem rightsizing later tries to fix.

## The Bin-Packing Alternative

Specify each program's resource requirements (CPU, RAM, disk) and let a **central scheduler** pack replicas onto a shared machine pool. This replaces hand-maintained "sign-up files" throttling who may use which machines with automated placement on unoccupied capacity.

The scheduler becomes the turning point in compute-environment automation: after deployment automation, monitoring, and self-healing, **automated scheduling** is what makes hundreds or thousands of machines operable without per-job human logistics.

## Capacity Planning Implications

*   **Declared requirements are the scheduling input.** Bin-packing quality depends on accurate CPU/RAM/disk declarations — inaccurate declarations cause either wasted slack (over-declaration) or [noisy-neighbor contention](container-multitenancy-noisy-neighbor.md) (under-declaration).
*   **Growth is multi-dimensional.** Forecasting must cover application count, replica count per application, and maximum single-application size — not just aggregate CPU-hours.
*   **New resource types arrive over time.** GPU/TPU scheduling, for example, was a major addition to Google's Borg scheduler long after initial deployment — capacity platforms must evolve their requirement types as workloads change.
