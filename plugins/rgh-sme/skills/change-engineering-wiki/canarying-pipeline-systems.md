---
type: concept
title: Canarying Noninteractive (Pipeline) Systems
description: >
  Canary evaluation for batch and streaming pipelines needs a duration
  spanning a full work unit and worker-pool isolation, instead of the
  request-latency-scale duration and traffic-split isolation used for
  request-serving services.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Canarying Noninteractive (Pipeline) Systems

[Canary release](canary-release.md) for batch or asynchronous pipeline
systems needs different mechanics than for request/response services:

- **Duration** must span at least one full work unit — which can be much
  longer than a request/response latency, unlike the durations discussed
  in [canary population and duration selection](canary-population-and-duration-selection.md).
- **Isolation** is harder to guarantee: a given work unit's stages must
  all be processed by workers from the same pool (canary or control)
  throughout its processing, or the canary and control signals get mixed
  partway through — there's no single request boundary to split traffic
  on.
- **Metric choice broadens** beyond latency to end-to-end processing time
  and output quality/correctness.

If the pipeline's output is a durable write rather than a discardable
response, [two-phase mutation testing](two-phase-mutation-testing.md)
lets the canary's real output be validated before it's actually committed
to the destination.
