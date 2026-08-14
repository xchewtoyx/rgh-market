---
type: concept
title: Observable Behavior Versus Implementation Details
description: >
  Observable behavior is what helps a client achieve its goals through
  operations or state; everything else is an implementation detail — and
  tests that track implementation details instead of observable behavior
  become brittle under refactoring.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
---

All production code can be categorized along two independent dimensions:
**public versus private API** (enforced by access modifiers) and **observable
behavior versus implementation details** (a semantic distinction not tied to
a language keyword).

Code counts as **observable behavior** when it does at least one of:

- Exposes an **operation** that helps a client achieve a goal (a calculation,
  a side effect, or both).
- Exposes **state** that helps a client achieve a goal.

Anything that does neither is an **implementation detail**. Whether code is
observable depends on who the client is and what its goals are — the code
must have an immediate connection to at least one such goal. "Client" can mean
in-process caller, external application, or UI.

In a **well-designed API**, observable behavior coincides exactly with the
public API and all implementation details sit behind the private API. There
is no symmetric notion of "leaking observable behavior" — hiding observable
behavior removes the client's ability to use it, which by definition
disqualifies it as observable.

**Rule of thumb**: if a client must invoke more than one operation on a
class to achieve a single goal, the class is likely leaking implementation
details. Ideally each individual goal is achievable via a single operation.
This heuristic holds for most business-logic cases but not universally.

Worked example: a `User` class exposes both a `Name` property and a public
`NormalizeName(string)` used to enforce "names ≤ 50 characters." A controller
whose goal is "change a user's name" needs only the setter — `NormalizeName()`
has no immediate connection to that goal and is an implementation detail
leaking through the public API. Fix: make `NormalizeName()` private and call
it from the `Name` setter so the client does `user.Name = newName`.

Maintaining this alignment is the mechanism of
[information hiding](information-hiding.md) — protecting invariants by
shrinking what callers can corrupt. Related: **tell-don't-ask** bundles data
with the functions that operate on it; hiding implementation details reduces
the surface clients can corrupt, while bundling data and operations lets those
operations enforce invariants.

**Testing payoff**: a well-designed API automatically improves unit tests —
when implementation details are private, tests have no choice but to verify
observable behavior. A test that asserts on internal composition (e.g. the
list of sub-renderers) couples to implementation and breaks under equivalent
refactors; retargeting at rendered output fixes the brittleness. See
[overabstracted tests](tests-should-assert-behavior-not-call-mechanics.md)
and [four pillars of a good unit test](four-pillars-of-a-good-unit-test.md).

**Onion layers**: whether a call is observable depends on who the client is
at that call site. A controller's call into domain code is an implementation
detail from an external client's perspective; from the controller's
perspective, the domain method is observable behavior worth its own tests.
Peel one layer at a time — test each layer from the viewpoint of its
immediate outside client.
