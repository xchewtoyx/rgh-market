---
type: concept
title: Four Reasons to Change Software
description: >
  Every code change is adding a feature, fixing a bug, improving the design,
  or optimizing resource usage — categories that matter less than the
  underlying question of what behavior the change actually affects.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 1"
---

Whether a given change counts as a "bug fix" or a "feature" is often
subjective or organizational — contracts and quality initiatives may force a
team to categorize it one way or the other — and this framing masks the more
technically important question: what behavioral change does it actually
make?

"Behavior is the most important thing about software. It is what users
depend on." Users welcome added behavior but lose trust when behavior they
depend on changes or disappears — that's what a bug is. Adding a method
doesn't change behavior unless the method is actually called somehow; but
wiring a new method into existing UI or logic both adds new behavior and
subtly changes existing behavior at the same time (rendering differently,
taking marginally longer) — it's nearly impossible to add behavior without
changing existing behavior to some degree.

The other two reasons for change hold functionality constant on purpose: see
[refactoring preserves behavior](refactoring-preserves-behavior.md) for
design improvement, and the same logic applies to optimization, where a
resource (time or memory) changes while functionality doesn't. See
[preserving behavior is the real challenge](preserving-behavior-is-the-real-challenge.md)
for what this means about where the actual difficulty in any change lives.
