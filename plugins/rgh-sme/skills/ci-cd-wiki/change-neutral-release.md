---
type: concept
title: Change Neutral Release
description: >
  A rollout where all new functionality sits behind feature flags so the only
  variable under test is deployment stability, not product behavior.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Change Neutral Release

When [placebo deployment testing](placebo-deployment-testing.md) is too costly
— insufficient user volume, or too much operational overhead to run two
builds in parallel — a **change-neutral release** still separates deployment
risk from product risk: every new feature is [flag-guarded](feature-toggle.md)
and remains off during rollout, so staged production traffic exercises the
same user-visible behavior as the previous release. Guardrail metrics then
reflect deployment and infrastructure stability only.

Once the neutral rollout is clean, flags flip in subsequent releases or via
configuration rollout, decoupling "did the deploy break anything?" from "did
the feature work?" This pairs with [deploy vs. release](deploy-vs-release.md)
— deploy the binary early, release features when data supports it.
