---
type: concept
title: Targeted Testing
description: >
  Once a specific change or refactoring is planned, check whether existing
  characterization tests actually exercise the exact code paths and type
  conversions that change — a passing test that never really executed the
  changed path proves nothing.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

Distinct from the general "understand this class" goal of
[characterization testing](characterization-tests.md): once you know exactly
what's about to change, check whether your tests exercise those exact
paths. Worked example — extracting a branch of a method into a new method:
logic that isn't being moved or altered doesn't strictly need a test for
safety, though it's nice to have; logic that *is* changing shape genuinely
needs a test that exercises it, since that's precisely where a mistake could
be introduced.

**Branch-coverage check**: "When you write a test for a branch, ask yourself
whether there is any other way that the test could pass, aside from
executing that branch. If you are not sure, use a sensing variable or the
debugger to find out whether the test is hitting it."

**Type-conversion trap**: original code accumulates into a `double`; an
extracted method changes the accumulator to `long`. A test built around
inputs whose fractional part happens to be zero will pass identically whether
or not a silent `double`→`long` truncation is happening — the test "passes"
without ever having exercised the conversion at all. When refactoring, check
two separate things: does the behavior still exist after the change, and is
it connected correctly? The most valuable characterization tests exercise a
specific path *and* exercise each conversion along that path — many
characterization tests are "sunny day" tests by nature (verifying presence,
not edge behavior), which is fine for confirming code was moved but
insufficient for confirming a type or precision change was safely
reconnected.

Practical techniques for catching conversion-sensitive bugs: manually
calculate expected values by hand, watching for truncation at each
conversion point; step through with a debugger to observe actual conversions
as they happen; use sensing variables to confirm a path and its conversions
actually executed; or fall back to characterizing a smaller chunk of code
directly via a trusted automated Extract Method, sidestepping the need to
reason about the conversion by hand. On that last option, even trusted
tooling needs sanity-checking case by case — see
[automated refactoring tools don't guarantee behavior preservation](automated-refactoring-tool-caution.md)
for a concrete instance of a tool silently changing which variables an
extracted method captures.
