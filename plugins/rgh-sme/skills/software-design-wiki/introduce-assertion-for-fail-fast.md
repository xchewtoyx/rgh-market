---
type: concept
title: Introduce Assertion to Fail Fast on Bad Input
description: >
  Whether to harden code against malformed input is a judgment call about
  trust in the caller — when corrupt data could otherwise propagate into a
  much-harder-to-debug failure downstream, fail immediately with an
  assertion instead.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
---

Many test frameworks distinguish a *failure* (an assertion produced a value
outside expected bounds) from an *error* (an unexpected exception thrown
during setup or exercise — calling a method meant for an array on a string,
say). Whether to harden production code against malformed input so it fails
predictably rather than erroring unpredictably is a judgment call depending
on trust in the input's source: internal, same-codebase callers often don't
need defensive validation — duplicate validation across trusted internal
boundaries frequently causes more trouble than it prevents. Inputs arriving
from external sources, like a raw JSON request, are a different matter and
should be validated and tested.

When a bad-input condition could let corrupt data propagate and cause a
much harder to debug failure further downstream, the tool is **Introduce
Assertion**: fail fast and loud at the point where the bad state is first
detectable, rather than letting it surface later as a confusing symptom far
from its cause. An assertion failure is itself a form of test, and doesn't
need a separate test written to check it. See
[invariants](invariants.md) for the related idea of documenting a property
that's always supposed to hold — an assertion is how you make a violated
invariant loud instead of silent — and see
[assertion placement and communication](assertion-placement-and-communication.md)
for where to put an assertion once you've decided to add one, and for its
value as documentation independent of bug-finding.

Because a rejected malformed input sits outside a function's [observable
behavior](refactoring-preserves-behavior.md) in the strict sense, a test
that pins down this behavior is fair game to discard once you're using tests
purely to protect a refactoring — refactoring is allowed to change
unspecified or undefined behavior, even though it must preserve everything
actually specified.
