---
type: concept
title: Feature Flag Aware Integration Tests
description: >
  Integration tests query rollout state and assert both enabled and
  disabled expected outputs so mid-rollout plug-ins do not break CI.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Feature Flag Aware Integration Tests

End-to-end tests with a single hard-coded expected result break when a
dependency is **mid-rollout**: a feature enabled in dev for months before
production forces manual per-environment test disabling during rollout.

Plug-in or service owners can specify a feature flag name or enabling
change ID plus **expected output with and without the feature**; tests
query the environment for feature status and verify accordingly. This
aligns test expectations with [feature flag blast radius
isolation](feature-flag-blast-radius-isolation.md) and [version skew during
rollout](version-skew-during-rollout.md) instead of treating rollout as
test infrastructure debt.

Automating flag-aware expectations reduces reliance on [known failure
suppression in CI](known-failure-suppression-in-ci.md) for rollout-induced
redness.
