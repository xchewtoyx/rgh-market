---
type: concept
title: Branch-for-Release Pattern
description: >
  Cutting a short-lived release branch from mainline just before a release,
  so mainline stays open for new work while only critical fixes land on the
  branch and get merged straight back.
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 14"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Branch-for-Release Pattern

Distinct from [trunk-based development](trunk-based-development.md)'s daily
integration discipline, this is a branching pattern used at the point of
release rather than during ongoing feature work: a release branch is created
from mainline right before a release goes out. Mainline immediately continues
accepting new feature work as normal. Only critical bug fixes needed for the
release in flight are committed to the release branch, and each such fix is
immediately cherry-picked or merged back into mainline so mainline never loses
a fix that shipped.

Unlike [branch by feature](trunk-based-development.md), this branch is
short-lived by construction (it exists only until the release stabilizes) and
carries a narrow, well-defined purpose (stabilization fixes only, not new
features) — which is what keeps it from accumulating the divergence that
causes [integration hell](integration-hell.md).

At organizations with rapid [continuous deployment](continuous-deployment.md),
release branches are often absent — fix forward from trunk instead. They remain
common for shipped devices, monthly cadences, or when you must know exactly
what is in the field; keep cherry-picks minimal and don't plan wholesale
rem merges with trunk. Contrast [long-lived dev branch anti pattern](long-lived-dev-branch-anti-pattern.md).
