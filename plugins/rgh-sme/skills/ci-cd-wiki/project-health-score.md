---
type: concept
title: Project Health Score
description: >
  A continuous 1–5 score aggregating test coverage, test latency, and related
  pipeline metrics so underperforming projects surface automatically for
  remediation.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Project Health Score

**Project Health (pH)** is Google's automated successor to the manual **Test
Certified** program — a dashboard scoring each project **1 (worst) to 5
(best)** from continuously gathered metrics including test coverage and test
latency. A pH-1 project is treated as a problem to address. Teams running
[continuous build](continuous-build-and-green-head.md) typically receive a
score automatically.

Test Certified (pre-2015) defined a **quarterly maturity ladder** teams could
follow voluntarily — Level 1: continuous build, coverage tracking,
[small/medium/large test classification](test-size-constraints.md), flaky-test
identification, fast presubmit subset; higher levels added "no releases with
broken tests" and removing nondeterministic tests; Level 5: all tests
automated, fast tests before every commit, full behavior coverage. An internal
dashboard created social pressure across 1,500+ projects.

pH generalizes that idea into ongoing measurement rather than a certification
checklist — aligning with [delivery metrics](flow-metrics.md) that guide
pipeline investment: when test latency or coverage regresses, the score drops
before releases stall entirely. Pair with [build cop](build-cop.md) for
responding to broken postsubmit and [CI as alerting](ci-as-alerting.md) for
presubmit signal quality.

This is a **pipeline health metric**, not a mandate on how to develop — Google
deliberately spread testing culture bottom-up (orientation, peer pressure)
rather than top-down coding mandates, on the theory that voluntary adoption
persists better than compliance.
