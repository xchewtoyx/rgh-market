---
type: concept
title: Design Patterns Are a Substitute for From-Scratch Design, Not an End in Themselves
description: >
  Design patterns are widely-recognized reusable solution shapes worth
  reaching for instead of inventing a new mechanism, but they only help when
  they genuinely fit — forcing a mismatched pattern onto a problem produces
  worse results than a tailored solution.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 19"
---

A design pattern (iterator, observer, and similar widely-recognized shapes)
is a reusable solution to a common category of problem. The reasonable
default: reach for an established, well-regarded pattern instead of
inventing a new mechanism, on the assumption that if a pattern is genuinely
well-suited to your situation, it will likely be hard to beat with a custom
approach.

The principal risk is **over-application**: not every problem has a clean
fit with an existing pattern, and forcing a mismatched pattern onto a problem
produces worse results than a tailored custom solution would. Using a pattern
doesn't automatically improve a design — patterns only help when they
genuinely fit. Just as with other techniques throughout this domain, the fact
that design patterns are good in the right context doesn't imply that using
*more* of them is better; see
[getters and setters are shallow](getters-and-setters-are-shallow.md) for a
concrete instance of a "good" pattern becoming reflexive overuse.
