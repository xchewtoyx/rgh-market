---
type: concept
title: CI Culprit Finding
description: >
  When CI batches changes, isolate the breaking commit by re-running tests
  per change or binary-searching the batch.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# CI Culprit Finding

Large-scale continuous build evaluates more than one change per second,
so it cannot run every test on every change. **Batching** related changes
reduces total test execution but obscures which change in a batch broke a
test — harder still when flakes and test-infrastructure issues mimic real
failures.

Two approaches speed identification:

1. **Automatic batch split** — on failure, rerun tests against each change
   in the batch in isolation until the culprit converges (can take time).
2. **Developer binary search** — tools let an engineer walk a batch to
   find the likely breaking change interactively.

Culprit finding feeds [build cop rollback
discipline](build-cop-rollback-discipline.md): fast isolation makes
rollback or fix-forward decisions timely enough to restore [green head vs
true head](green-head-vs-true-head.md) confidence.
