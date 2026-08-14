---
type: concept
title: Seam
description: >
  A place in existing code where behavior can be substituted without editing
  the code at that point, which is the enabling mechanism for bringing
  untested legacy code under automated test before changing it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 4"
---

# Seam

A seam is a place where you can alter a program's behavior without editing
the source at that point. Every seam has an **enabling point**: somewhere
else (a build flag, a classpath, a constructor argument, which subclass gets
instantiated) where the decision between the real behavior and a substitute
is actually made. The code at the seam itself stays byte-for-byte identical
between production and test — only the enabling point differs.

This is the mechanism [characterization testing](characterization-testing.md)
depends on: code with hard-wired collaborators (a direct database call, a
`new` of a concrete network client) has no seam, so it can't be exercised in
isolation at all. Finding or creating a seam is what turns "untestable
without a live dependency" into "testable by substituting a fake at the
enabling point" — which is the prerequisite for getting legacy code inside a
[commit stage](commit-stage.md)'s fast, in-memory test suite instead of
depending only on slow end-to-end regression checks.

## Seam types, in order of preference

- **Object seams** (OO languages): a call like `cell.recalculate()` is a seam
  if the runtime type of `cell` can vary without editing the call site — e.g.
  because `cell` arrives as a parameter or is otherwise injected rather than
  constructed inline. This is the workhorse mechanism behind
  [test-driven development](test-driven-development.md)'s emphasis on
  dependency injection, and is generally the best choice: the substitution is
  explicit in the code (a constructor argument, an interface), so the
  resulting tests are easy to maintain.
- **Link seams**: exploit whatever resolves cross-module references at
  link/build time (a linker, a classpath) to swap in a stub implementation
  for testing. The enabling point lives outside the program text entirely (a
  build script or IDE project setting), which makes it easy to lose track of
  which environment is actually running — usage only pays off when the
  test/production difference is made obvious.
- **Preprocessing seams** (C/C++ specific): the macro preprocessor runs before
  compilation and can redefine a call under a `TESTING` flag. The most
  fragile of the three — heavy conditional compilation forces maintaining
  what is effectively several different programs in one source tree.

## Why exploitability isn't automatic

A seam can exist without yet being usable. A private static method call is
technically a seam (you're not editing the call site), but it isn't
exploitable until a small, mechanical, behavior-preserving edit — loosening
visibility, removing `static` — makes it overridable. This distinction
matters for legacy work: the first pass over untested code is often not
"add tests" but "make the existing seams exploitable," a narrower and safer
edit to make without a test safety net than any real behavioral change.
