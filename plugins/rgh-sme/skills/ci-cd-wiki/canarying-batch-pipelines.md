---
type: concept
title: Canarying Batch and Pipeline Systems
description: >
  How to adapt canarying for asynchronous or batch pipelines — spanning at
  least one full work unit, keeping canary and control worker pools
  separate, and using two-phase mutation when a pipeline writes real data.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 8, 27"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 13"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

For asynchronous or batch pipelines, a [canary release](canary-release.md) has to span at least one full
work unit — which can run far longer than a typical request/response
latency — and every stage of a given work unit needs to be processed by
workers from the same pool (canary or control) throughout, or the signal
gets mixed between the two groups partway through. The metric aggregation
window also has to be no coarser than the canary's own duration: evaluating
a 30-minute canary against an hourly-computed error rate muddies the signal
by mixing canary and pre-canary behavior in the same number.

Where a pipeline mutates real data, canarying it safely can require
**two-phase mutation**: a first phase reads and transforms data but writes
only proposed mutations to a temporary store, without touching the real
destination; a validation step checks those proposed mutations for
correctness; only verified mutations are applied to the real destination in
a second pass. This lets a canary exercise a pipeline's actual output
without risking corrupting production data if the canary turns out to be
wrong.
