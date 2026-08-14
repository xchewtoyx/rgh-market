---
type: concept
title: Functional Requirement
description: >
  A functional requirement specifies a single action a product must
  execute, stated as "the product shall [action]," attached to a specific
  use case, and kept separate from any statement of quality.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 10"
---

A functional requirement specifies an action the product must execute:
processing, a calculation, a data transform, a behavior. The standard
syntax is "the product shall [action] [object] [context/condition]" — for
example, "the product shall calculate the required de-icing chemical
quantity for a given road segment." It must be attached to a specific
[business use case or product use case](business-event-and-use-case.md),
and it must specify the business data entities and inputs/outputs the
action involves.

Common pitfalls: combining more than one distinct function into a single
requirement (split them — see the atomicity principle this wiki itself
follows); using ambiguous verbs like "process," "handle," or "manage"
without stating the actual logical or mathematical steps; and conflating a
functional capability with a quality statement about it ("calculate the
route quickly" mixes a function with a
[non-functional requirement](non-functional-requirement.md) about its
performance — split them, and give the quality half its own [fit
criterion](fit-criterion.md)).

A functional requirement should describe purely what the product must do,
not how — see [requirement vs. design decision](requirement-vs-design-decision.md)
for why that boundary matters.
