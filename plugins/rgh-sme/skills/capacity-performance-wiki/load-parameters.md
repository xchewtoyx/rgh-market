---
type: concept
title: Load Parameters
description: The quantitative, system-specific measures used to characterize workload demand as an input to capacity models and load tests.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
---

**Load parameters** are the numbers chosen to describe how much demand a system is under. There is no universal set of load parameters — which ones matter depends on the system's architecture and the resource most likely to become a bottleneck under growth.

## Choosing Load Parameters

Typical examples include:

*   Requests per second to an application server.
*   The ratio of reads to writes in a database workload.
*   The number of simultaneously active users in a chat room or collaborative session.
*   The hit rate of a cache.

The right choice is architecture-dependent: a system dominated by fan-out writes cares about follower/subscriber counts per write, while a system dominated by read joins cares about query complexity and read volume. Picking the wrong load parameter produces a capacity model that looks healthy right up until the dimension nobody measured becomes the bottleneck.

## Use in Capacity Engineering

Load parameters are the independent variable in two related activities:

*   **Capacity modelling:** projecting how resource consumption (CPU, memory, storage IOPS, network bandwidth) grows as a load parameter increases, to forecast when headroom runs out.
*   **[Load testing](capacity-test-types.md):** driving a system with synthetic traffic that varies one load parameter at a time (e.g., doubling requests per second, or skewing the read/write ratio) to find the point at which a specific resource saturates. See [load generator bottlenecks](load-generator-bottlenecks.md) for a pitfall that can invalidate this kind of test.

A single load parameter rarely tells the whole story — see [heavy-tailed load skew](heavy-tailed-load-skew.md) for how the *distribution* of a load parameter (not just its average) can determine which capacity strategy actually works.

## Composition Shift Can Break a Capacity Model Even at Constant Volume

A capacity model built around a load parameter's *volume* (requests/sec, records/day) can still be blindsided by a change in that load's *composition* — the mix of distinct work types within the same volume — if different work types carry different per-unit resource cost. A batch pipeline sized for "N events/night" can develop a real capacity shortfall purely because the share of a more expensive event subtype (one requiring an extra lookup or join the cheaper subtype doesn't) grows over time, even while total event volume stays flat or grows only slowly. The symptom is easy to misdiagnose: the bottleneck resource (e.g., CPU) appears to be running out, when the actual cause is a downstream dependency (e.g., a lookup data store) that the growing expensive subtype now hits proportionally more often — CPU looks saturated because it's waiting on that dependency's response, not because it needs more raw compute. Tracking a workload's *mix* of request/record types as its own load parameter, not just its total volume, is what catches this before it's mistaken for the wrong resource running out.
