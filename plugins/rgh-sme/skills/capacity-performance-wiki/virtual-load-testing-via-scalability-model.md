---
type: concept
title: Virtual Load Testing via a Scalability Model
description: Using a fitted scalability model to project throughput at concurrency levels too expensive, impractical, or licensing-constrained to load-test directly, instead of extending the real test rig further.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 1, ch. 6"
---

Real load testing at large scale is often bottlenecked by something other than the question being asked: enough client licenses to drive the target load, hardware big enough to generate or absorb it, or simply time. **Virtual load testing** substitutes a small, cheap, real measurement rig plus a fitted scalability model ([the Universal Scalability Law](universal-scalability-law.md), via [fitting it to measured data](fitting-universal-scalability-law-to-data.md)) for the more expensive alternative of physically scaling the test rig up to the target load.

## Why "Appearances Can Be Deceiving" Without It

A worked comparison across three server configurations that all showed an apparent throughput plateau or drop-off around the same measured load level illustrates the risk of stopping at the raw data: fitting the USL to each configuration's measurements revealed very different coherency values behind that superficially similar plateau. One configuration's true capacity maximum sat far beyond the tested range — meaning the "saturation" visible in the raw data was an artifact of not having tested far enough, not a real ceiling — while another configuration's fitted maximum sat close to where testing had already stopped, confirming the apparent ceiling was real. Without fitting the model, both cases look identical in the raw data; extending the real test rig to tell them apart would have cost more testing time and hardware than the fit did.

## What It Trades Away

A virtual (model-based) projection is not a substitute for testing the load pattern that actually matters in production — it is only as good as the measurements it was fit from, and it inherits the model's own limitations: it assumes a stable, homogeneous workload throughout the projected range, and (per [the Universal Scalability Law](universal-scalability-law.md)) it can flag *that* contention or coherency dominates but not *which specific subsystem* is responsible without further investigation. Treat a virtual projection as a way to decide *whether* to invest in real testing at a given scale, or as a stand-in when real testing genuinely isn't feasible — not as a permanent replacement for validating the load levels a system will actually see. See [capacity test types](capacity-test-types.md) for where synthetic testing (of which this is a model-based variant) sits relative to [live-traffic capacity validation](live-traffic-capacity-validation.md).
