---
type: concept
title: Requirement vs. Design Decision
description: >
  A requirement states what a product must do and how well it must do
  it; a design decision states how that will be achieved — conflating the
  two locks in a solution before the problem has been properly specified.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 1"
---

Requirements and design are closely related but distinct, and the
distinction is a boundary, not a matter of degree. A requirement specifies
*what* a product must do and *how well* it must do it —
[functional](functional-requirement.md) and
[non-functional](non-functional-requirement.md) properties. Design
specifies *how* the implementation will achieve that. Flawless engineering
applied to the wrong solution is wasted effort precisely because getting
the requirements right is a separate problem from building well — a
correct answer to the wrong question.

The practical failure mode this guards against is a stakeholder (or an
analyst) stating a solution ("add a caching layer," "use a mobile app")
when what's actually needed is the underlying requirement the solution is
meant to satisfy ("the response must be visible within 2 seconds"). A
solution stated as if it were a requirement forecloses design options that
might satisfy the real need better, and it hides the actual acceptance
criterion behind an assumed implementation. See [essence of the business
work](essence-of-the-business-work.md) for the elicitation technique that
surfaces this distinction, and [fit criterion](fit-criterion.md) for how a
requirement, correctly stated as a *what*, still ends up measurable
without describing a *how*.

On the architecture side of the same boundary, see [architecturally
significant decision](architecturally-significant-decision.md) — the
symmetric question of which design choices are consequential enough to
document as decisions in their own right.
