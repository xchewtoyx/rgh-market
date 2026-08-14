---
type: concept
title: The Rhythm of Refactoring
description: >
  Refactoring proceeds in steps far smaller than most people expect, each one
  compiled, tested, and committed before the next — and taking tiny steps is
  what lets you go faster, not slower.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 1 and ch. 5"
---

The central, counter-intuitive lesson of refactoring practice is that it
proceeds in steps far smaller than most people expect — each step leaves the
code compiling and all tests passing, and small steps compose into
substantial redesigns. Taking tiny steps is what lets you go *faster*, not
slower, because it keeps the distance between "last known-good state" and
"here" small at every point.

Discipline: compile, test, and commit after essentially every micro-step,
using a version-control system that supports cheap private commits (later
squashed before pushing to a shared history). When a test fails mid-step and
the cause isn't immediately obvious, the recommended recovery is to **revert
to the last good commit and redo the step in smaller increments**, rather
than debug forward from the broken state.

The size of the steps is itself an adjustable dial, not a fixed procedure:
the trickier the situation, the smaller the steps should be. In practice,
steps are usually bigger than any published mechanics describe — the
fallback to the smallest, safest version of a move is for when something
breaks, not the default pace. [Unit tests enable this kind of safe structural
change](unit-tests-enable-safe-refactoring.md) in the first place; without a
fast, self-checking suite, the rhythm has no feedback loop to run on. Related
editing discipline for code without full understanding is
[hyperaware editing](hyperaware-editing.md) and [single-goal
editing](single-goal-editing.md) — this note is specifically about the
test/commit/revert cadence, not about scope discipline mid-edit.
