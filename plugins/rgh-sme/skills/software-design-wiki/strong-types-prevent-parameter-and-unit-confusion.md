---
type: concept
title: Strong Types Prevent Parameter and Unit Confusion
description: >
  Wrapping same-typed parameters and physical quantities in small dedicated
  types turns argument-order and unit-mismatch mistakes into compile errors
  instead of silent runtime bugs.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 12, Use Strong Types"
---

[Primitive obsession](primitive-obsession.md) names the general reluctance
to give domain concepts their own type; this is the specific failure mode
that shows up whenever two or more parameters of a call share the same
primitive type. `AddUserToGroup(string, string)` doesn't tell a caller
which argument is the user and which is the group; `Rectangle(3.14, 5.67)`
doesn't say whether that's width-then-height or height-then-width;
`Circle(double)` doesn't say whether the value is a radius or a diameter.
Documentation and unit tests can catch some of these, but only at review
time or runtime — a caller who mixes up the argument order still compiles
and often still passes casual testing, since a swapped-argument bug rarely
crashes outright.

Wrapping each parameter in its own thin type turns the ambiguity into a
compile error: `Add(User("alice"), Group("root-users"))`,
`Rectangle(Width(3.14), Height(5.67))`, `Circle(Radius(1.23))`. Swapping two
same-shaped strong-typed arguments now fails to compile instead of silently
doing the wrong thing — and the call site becomes self-documenting enough
that, in the first example, the function name `Add` alone is sufficient
without needing `AddUserToGroup`'s more descriptive name to disambiguate
argument order.

**Unit confusion** is the same problem one level up: a bare number attached
to no unit type invites the units themselves to be mismatched rather than
just the argument position. Consequences range from harmless (`Timer(30)` —
seconds or minutes?) to catastrophic — a cited aviation incident where
ground crew calculated fuel in pounds instead of kilograms, and a lost Mars
orbiter that resulted from one engineering team using imperial units while
another used metric for the same interface. A strong type representing an
abstract quantity (`Duration`, `Weight`, `Timestamp`) rather than a bare
number closes this off structurally: the type carries unit-conversion
methods (`Duration::ToHours`, `Weight::ToKilograms`) instead of leaving the
caller to track which unit a raw number is denominated in, and it exposes
only the operations that are actually sensible for the concept — adding two
timestamps together is nonsensical and the type simply doesn't offer it,
while subtracting two timestamps to get a duration is offered because it's
meaningful.

This is a narrower, compiler-enforced version of what [invariants](invariants.md)
and [parse, don't validate](parse-dont-validate.md) do more generally: push
a class of mistake out to construction time so it can't recur at every call
site, rather than trusting every caller to get the convention right by
convention alone.
