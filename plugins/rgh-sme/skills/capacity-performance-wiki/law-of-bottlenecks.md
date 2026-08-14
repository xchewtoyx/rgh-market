---
type: concept
title: Law of Bottlenecks
description: Relieving a system's current bottleneck does not eliminate bottlenecks — it moves the constraint to whichever resource is next most limiting, so capacity work is never "done," only relocated.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 8"
---

In any system decomposed into subsystems (CPU, memory, disk, network, a downstream service, a lock), there is always some resource that constrains overall throughput most tightly at the current load level. Adding capacity to that resource, or optimizing it away, does not remove the constraint from the system — it simply reveals whichever resource was the *next* most limiting one, which then becomes the new bottleneck, possibly at a different, higher load level than the first.

## Practical Implications

*   **A capacity investigation never has a final answer, only a current one.** "We fixed the bottleneck" is only true relative to today's load and today's architecture; it should be read as "we moved the bottleneck," not "we eliminated bottlenecks."
*   **Forecasts that assume a fixed bottleneck resource are fragile.** A statistical capacity model built entirely around the currently-dominant resource (e.g. assuming a workload will remain CPU-bound throughout a forecast horizon) has no way to anticipate a different resource becoming limiting once the current one is relieved — see [fitting the Universal Scalability Law to data](fitting-universal-scalability-law-to-data.md) and [effective demand](effective-demand.md) for two forecasting techniques that share this same blind spot.
*   **This motivates re-running capacity analysis after every significant capacity change**, not just before it — the bottleneck identified pre-change is not reliably the bottleneck post-change, even if the change was specifically targeted at that resource.

This principle generalizes the single-resource reasoning of the [USE method](use-method.md) and [resource vs. workload perspectives](resource-vs-workload-perspectives.md) into an ongoing process rather than a one-time diagnosis: identifying and relieving the current bottleneck is necessary but never sufficient — it's one iteration of a loop that keeps running as long as the system keeps growing.
