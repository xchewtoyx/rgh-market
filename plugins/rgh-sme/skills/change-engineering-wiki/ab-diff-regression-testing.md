---
type: concept
title: A/B Diff Regression Testing
description: >
  Send identical traffic to old and new versions and compare outputs to
  catch regressions without pre-specifying every expected behavior.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# A/B Diff Regression Testing

**A/B diff regression testing** runs two isolated SUT copies — typically
old production version and candidate build — sends identical traffic to
both (often via a third comparator binary), and diffs responses. Intended
behavior isn't fully pre-specified; humans or policy judge whether
differences are expected or regressions.

Variants:

- **A-A testing** — system against itself, to isolate nondeterminism and
  infrastructure noise from real A/B diffs; see [A-A baseline noise
  calibration](aa-baseline-noise-calibration.md).
- **A-B-C testing** — last production version, baseline build, and pending
  change together, showing immediate and accumulated impact.

Data is usually multiplexed from production or smart-sampled for coverage.
Limitations: human **approval** of diffs, **noise** remediation, **coverage**
of corner cases, and roughly doubled setup complexity (worse with
interdependencies).

A/B diff is a common large-test form in release verification pipelines —
complementary to assertion-based [release candidate regression
testing](release-candidate-regression-testing.md) and [canary
release](canary-release.md) (which compares populations in production rather
than isolated twin environments).

For deployment-stability-only rollouts, pair with [change-neutral
release](change-neutral-release.md) or [placebo deployment A/B
test](placebo-deployment-ab-test.md) when comparing in live traffic.
