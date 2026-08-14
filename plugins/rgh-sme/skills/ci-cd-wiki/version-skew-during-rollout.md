---
type: concept
title: Version Skew During Rollout
description: >
  A distributed system temporarily running incompatible code, data, or
  configuration versions at once — an expected side effect of canarying and
  phased rollouts that tests and design must tolerate.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Version Skew During Rollout

**Version skew** is a state where a distributed system simultaneously contains
multiple incompatible versions of code, data, and/or configuration. It is not
only a failure mode — it is an **expected condition** during
[canary release](canary-release.md) and staged rollouts: a subset of production
runs the new version while the rest runs the old.

CI feedback loops span from local edit-compile-debug through presubmit,
postsubmit, staging, dogfood, and production. Canarying adds a
subset-of-production loop before full fleet promotion but introduces skew
between cohorts. [Feature toggles](feature-toggle.md) and experiments add
another dimension — behavior can diverge within the same binary via
configuration.

Release candidate promotion often catches configuration skew when static config
is versioned and promoted with code — see [release candidate](release-candidate.md).
Failure-isolation strategies for microservices (staging one service at head
against production versions of dependencies) must account for skew: staged
combinations may show false positives that wouldn't occur in production's
actual mix.

Design for backward-compatible RPC and schema changes; test representative skew
scenarios in [hermetic testing](hermetic-testing.md) or staging before wide
rollout.
