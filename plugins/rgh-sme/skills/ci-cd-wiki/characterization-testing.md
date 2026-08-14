---
type: concept
title: Characterization Testing
description: >
  Writing tests that document a legacy codebase's existing behavior before
  refactoring or extending it, so later changes can be verified against what
  the system actually does rather than what it was intended to do.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 4"
---

# Characterization Testing

Drawing on Michael Feathers' definition of legacy code as "code without
automated tests," characterization testing is the technique for bringing such
code safely under a [deployment pipeline](deployment-pipeline.md)'s automated
gates: before changing anything, write tests that capture what the code
currently does (not what it's supposed to do), then use those tests as a
safety net while refactoring or adding features.

The prerequisite is finding [seams](seam.md) — places in the code where
behavior can be altered without editing the source directly (e.g. by
injecting a different dependency) — and using them to break tight couplings
that would otherwise make the code untestable in isolation. Only once
characterization tests exist does the code have the fast feedback loop a
[commit stage](commit-stage.md) depends on; without them, changes to legacy
code are unverifiable except by manual regression testing.

## Writing one: assert wrong, then correct the assertion

The concrete technique: put the code in a test harness, write an assertion
you expect to fail (a deliberately implausible value), run it, and read the
actual value out of the failure message — then rewrite the assertion to
match that actual value. Repeat for each behavior worth pinning down. This
sidesteps the otherwise-tedious alternative of manually tracing the code to
predict its output by hand; the test harness computes the real answer for
you and the failure message hands it back.

The natural objection — "isn't this just enshrining whatever the code
happens to do, bug included?" — misses what the test is for. It isn't a
correctness oracle; it's a drift detector for the
[commit stage](commit-stage.md): if a later change silently alters this
behavior, the test fails and forces a conscious decision about whether that
change was intended, rather than letting it ship unnoticed. A suspicious
result should still be flagged for follow-up, not silently accepted.

There's no complete set of characterization tests for a nontrivial piece of
code, so the practical stopping point is targeted: write enough tests to
be confident you understand the code's current behavior, then check
specifically whether those tests would actually catch a mistake in the
change you're about to make — including any type or precision conversion on
the changed path, since a test built from happy-path inputs can pass
identically whether or not a conversion bug is present. If they wouldn't
catch it, add more before proceeding, or narrow the change.

## The legacy code dilemma

Bringing untested code under test creates a circularity: changing code
safely requires tests, but adding tests to tightly-coupled code often
requires changing it first (to expose a seam a test can use). The resolution
is asymmetric risk-taking: dependency-breaking edits are done first, without
tests, but kept deliberately mechanical and conservative (e.g. narrowing a
constructor parameter's type, extracting an interface) rather than any real
behavioral change — since these edits have no safety net yet, they must be
small enough to verify by inspection. Only after a seam is opened this way
can characterization tests be written, after which normal
[test-driven development](test-driven-development.md) and refactoring can
resume with an actual safety net in place.
