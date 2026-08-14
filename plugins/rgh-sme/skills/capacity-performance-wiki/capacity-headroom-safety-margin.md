---
type: concept
title: Capacity Headroom Safety Margin
description: Sizing demand forecasts and load tests with a safety multiplier above the best available estimate, because launch-day and viral demand routinely exceed pre-launch predictions by a wide margin.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 11"
---

**Capacity headroom** is the gap between provisioned capacity and expected peak demand. Because demand forecasts for new or viral products are frequently wrong on the low side — sometimes by an order of magnitude — capacity plans and load tests need an explicit safety margin above the best point estimate, not just the point estimate itself.

## Worked Example

A mobile game's pre-launch load testing targeted 5x the expected traffic as a safety margin — a reasonable-looking buffer. Actual launch traffic hit roughly 50x expected traffic, an order of magnitude beyond what was tested for. The architecture (a regional load balancer with an under-provisioned reverse proxy handling SSL termination and request buffering) had no spare headroom at that scale and became the bottleneck, compounding into a broader incident once true demand was found to be 200% higher than even the revised in-incident estimate.

## Why a Fixed Multiplier Isn't Enough

A safety multiplier chosen once, early, is only as good as the demand model it's applied to. For products where demand is genuinely hard to forecast (viral consumer launches, unpredictable seasonal spikes), even a seemingly generous multiplier can be wrong by an order of magnitude, because the uncertainty in the underlying forecast — not just the multiplier — is what actually needs to be sized for. Point-estimate-plus-multiplier approaches implicitly assume the forecast's uncertainty is bounded and known; for high-uncertainty launches it usually isn't.

## Practical Implications

*   **Measure load as close to the client as possible.** Server-side metrics can already be filtered or distorted by an earlier bottleneck; client-side or edge measurement gives the truest picture of actual offered load, which is the number the next capacity plan should be built from.
*   **Preemptively over-scale where feasible** for launches with high demand uncertainty, rather than relying solely on reactive [autoscaling](autoscaling-safety-bounds.md) to catch up — autoscaling has reaction lag, and a launch-day spike can outrun it before it stabilizes.
*   **Treat components as load-bearing that weren't designed to be.** A component that becomes "just another backend in the pool" under a migration or failover (as happened when a regional load balancer effectively became one more upstream target) inherits load it may not have been sized or tested for — audit every component in the actual traffic path, not just the ones designed to be user-facing.
*   **Test qualification should include load, not just correctness.** Treat every backend and dependency as a real source of potential load-induced regression, and load-test it as part of normal qualification — not only the top-level service.

Headroom sized for expected failure and rebalancing events (not demand spikes) is a related but distinct concern — see [N+M redundancy](n-plus-m-redundancy.md).
