---
type: concept
title: Mean Time to Restore (MTTR) as a Delivery Metric
description: >
  One of the four DORA delivery-performance metrics, measuring how quickly
  full service is restored after a production incident caused by a change.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Mean Time to Restore (MTTR) as a Delivery Metric

Mean time to restore (MTTR) measures the speed at which full service is
restored following an incident. It is one of the two "stability" metrics in
the DORA four-key-metrics model, alongside [change failure rate](change-failure-rate.md).
DORA treats failure as inevitable in complex systems — the metric that
matters for delivery safety is not whether failures happen, but how fast
they are undone.

Empirical performance tiers (2017 DORA benchmark):

- **High performers**: less than one hour.
- **Medium performers**: less than one day.
- **Low performers**: between one day and one week.

From a change-engineering standpoint, MTTR for a change-caused incident is
largely a function of whether the change is designed to be
[rolled back cheaply](rollback-vs-roll-forward.md) — the fastest recovery
path is rarely "diagnose then fix forward," it's "revert to the last known
good state." Detecting *which* recent change caused a regression, and the
broader mechanics of incident response, belong to `incident-management`;
this note is scoped to how a change's design affects how fast it can be
undone.
