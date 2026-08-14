---
type: concept
title: Green Head vs True Head
description: >
  Continuous build maintains two notions of mainline — latest commit and
  latest commit that passed automated build and test — so developers can
  choose stability vs freshness when syncing.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Green Head vs True Head

**Continuous build** integrates the latest changes at head and runs an
automated build and test on every submission. "Breaking the build" includes
breaking tests, not just compilation failures.

This introduces two versions of mainline:

- **True head** — the latest committed change, whether or not it passed CI.
- **Green head** — the latest change verified green by continuous build.

Engineers often sync to green head for a stable local environment but must
sync to true head before submission so their change integrates with the
latest work. [Continuous delivery](continuous-deployment-vs-continuous-delivery.md)
typically assembles release candidates from green head (or a deliberately
chosen cut), not from arbitrary unverified commits — except [emergency
push paths](emergency-change-breakglass.md) that cut from true head with a
minimal test set when waiting for full continuous build is unacceptable.

Green head is the bridge between [presubmit vs postsubmit test
gating](presubmit-vs-postsubmit-test-gating.md) (fast signal before merge)
and release-candidate assembly (verified cut for promotion).
