---
type: concept
title: Build Cop
description: >
  A rotating role responsible for keeping a project's automated test suite green
  by rolling back or fixing forward when postsubmit breaks, regardless of who
  caused the failure.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Build Cop

At scale, [presubmit vs. postsubmit testing](presubmit-vs-postsubmit-testing.md)
allows optimistic integration after a fast presubmit subset — empirically, a
change passing presubmit has high likelihood of passing slower tests, but
breakages still surface asynchronously on postsubmit. A **Build Cop** (per
team or project) owns keeping all tests passing: when postsubmit breaks, they
drop current work, identify the offending change, and **rollback** (preferred)
or fix forward (riskier).

Cultural norm: do not start new work on top of known failing tests. Build Cop
discipline pairs with fast presubmit (~minutes) and automated culprit finding
so longer tests don't block every submit but still get addressed quickly.

"Tests give us confidence to change; rollbacks give us confidence to undo.
Without tests, rollbacks can't be done safely. Without rollbacks, broken tests
can't be fixed quickly, thereby reducing confidence in the system." See
[rollback and roll-forward](rollback-and-roll-forward.md) and
[CI as alerting](ci-as-alerting.md).

Modern continuous build systems can auto-rollback when culprit confidence is
high — two-click rollback should be a baseline capability.
