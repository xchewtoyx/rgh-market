---
type: concept
title: Architectural Tactic
description: >
  A tactic is a design decision that influences one quality-attribute
  response to a stimulus; a pattern bundles several tactics together and
  so embodies trade-offs among several quality attributes at once.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 3"
---

A **tactic** is a design decision that directly influences achievement of
a single [quality-attribute scenario](quality-attribute-scenario.md)'s
response to its stimulus — "schedule resources" for a performance
response, "use an intermediary" for a modifiability response. An
**architectural pattern** is a recurring design problem in a specific
context paired with a proven solution, specified as a set of element
roles, responsibilities, relationships, and collaborations — see
[pattern-language documentation format](pattern-language-documentation-format.md)
for how such patterns get named, structured, and cited. Because a
pattern is built from several tactics working together, choosing a
pattern is really choosing a whole bundle of trade-offs among multiple
quality attributes at once, not a single-attribute decision the way
picking one tactic is.

This distinction matters for documenting rationale precisely: recording
"we used a broker pattern" names a bundle, but recording *which tactics*
that pattern choice actually committed you to (which quality attributes
it traded off, and by how much) is what makes the decision's consequences
inspectable later — see [documenting trade-offs](documenting-trade-offs.md).
It also explains why a stock pattern often needs deliberate augmentation:
if the textbook broker isn't secure or available enough, tactics are the
vocabulary for stating exactly what was added to it and why, rather than
describing the result as a vague variant of the pattern.

A small number of **super-tactics** recur across nearly every pattern and
across multiple quality attributes at once — encapsulation, restricting
dependencies, using an intermediary, abstracting common services, and
monitoring are named examples. Recognizing when a design decision is
actually an instance of one of these is useful specifically for
rationale-writing: it lets a decision record cite the general tactic being
applied rather than re-deriving the reasoning for it from scratch each
time.
