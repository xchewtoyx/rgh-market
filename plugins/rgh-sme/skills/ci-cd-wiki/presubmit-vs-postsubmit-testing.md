---
type: concept
title: Presubmit vs. Postsubmit Testing
description: >
  Fast, reliable tests run before merge on presubmit; slower, broader, and
  occasionally flaky tests run after merge on postsubmit, accepting some
  rollbacks to keep presubmit productive.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Presubmit vs. Postsubmit Testing

**Presubmit** runs before a change lands on mainline; **postsubmit** runs after
integration on [continuous build](continuous-build-and-green-head.md) (CB).
Rule of thumb: **only fast, reliable tests on presubmit** — accept some
coverage loss at the gate and catch gaps on postsubmit, including rollbacks
when needed.

Reasons not to run everything on presubmit:

1. **Cost and productivity** — multi-hour presubmit blocks every submit.
2. **Flakiness cost** — engineers debugging unrelated flakes is expensive.
3. **Mid-air collisions** — while presubmit runs, mainline moves; two
   compatible-in-isolation changes can fail together at scale.

Postsubmit can tolerate longer runs and some instability when paired with
failure management (culprit finding, temporary test disablement, rollbacks).
Presubmit tests are usually scoped to the project being changed and run
concurrently. Unreliable tests belong off presubmit — or behind
[hermetic testing](hermetic-testing.md) if they must run early.

See [pre-tested commit](pre-tested-commit.md) for structural presubmit gating
and [commit test suite design](commit-test-suite-design.md) for what belongs
in the fast commit-stage suite.
