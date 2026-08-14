---
type: concept
title: Dependency-Breaking Catalog Framing
description: >
  Dependency-breaking techniques are technically behavior-preserving
  refactorings, but done deliberately without tests in order to get tests
  in place — a different safety regime from ordinary test-backed
  refactoring, and not expected to look like good design yet.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

The dependency-breaking catalog's entries are technically refactorings
(behavior-preserving), but unlike most published refactoring catalogs
(Fowler's, for instance), they're explicitly meant to be **done without
tests, in order to get tests in place** — a fundamentally different safety
regime, requiring careful mechanical steps in place of test-verified
confidence. Expectation-setting worth internalizing before applying any of
them: "these techniques do not immediately make your design better. In
fact, if you have good design sense, some of these techniques will make you
flinch." Their payoff is enabling test coverage, after which ordinary
test-supported refactoring can clean up whatever scar they leave — see
[dependency-breaking for testability](dependency-breaking-for-testability.md)
for that trade explained directly, and
[hyperaware editing](hyperaware-editing.md) for the mechanical discipline
([Preserve Signatures](preserve-signatures.md),
[single-goal editing](single-goal-editing.md)) that keeps these techniques
safe to apply without a test safety net.
