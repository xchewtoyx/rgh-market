---
type: concept
title: Optimizing Infrastructure for Continuous Change
description: The Cloud Age argument that, because infrastructure changes constantly and cheaply, teams should optimize their capability to change it rapidly and reliably rather than trying to minimize change.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 1"
---

Traditional ("Iron Age") governance treats infrastructure change as inherently risky: it adds up-front design, review, and approval steps to reduce the frequency of change, on the assumption that changes represent failure and should be minimized. This made sense when hardware made changes slow and expensive. It does not fit dynamic, cloud-provisioned infrastructure, where the cost of a change is low and systems change constantly whether or not that change is deliberately managed — through patches, scaling events, dependency updates, and incident fixes.

Because change is continuous and unavoidable, and because change is the only way to improve or fix a system, the productive strategy is to optimize the capability to make changes both rapidly *and* reliably, rather than trying to suppress change. A system that cannot be patched, fixed, or recovered quickly is not stable, however infrequently its code changes.

This reframes speed and quality as reinforcing rather than opposed: teams that are good at frequent, small, well-tested changes tend to also be more stable, while teams that add heavyweight change control to preserve stability tend to accumulate technical debt and become both slow and fragile. DORA's *Accelerate* research operationalizes this trade-off with [four key delivery and stability metrics](four-key-delivery-metrics.md) that correlate with organizational performance.

This principle motivates [defining infrastructure as code](define-everything-as-code.md) and [continuously testing and delivering it through a pipeline](infrastructure-delivery-pipeline.md): the goal is not to slow changes down until they are safe, but to make the change process itself fast, repeatable, and well-tested, so speed and safety come from the same mechanism.
