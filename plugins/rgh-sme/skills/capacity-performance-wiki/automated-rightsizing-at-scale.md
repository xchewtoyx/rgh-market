---
type: concept
title: Automated Rightsizing at Scale
description: Observing actual workload resource consumption and automatically adjusting declared CPU, memory, and replica counts can remove manual sizing toil for the majority of fleet configurations, though complex workloads still need human tuning.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 27"
---

Manual [resource declarations](resource-declaration-drift.md) (replica counts, CPU, RAM, disk) do not scale with organization growth: estimating requirements is error-prone, the cost of correct estimation grows with service count, and declarations drift from reality as programs evolve. **Automated rightsizing** closes the loop by measuring actual consumption and adjusting allocations — but doing it well is harder than it appears.

## What "At Scale" Looks Like

At Google/Borg, automated rightsizing had reached the point where automation determined resource usage for **more than half of total fleet resource consumption** — not a minority experiment, but the majority of configurations where engineers no longer hand-tuned sizing. That threshold matters for capacity planning: once automated sizing covers most of the fleet, the organization's capacity model shifts from "sum of engineer guesses" to "sum of observed usage plus policy margins."

## Why It's Tricky

*   **Workload diversity.** Batch jobs, latency-sensitive serving, stateful databases, and GPU workloads have incompatible sizing signals — one automation policy cannot fit all.
*   **Spike and failure headroom.** Naive automation that sets declarations equal to average usage eliminates the slack needed for bursts, rolling deploys, and node loss — the same [capacity headroom](capacity-headroom-safety-margin.md) problem as manual drift, approached from the opposite direction.
*   **Feedback loops.** Aggressive down-sizing based on recent low-traffic windows can leave a service under-provisioned when traffic returns; aggressive up-sizing during a spike can lock in over-provisioned declarations permanently.

## Relationship to Other Levers

Automated rightsizing is the fleet-scale counterpart to [efficiency investment vs. resource cost](efficiency-investment-vs-resource-cost.md): it reduces ongoing waste from mis-declared capacity without requiring each team to run a manual [squeeze-optimize-migrate](fleet-rightsizing-squeeze-optimize-migrate.md) cycle. It does not replace architecture-level changes (moving between [compute purchasing models](compute-purchasing-model-spectrum.md)) when the workload shape itself is wrong.

For workloads automation handles poorly, manual rightsizing and explicit [load testing](self-serve-load-test-tooling.md) remain necessary — automation covering the common case is valuable even when it cannot cover every configuration.
