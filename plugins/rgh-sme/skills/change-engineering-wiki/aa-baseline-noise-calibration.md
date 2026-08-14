---
type: concept
title: A-A Baseline Noise Calibration
description: >
  Run a system against itself under identical inputs to measure nondeterminism
  and infrastructure noise before trusting an A/B diff against a new version.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# A-A Baseline Noise Calibration

[A/B diff regression testing](ab-diff-regression-testing.md) compares old and
new version outputs. **A-A testing** compares a system to *itself* under
the same inputs — isolating nondeterminism, flaky infrastructure, and
measurement noise from genuine regressions.

The same principle applies to performance diff tests: if baseline and
candidate run on different machine or network tiers, a spurious regression
can appear. Optimal setup runs both versions on the same machine; when that
doesn't fit, calibrate via multiple runs discarding peaks and valleys.

This is a release-verification hygiene step before promoting a candidate —
aligned with [canary measurement validity](canary-measurement-validity.md)
(population-based comparison beats time-based) and [pre-canary artifact smoke
test](pre-canary-artifact-smoke-test.md) (structural sanity before spending
diff budget).
