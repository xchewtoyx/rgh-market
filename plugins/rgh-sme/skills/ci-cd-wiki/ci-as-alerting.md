---
type: concept
title: CI as Alerting
description: >
  Continuous integration is the left shift of production alerting — both exist
  to surface actionable signals quickly, and CI policies benefit from the same
  error-budget thinking SRE applies to uptime.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# CI as Alerting

Production monitoring reveals how live systems respond to change; CI reveals
how software responds to changes in its environment **before** deployment.
Both serve the same purpose: identify problems as quickly as reasonably
possible — CI at the early end (test failures), alerting at the late end
(metric thresholds).

Shared principles:

- **Fidelity and actionability** — tests should fail only when an important
  invariant is violated, not because the test is brittle. A flaky presubmit
  test is as harmful as a spurious page every few minutes: "If it isn't
  actionable, it shouldn't be alerting. If it isn't actually violating the
  invariants of the system under test, it shouldn't be a test failure."
- **Localized vs. cross-dependency signals** — unit tests parallel cause-based
  monitoring; integration and release tests parallel black-box probing.
  End-to-end signals have highest fidelity but cost more in flakiness,
  resources, and debug difficulty.
- **Brittle signals** — cause-based alerts on arbitrary thresholds and tests
  asserting overly rigid invariants (e.g. byte-identical JPEG output) can still
  help investigation but should not be the primary quality gate.

Reframing CI with SRE's **error budget** mindset:

1. **100% green CI**, like 100% uptime, is expensive — pursuing it literally
   risks a race between testing and submission.
2. Silencing a alert that doesn't impact users is correct; similarly, disabling
   or quarantining a test known to fail for irrelevant reasons can be correct
   until fixed — not every test failure predicts production impact.
3. Blanket "nobody commits if CI isn't green" policies are often misguided.
   Block compounding failures, but when root cause is understood and clearly
   won't affect production, blocking all commits is unreasonable.

See [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md),
[reliable tests over coverage](reliable-tests-over-coverage.md), and
[developer-owned test maintenance](developer-owned-test-maintenance.md).
