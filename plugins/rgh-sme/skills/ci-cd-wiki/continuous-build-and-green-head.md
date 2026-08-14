---
type: concept
title: Continuous Build and Green Head
description: >
  Continuous build integrates latest mainline and runs automated build and
  test, producing green head — the latest verified cut — distinct from true
  head, the latest commit.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Continuous Build and Green Head

**Continuous build (CB)** integrates the latest code at head and runs an
automated build and test. "Breaking the build" includes failing tests, not
only compile errors. After submission, CB runs all relevant tests; a passing
change is marked **green**.

This yields two notions of head:

- **True head** — the latest committed change.
- **Green head** — the latest CB-verified change.

Developers often sync to green head for a stable dev environment but must
sync to true head before submitting their own change. CB is the automation
underneath postsubmit testing in
[presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md) and
feeds [release candidate](release-candidate.md) assembly in continuous
delivery.

Emergency paths can cut a candidate from true head and run a minimal test set
without waiting for full CB when speed outweighs full verification — a
conscious trade-off documented in [hotfix through pipeline](hotfix-through-pipeline.md).
