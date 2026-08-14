---
type: concept
title: Energy as a Capacity Resource
description: Power draw behaves like any other finite, costed resource — it needs the same measure-allocate-reduce-demand discipline as CPU or memory, and in mobile/IoT contexts it can be the binding constraint rather than an afterthought.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 6"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Energy is a real, finite, costed resource, not an unlimited utility sitting outside the capacity model — data centers collectively draw on the order of several percent of global electricity, and cooling cost alone has driven decisions as extreme as siting data centers underwater or in arctic climates. Treating power draw with the same discipline as CPU, memory, or network capacity (rather than as an operational afterthought) is directly in scope for capacity planning, not just facilities management.

## Same Discipline, Different Resource

The management approach mirrors the [USE method](use-method.md)'s measure-then-act discipline, applied to power instead of utilization/saturation/errors:

*   **Measure it before managing it.** Fine-grained metering (per-server or per-rack power draw) is the direct analogue of resource-level utilization metrics; where direct measurement isn't available (for example, on a cloud platform with no metering API), consumption must be estimated from published hardware specs or from a model trained against observed workload characteristics — the same fallback posture as estimating a resource's cost when it can't be directly instrumented.
*   **Allocate deliberately.** Consolidating workloads onto fewer physical hosts and powering down the freed hardware is the energy-domain instance of the same consolidation logic behind [fleet rightsizing](fleet-rightsizing-squeeze-optimize-migrate.md) — both are cases of eliminating provisioned-but-idle capacity rather than accepting it as a fixed cost.
*   **Reduce demand, not just supply.** The demand-side levers — capping event/request rates, prioritizing important work over low-value work, reducing per-request computational overhead — are the identical [performance tactics](throughput-vs-latency-tradeoff.md) used to control latency and throughput; reducing the amount of work a system does lowers both its resource footprint and its energy draw at the same time, so this is a case where the capacity and cost objectives point the same direction rather than trading off.

## When Energy Is the Binding Constraint

Cloud and on-premises capacity planning almost always treats energy as a cost signal to optimize, not a hard ceiling — the trade is against money and environmental impact, not against the system simply running out of power. Mobile and IoT contexts invert this: battery capacity is a hard, non-negotiable ceiling with no path to "just add more," so a design choice there is genuinely a energy-vs-performance or energy-vs-usability trade, not a cost-optimization exercise. One specific lever unique to this constrained context is **offloading computation to the cloud when the energy cost of communicating the request is lower than the energy cost of computing the answer locally** — the mobile-side analogue of choosing where a computation happens based on the true cost of each option rather than assuming local execution is always cheaper.

Large accelerator-dense clusters (e.g., GPU-heavy training/inference fleets) push cloud-side capacity planning back toward the "hard ceiling" end of this spectrum rather than the pure cost-optimization end: a single high-end accelerator can draw several thousand kWh per year at sustained peak, and siting a large enough cluster runs into genuine electricity-supply, grid-speed, and geopolitical constraints — not just a price to pay. This creates a direct trade against latency: remote regions with cheaper or more available power are often worse-connected, a real cost for latency-sensitive workloads specifically, distinct from the usual capacity-vs-cost calculus.

## Estimating Power Draw Without Direct Metering

When per-device metering isn't available, hardware datasheets typically publish two figures that bound the estimate: **TDP** (thermal design power — the heat a cooling system must dissipate under a *typical* workload, an expected-draw indicator rather than an exact power measurement) and **maximum power draw** (peak draw under full sustained load). For CPUs and GPUs, maximum power draw is typically **1.1–1.5× TDP**, varying by architecture and workload — a usable estimation range when a device's real-time power isn't directly observable, the same estimate-from-specs fallback described above for consumption modeling in general.
