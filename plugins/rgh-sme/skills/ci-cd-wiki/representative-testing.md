---
type: concept
title: Representative Testing
description: >
  When exhaustive qualification across all client variants is infeasible, test a
  representative sample and rely on staged production rollouts for breadth.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Representative Testing

Client and device diversity — form factors, OS versions, locales, network
conditions — can make pre-release qualification feel impossible. The useful
reframe: diversity is not a problem to eliminate but a **fact** to design
around.

When comprehensive pre-production testing is infeasible, aim for
**representative testing** in lab or beta tracks, then use
[staged rollouts](canary-release.md) to slowly increase exposure while
monitoring guardrails. Specialized testing tracks (e.g. Play Store internal,
alpha, beta, staged production percentages) let global QA teams exercise
builds overnight across regions.

Synthetic environments dissimilar from production still produce late
surprises; **production-like staged exposure** is the benchmark. See
[change-neutral release](change-neutral-release.md) and
[placebo deployment testing](placebo-deployment-testing.md) for separating
deploy stability from feature effects during rollout.
