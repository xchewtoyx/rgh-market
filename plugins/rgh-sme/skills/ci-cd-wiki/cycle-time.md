---
type: concept
title: Cycle Time
description: >
  The total elapsed time from when a change is committed (or conceived) to when
  it is running in production and delivering value, and the primary efficiency
  metric a delivery pipeline is optimized to reduce.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 1"
---

# Cycle Time

Cycle time measures the [deployment pipeline](deployment-pipeline.md) end to
end: commit to production-and-generating-value. Reducing it — from
months/weeks toward hours/minutes — is the primary goal continuous delivery
practices serve; every pipeline design decision (fast commit-stage feedback,
automated gates, build once/deploy everywhere) exists to cut cycle time without
cutting the confidence the pipeline provides.

Cycle time decomposes into **process time** (actual work: build, test, deploy)
and **queue time** (waiting between stages, for environments, or for manual
gates). Diagnosing which of the two dominates is the first step in
[value stream mapping](value-stream-mapping.md) to find a pipeline's
bottleneck; within process time itself, see
[pipeline critical path analysis](pipeline-critical-path-analysis.md) for
diagnosing which specific stage is actually gating a run's total duration,
as opposed to which stage merely looks slowest in isolation.

Rule-of-thumb targets: [commit stage](commit-stage.md) under 5–10 minutes;
automated acceptance suite under 1–2 hours; ability to deploy multiple times
per day on demand.

## A terminology note

Sources use overlapping terms for closely related but not identical
measures: "cycle time" (used here) versus "lead time" versus "deployment lead
time" versus "process time." Some sources deliberately avoid "cycle time" as
ambiguous and use **lead time** for the commit-to-production span and
**process time** (or "touch time") specifically for the queue-time-excluded
subset — matching what this note calls process time above. When comparing
figures across sources, check which of these definitions is actually being
used rather than assuming the label alone disambiguates it. See also
[the DORA four key metrics](dora-four-key-metrics.md)'s "lead time for
changes," which is this same measure, and
[flow metrics](flow-metrics.md)'s "flow time," which measures the same span
for a unit of business value rather than a single commit.
