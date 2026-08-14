---
type: concept
title: Risk-Driven Test Selection, Not Exhaustive Coverage
description: >
  Aiming to test every public method, or to enumerate every combination
  exhaustively, is a common way to end up writing no tests at all — target
  testing effort at the code you're actually worried about instead.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
---

Explicit rejection of "test every public method" as the goal — simple field
accessors that just read or write are worth skipping, since they're too
simple to likely harbor bugs. Testing effort should target the areas you're
actually worried about, both now and looking forward, rather than spreading
evenly across the surface area of the code — one concrete heuristic for
finding those areas is to [probe boundary
conditions](boundary-condition-testing.md), since edges are
disproportionately likely to harbor bugs. Rule: **"It is better to write
and run incomplete tests than not to run complete tests."** Aiming for a
too-complete test suite is a common way to end up writing none at all — the
goal should feel achievable, not exhaustive.

Related discipline: prefer one verification per test as a general default —
a test halts at its first failing assertion, so packing multiple checks into
one test can hide information about what else broke, unless the checks are
closely enough connected that knowing about the first failure makes the
others uninformative anyway.

There is no good objective measurement for "how much testing is enough" —
coverage tooling is useful only for spotting *un*tested code, not for
judging the quality of the tests that do exist. The practical criterion is
subjective confidence: how confident are you that if someone introduces a
defect into this code, some test would fail? This is the same question
[testability](testability.md) answers more formally, as a probability
grounded in the code's own structure rather than a gut feeling. Over-testing
is possible — a
warning sign is spending more time maintaining tests than the code they
cover — but this is called out as vanishingly rare compared to
under-testing.
