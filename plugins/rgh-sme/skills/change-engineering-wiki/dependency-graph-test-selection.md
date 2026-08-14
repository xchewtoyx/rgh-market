---
type: concept
title: Dependency Graph Test Selection
description: >
  Run only tests downstream of a change in the build dependency graph to
  minimize CI cost and wait time while preserving relevant coverage.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Dependency Graph Test Selection

At scale, running the full test suite on every change is infeasible.
Continuous integration can analyze the **downstream dependency graph** for
each change — maintained near-real-time by distributed build tools — and
determine the **minimal test set** affected by that change.

Scheduling also prioritizes changes triggering fewer tests ahead of those
triggering more; on a busy day the wait-time gap between a 100-test change
and a 1,000-test change can be tens of minutes. That incentive structure
nudges engineers toward [working in small batches](working-in-small-batches.md)
and targeted changes.

This is the resource-efficiency complement to [presubmit vs postsubmit test
gating](presubmit-vs-postsubmit-test-gating.md): gating decides *which
kinds* of tests run when; graph selection decides *which* tests must run
for *this* change.
