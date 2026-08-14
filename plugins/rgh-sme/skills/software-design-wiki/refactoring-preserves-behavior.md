---
type: concept
title: Refactoring Preserves Behavior
description: >
  Refactoring is a series of small structural modifications, each verified
  by tests to leave existing behavior unchanged — distinct from both
  low-risk cosmetic cleanup and high-risk invasive rewriting.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 1"
---

Refactoring alters a piece of software's structure or maintainability while
keeping its behavior intact. Losing behavior along the way is what
programmers call a bug — this risk is exactly why many programmers are
reluctant to refactor in the first place. The definition specifically
excludes two neighboring activities: reformatting or other cosmetic cleanup
(low-risk, but not really restructuring), and invasive rewriting (high-risk,
and not done in small, individually-verified steps). Refactoring proceeds
through small structural changes, each one supported by tests that verify
behavior hasn't changed — see
[dependency-breaking techniques](dependency-breaking-vs-refactoring.md) for
what to do when those tests don't exist yet. Refactoring isn't meant to
produce functional changes, though performance can shift as a side effect of
restructuring. Fowler's canonical definition puts the same point formally: "a
change made to the internal structure of software to make it easier to
understand and cheaper to modify without changing its existing behavior."
Note that this guarantee doesn't come for free from tooling — see
[automated refactoring tools don't guarantee behavior preservation](automated-refactoring-tool-caution.md).

A commit-level discipline follows directly from this definition: [never mix
refactoring with a functional change in the same
commit](never-mix-refactoring-with-functional-changes.md) — a mixed diff
hides a smuggled behavioral bug behind an otherwise behavior-preserving
change.

"Observable behavior" is deliberately a loose standard, not a literal
byte-for-byte one: internals such as raw performance can shift, and module
boundaries themselves often *do* change via refactorings like changing a
function's declared parameters or moving a function to another module —
both are compatible with the definition as long as nothing a caller actually
depends on breaks. Refactoring also preserves existing bugs rather than
silently fixing them, though a latent, previously-unobserved bug can
incidentally get fixed as a side effect of restructuring.
