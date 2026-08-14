---
type: concept
title: Consistency as a Design Tool
description: >
  Consistency means similar things are done in similar ways and dissimilar
  things are done visibly differently — a general-purpose tool for reducing
  complexity, because it lets knowledge learned in one place transfer safely
  everywhere else the same pattern appears.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 17"
---

Two distinct benefits follow from consistency. **Cognitive leverage**: once
you've learned how something is done in one place, that knowledge transfers
immediately to every other place using the same pattern, instead of having to
learn each situation from scratch — directly reducing
[cognitive load](cognitive-load.md). **Fewer mistakes**: inconsistency
invites false-pattern-matching, where a developer sees something that
*looks* familiar and imports assumptions from a previous, superficially
similar but actually different case (the mechanism behind the
[naming bug](naming-as-documentation.md)); consistency makes those
pattern-based assumptions safe to rely on instead of dangerous.

Consistency shows up in several forms: [names](consistent-names.md); coding
style (indentation, brace placement, naming and commenting norms, bans on
risky language features) beyond what a compiler enforces; interfaces with
[multiple interchangeable implementations](interface-duplication-when-ok.md),
where understanding one makes every other one easier to grasp; design
patterns — well-known, generally accepted solutions to recurring problems,
reused where they genuinely fit to speed implementation and raise reader
confidence; and [invariants](invariants.md).

The whole mechanism depends on a trust guarantee: "if it looks like an x, it
really is an x." See [overzealous consistency](overzealous-consistency.md)
for what happens when that guarantee is broken by forcing genuinely
different things to look the same, and
[ensuring consistency](ensuring-consistency.md) for how a team keeps the
guarantee intact as it scales.
