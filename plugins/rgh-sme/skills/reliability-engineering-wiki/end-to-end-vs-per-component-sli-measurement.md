---
type: concept
title: End-to-End vs Per-Component SLI Measurement
description: >
  Measuring the full path a user's request actually takes gives the most
  representative signal, but measuring each component's own reliability well
  is often an acceptable, cheaper compromise.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 3"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 13"
---

For a complex, multi-component service (e.g. load balancer → web app →
cache/DB → cart service → user service → payment gateway), different user
journeys traverse different subsets of components. Measuring only one
internal hop's error rate is not representative of the true end-to-end
experience — ideally the full path a real request takes is measured or
traced (see distributed tracing, owned by `observability`).

**Practical compromise**: perfect end-to-end capture isn't always feasible.
Measuring each component's own reliability well, then approximating
whole-journey reliability by composing the per-component SLIs, is often
"more than good enough" — see
[dependency reliability composition](dependency-reliability-composition.md)
for the multiplicative math this composition implies, which is itself a
reason to prefer end-to-end measurement where it's affordable: composing many
"reasonable" per-component targets erodes the overall guarantee faster than
intuition suggests.

For data pipelines specifically, per-stage measurement can miss cross-stage
corruption bugs where each stage individually "succeeds" but the composition
is wrong — see [pipeline SLI types](pipeline-sli-types.md).

See also [critical user journeys](critical-user-journey.md), which are the
concrete motivation for wanting end-to-end measurement in the first place.
