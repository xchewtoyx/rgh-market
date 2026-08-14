---
type: concept
title: Assertion Placement and the Communication Value of Assertions
description: >
  An assertion should sit at the point where an invariant is established
  rather than everywhere it's relied on, must leave program behavior
  unchanged if deleted, and is valuable to readers as documentation even
  after the bug that prompted it is long fixed.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 10, Introduce Assertion"
---

Code frequently depends on conditions being true that are never stated
explicitly — anywhere from "this square root only works for positive
input" to "an object needs at least one field from some group populated."
Such assumptions are usually invisible, sometimes only documented in a
comment. An assertion is a conditional assumed to always be true; its
failure signals a *programmer* error, never something other parts of the
system should catch or react to. See
[introducing an assertion to fail fast on bad input](introduce-assertion-for-fail-fast.md)
for the judgment call about *when* an assumption is worth asserting versus
trusting; this note covers *how* to place and use assertions well once
you've decided to add one.

**Behavior-preservation constraint**: assertions must be written so the
program behaves identically if every assertion were deleted — some
languages even let assertions be compiled out entirely via a build switch,
which only works safely if this invariant holds. Adding a correct assertion
is therefore inherently behavior-preserving, which is why it's safe to do
mid-refactoring.

**Where to place it**: at the point where an invariant is *established*,
not merely everywhere it's relied upon. A value that's implicitly assumed
non-negative at every read site is better asserted once, at its setter or
constructor — the point where an invalid value would actually enter the
system — rather than re-checked defensively at each place that reads it.
This can make an otherwise-obscure error (a stray sign flip, an inversion
bug elsewhere) far easier to trace back to its true origin, since the
assertion fires at the moment the bad value is created rather than
somewhere downstream. See [invariants](invariants.md) for the more general
idea of a property that's always supposed to hold.

**Communication value beyond bug-finding**: assertions tell a reader what
state is assumed to hold at a given point in the code — this is why an
assertion is often worth leaving in place even after the specific bug that
prompted adding it has been fixed. [Self-testing code](self-testing-code.md)
reduces, but doesn't eliminate, assertions' debugging value, since a narrow unit test often
localizes a bug faster than an assertion firing at runtime would; the
communication value remains regardless of test coverage.

**Cautions**: assertions are for checking things that genuinely *must* be
true, not everything the author merely believes to be true. Duplication
among assertion conditions is a particular hazard, since these conditions
tend to get tweaked over time and duplicated copies easily drift out of
sync — use [Extract Function](extract-function.md) liberally to keep any
repeated assertion condition in exactly one place. Assertions are strictly
for programmer errors: if a value originates from an external, untrusted
source, validating it is a first-class part of the program's real logic,
not something to relegate to an assertion — unless the source is trusted
enough to treat its correctness as an actual invariant.
