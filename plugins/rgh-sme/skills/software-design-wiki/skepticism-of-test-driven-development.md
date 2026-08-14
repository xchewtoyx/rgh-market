---
type: concept
title: Skepticism of Test-Driven Development
description: >
  TDD's moment-to-moment focus on making the next test pass, rather than on
  finding the best overall design, is tactical programming by another name —
  though writing a failing test before fixing a bug is a genuine exception
  worth keeping.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 19"
---

Test-driven development means writing a class's unit tests first, based on
expected behavior and all initially failing, then implementing just enough
code to make each test pass one at a time, finishing when all tests pass.
This is distinct from — and treated with more skepticism than —
[unit testing in general](unit-tests-enable-safe-refactoring.md), which is
strongly endorsed on its own.

The core objection: TDD's moment-to-moment focus is on making the next
specific test pass, not on finding the best overall design — this is
[tactical programming](strategic-vs-tactical-programming.md), plainly, with
all its downsides. TDD is "too incremental": at any given moment it's
tempting to just hack in whatever makes the next test green, and the
methodology never designates an explicit point to step back and actually
design, making it easy to end up with a mess despite good test coverage. This
is the same principle as
[the unit of incrementality should be abstractions, not features](agile-and-incremental-abstraction-design.md)
applied to testing specifically: once an abstraction's need is identified, it
should be designed as a coherent whole — or at least with a reasonably
complete initial set of core functionality — rather than assembled
incrementally, test by test, over time, since a wholesale design pass is more
likely to produce parts that genuinely fit together.

The notable carve-out is **bug fixing**: before fixing a bug, write a unit
test that reproduces and fails on the bug, then fix the bug and confirm the
test now passes. This is the only reliable way to know the fix actually
addresses the real problem — fixing first and writing the test afterward
risks a test that doesn't actually exercise the buggy path, silently failing
to validate anything.

A narrower, more favorable use case for the same mechanics is adding one
already-understood piece of behavior to code that's already under test —
see [the TDD loop](test-driven-development-loop.md) and
[TDD for legacy code](tdd-for-legacy-code.md). There, the target abstraction
already exists and isn't being designed test-by-test, which sidesteps the
core objection above.
