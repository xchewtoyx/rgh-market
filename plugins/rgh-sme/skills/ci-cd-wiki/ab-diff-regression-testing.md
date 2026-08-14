---
type: concept
title: A/B Diff Regression Testing
description: >
  Sending identical traffic to two isolated deployments and comparing outputs
  or metrics to detect regressions without pre-specifying every expected value.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# A/B Diff Regression Testing

**A/B diff** (differential regression) runs two SUT copies — baseline and
candidate — sends identical traffic (often multiplexed or sampled from
production), and compares outputs. Intended behavior is not fully pre-specified;
humans or tooling judge whether diffs are expected or regressions.

Variants:

- **A-A testing** — system vs. itself, isolating noise and flakiness from real diffs.
- **A-B-C testing** — last production, baseline build, and pending change together,
  showing immediate and accumulated impact.

Common for ads, search, and API-heavy systems. Limitations: **approval** (human
judgment on diffs), **noise** (unanticipated variance drives investigation),
**coverage** (traffic must hit corner cases), **setup cost** (roughly doubles
environment complexity).

Optimal performance diffs run both versions on the **same machine** to avoid
hardware/network confounds; otherwise calibrate with multiple runs dropping
outliers.

Distinct from [A/B testing via release routing](ab-testing-via-release-routing.md)
(business metric experiments on live traffic) and from
[canary release](canary-release.md) operational telemetry — though
[canary analysis](canary-release.md) combines prober assertions with metric diffs
during staged rollout.
