---
type: concept
title: TDD for Legacy Code, Not Sprout/Wrap, as the Default
description: >
  Confront existing code by getting it under test and adding features
  test-first, rather than defaulting to Sprout/Wrap Method as a permanent
  strategy — habitual sprouting leaves surrounding code un-improved and
  breeds fear that it can never be tamed.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

[Sprout method](sprout-method.md) and [sprout class](sprout-class.md) are explicitly flagged as
a fallback for time pressure, not a default practice. Leaning on them
habitually has three costs: the surrounding old code never improves; new
code can unknowingly duplicate logic buried in untested areas ("it might
just lie there and fester"); and it breeds fear and resignation — fear that
a piece of code can never be tamed, resignation that whole areas simply
won't get better — with the leftover sprouts and wraps serving as constant
reminders of both. The stated preference: "it's better to confront the beast
than hide from it."

Confronting it means an extended TDD algorithm, distinguished from the
greenfield loop by an explicit step 0 and a legacy-specific caveat on step 3:

0. Get the class under test (see
   [the legacy code change algorithm](the-legacy-code-change-algorithm.md)
   and [dependency-breaking for testability](dependency-breaking-for-testability.md)).
1. Write a failing test case.
2. Get it to compile.
3. Make it pass — **"try not to change existing code as you do this"**, a
   caveat absent from ordinary TDD: the point is to add new, tested behavior
   without simultaneously risking untested existing behavior.
4. Remove duplication (see
   [the TDD loop](test-driven-development-loop.md) for the discipline this
   step depends on).
5. Repeat.

An alternative on-ramp for adding a feature via variation rather than net-new
logic is [programming by difference](programming-by-difference.md).
