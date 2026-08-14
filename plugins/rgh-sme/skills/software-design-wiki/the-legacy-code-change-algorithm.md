---
type: concept
title: The Legacy Code Change Algorithm
description: >
  A five-step sequence for making a change in legacy code safely — identify
  change points, find test points, break dependencies, write tests, then
  make the change and refactor — with tested areas of a codebase gradually
  growing from isolated islands into larger covered regions.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

1. **Identify change points** — figure out where in the code the change
   actually needs to happen, which itself can require first understanding
   the code or the overall architecture well enough to know.
2. **Find test points** — decide which methods and classes around the
   change points need coverage.
3. **Break dependencies** — see
   [dependency-breaking for testability](dependency-breaking-for-testability.md)
   for the general technique, applied to whatever specific obstacle blocks
   getting the relevant class or method into a test harness.
4. **Write tests** — legacy-code tests differ from tests written alongside
   new code, since they're written after the fact against existing,
   possibly-undocumented behavior; see
   [characterization tests](characterization-tests.md).
5. **Make changes and refactor** — favoring a test-first style for adding
   new features once coverage exists, and ordinary
   [refactoring](refactoring-preserves-behavior.md) for improving structure.
   (This is a narrower, more favorable use of test-first development than
   the general-purpose case examined in
   [skepticism of test-driven development](skepticism-of-test-driven-development.md):
   here it's applied specifically to extending code that's already been
   pinned down by characterization tests, not to designing a class from
   scratch.)

These are deliberately "baby steps," not a path to an ideal, pattern-enriched
design — "better" is context-dependent, often just a few steps more
maintainable than before. Even a purely mechanical improvement, like breaking
down a large class just to make it more workable, is argued to matter
significantly in practice. The cumulative-value framing: over time, tested
areas of a codebase "surface like islands rising out of the ocean,"
eventually growing into "continents of test-covered code."
