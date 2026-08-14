---
type: concept
title: "Fleet Rightsizing: Squeeze, Optimize, Migrate"
description: A rightsizing effort should exhaust cheap, low-risk levers — shrinking allocations, raising autoscaling targets — before spending engineering effort on code optimization or architecture migration.
sources:
  - title: "Observability Engineering, 2nd Edition"
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 20"
---

When a fleet is over-provisioned relative to its real workload, the highest-leverage rightsizing work is usually not the most technically interesting work. A useful ordering, from least to most effort, is **squeeze, then optimize, then migrate**.

## Squeeze

Shrink per-task CPU/memory allocations and raise autoscaling targets until latency actually starts to degrade, verified empirically rather than assumed from a rule of thumb. Old utilization guidelines (e.g., a fixed safe-CPU-utilization percentage for a given CPU generation) can be stale — hardware, hyperthreading behavior, and workload shapes all change — so re-test the ceiling on current hardware rather than reusing an inherited number. This is the cheapest lever: it costs no engineering time beyond measurement and configuration, and it directly reduces the gap between provisioned and [actually used capacity](capacity-headroom-safety-margin.md).

## Optimize

Once allocations are squeezed, look for shared bottlenecks that generalize across many workloads at once — OS, kernel, or common-library code paths that many services all pay for redundantly — rather than optimizing one service's application code in isolation; a fix at that shared layer pays off fleet-wide instead of once. This is also where hardware-generation migration belongs (e.g., moving to a newer CPU architecture that offers a meaningful price-performance step): it is still comparatively low-risk (the workload's code doesn't change) but requires validating compatibility and re-measuring the safe-utilization ceiling on the new hardware.

## Migrate

Only once squeeze and optimize are exhausted does it make sense to consider migrating a workload's architecture entirely — e.g., moving a component between [compute purchasing models](compute-purchasing-model-spectrum.md) (VM to elastic container to serverless). This is the highest-effort, highest-risk lever, since it usually involves re-architecting how the workload holds state and handles cold starts, so it should be justified by data (observed utilization, concurrency patterns) rather than attempted first out of an assumption that a different platform is inherently more efficient.

## Bin-Packing and Stranded Capacity

A rightsizing effort that only tunes allocation size without checking how allocations *pack* onto underlying hosts can still leave capacity stranded. If a workload's per-task allocation doesn't divide evenly into a host's total capacity, the remainder goes unused: a task sized to consume 20 of a host's 32 cores strands roughly 11–12 cores that are too small to fit another instance of that same task. Fixing this requires either resizing the task to pack cleanly against the host size, or resizing the host to be a clean multiple of the task — a squeeze-phase fix that pure per-task utilization metrics alone won't reveal, since it's a property of how allocations tile onto hosts, not of any single task's own efficiency. Shared infrastructure overhead (security agents, log collectors, storage drivers running as sidecars or daemons on every host) also needs to be counted against available capacity when doing this packing math, since it silently narrows how much room is actually left for workload tasks.
