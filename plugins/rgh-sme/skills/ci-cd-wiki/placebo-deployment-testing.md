---
type: concept
title: Placebo Deployment Testing
description: >
  Running an A/B rollout where one cohort receives the real update and another
  receives a re-shipped old version, to distinguish deployment-induced metric
  shifts from genuine product regressions.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Placebo Deployment Testing

Pushing **any** update — even with no functional change — can itself cause a
statistically significant shift in user metrics. A small-percentage
[canary release](canary-release.md) therefore reveals crash and stability
signals but says little about whether the new version is actually *better*.

**Placebo deployment testing** ships two versions simultaneously to large,
similar user cohorts: the real update and a **placebo** (the previous version
re-shipped). Comparing guardrail and product metrics between cohorts isolates
effects of the deployment process and environment from effects of the code
change. With sufficient user volume, statistically significant results can
arrive within hours or days; an automated metrics pipeline can then promote
the real release to more traffic as soon as guardrails hold.

This is distinct from [A/B testing via release routing](ab-testing-via-release-routing.md),
which compares two intentional product variants presumed non-defective — here
one variant is deliberately identical to the prior release to control for
deployment noise. The technique needs a large enough user base to be worth
the overhead; where it does not, fall back to a
[change-neutral release](change-neutral-release.md).
