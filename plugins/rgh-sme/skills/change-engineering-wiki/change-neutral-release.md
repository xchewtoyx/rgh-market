---
type: concept
title: Change Neutral Release
description: >
  Flag-guard every new feature so a rollout validates deployment mechanics
  and stability without simultaneously testing new behavior.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Change Neutral Release

When [placebo deployment A/B testing](placebo-deployment-ab-test.md) is
too heavy — insufficient userbase, too much operational overhead — a
**change-neutral release** is the fallback: every new feature is
[flag-guarded](feature-flag-blast-radius-isolation.md) off, so the only
thing under test during rollout is whether the deployment itself is stable
(install, startup, crash rate, resource use), not whether new behavior is
good.

This decouples "did we ship the binary safely?" from "did the feature
work?" — the same separation [decoupling deployment from
release](decoupling-deployment-from-release.md) achieves at the
deploy-vs-expose layer, applied during qualification of a rollout.

Once deployment stability is confirmed, features can be enabled
progressively via [staged percentage rollout](staged-percentage-rollout.md)
or flag ramping.
