---
type: concept
title: Production vs. CI Test Comparison
description: >
  Running the same test suite continuously against production and against CI
  builds to distinguish new regressions from pre-existing upstream failures.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Production vs. CI Test Comparison

Integration tests that call live product APIs can fail for reasons outside the
system under test — an upstream microservice release, a flaky backend, a
rollout in progress elsewhere. Running the **same suite** continuously against
**production** and against **postsubmit CI** (new binaries, often same live
backends) is a cheap isolation technique: failures present in both are likely
environment-wide; failures only in CI point at the recent build.

This does not replace [hermetic testing](hermetic-testing.md) — live-backend
tests remain flaky — but narrows culprit search before investing in record/replay
or full hermetic stacks. Pair with [production probers](production-probers.md)
for ongoing health signal.

Manual comparison becomes costly as integration breadth grows; automating diff
between CI and prod failure sets is a common next step.
