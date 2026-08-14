---
type: concept
title: Container Multitenancy Noisy-Neighbor Effects
description: When multiple programs share a host via containers, a tenant whose actual resource use exceeds its declared allocation causes CPU latency blips and memory pressure that harm co-located serving jobs — and isolation failures extend beyond CPU and RAM to shared kernel namespaces.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 27"
---

[Multitenancy bin-packing](multitenancy-bin-packing-motivation.md) improves fleet utilization by placing many programs on shared hosts behind declared CPU/RAM/disk requirements. The failure mode is the **noisy neighbor**: a program whose actual usage exceeds its declaration — from a bug, organic growth, or burst traffic — steals resources from co-located tenants.

## CPU and Memory Contention

*   **CPU overuse** causes latency blips in co-located **serving jobs** (interactive, latency-sensitive workloads suffer first). See [container CPU throttling](container-cpu-throttling.md) for how cgroup quotas interact with multi-threaded burst patterns.
*   **RAM overuse** triggers kernel OOM kills or disk-swap latency. Google chose **OOM-kill-and-migrate** over tolerating swap latency for serving workloads — the same [swap vs. OOM-killer trade-off](memory-overcommit.md) applied at fleet scale: slow degradation under swap is worse for latency-sensitive services than fast failure with automated reallocation.

## Isolation Beyond CPU and RAM

Containers (cgroups, namespaces, bind mounts) are lighter than full VMs but isolation gaps keep surfacing:

*   **Conflicting dependency versions** between co-located programs.
*   **Shared system resources** (e.g., `/tmp` space, file descriptors).
*   **Security boundaries** between tenants handling sensitive data.
*   **PID namespace exhaustion** — at Google's Borg, default 32,000 PIDs per replica became an isolation failure mode in 2011, requiring per-replica process/thread limits.

VMs remain the classical strong-isolation answer but carry **heavy overhead** (full OS resource cost, slow boot) — a poor fit for batch jobs needing small footprints and short runtimes, which is why container schedulers (Borg, Kubernetes) became the default for mixed batch-and-serve fleets.

## Capacity and Rightsizing Connection

Noisy-neighbor damage is both a **scheduling enforcement** problem (limits not matching reality) and a **[resource declaration drift](resource-declaration-drift.md)** problem (declared config no longer matches actual growth). Monitoring must detect tenants exceeding allocation before neighbors suffer — cgroup throttling metrics, OOM events, and per-replica resource usage vs. declared requests.

When isolation requirements exceed what containers can guarantee (strong security boundaries, incompatible kernel dependencies), falling back to VM-per-tenant or dedicated nodes trades utilization for isolation — a deliberate [efficiency vs. headroom cost](efficiency-investment-vs-resource-cost.md) choice, not a scheduler bug.
