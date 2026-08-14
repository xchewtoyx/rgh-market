---
type: concept
title: Pinch Points Reveal Natural Encapsulation Boundaries
description: >
  Where a pinch point falls tells you where a codebase's actual
  encapsulation boundary is, and clustering an effect sketch's bubbles
  without their names attached can surface classes hiding inside a class
  that hasn't been split out yet.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 12"
---

A [pinch point](pinch-point.md) is "a natural encapsulation boundary," not
just a testing shortcut. If one method is the pinch point for a whole
cluster of changes to its collaborators, that tells you exactly where to
look when the cluster's overall output is wrong, and confirms that a caller
of that method genuinely doesn't need to know about the collaborators'
internals — "pretty much the definition of encapsulation."

**Using effect sketches to find hidden classes**: build an
[effect sketch](effect-sketches.md) for a class, then check which private
methods and fields a given public method's effects actually touch versus
never touch. A cluster of private members that a public method depends on
only *through* certain other private methods — never directly — is a natural
encapsulation boundary hiding a class that hasn't been extracted yet
(worked example: a parser's tokenizing state and helper methods form such a
cluster, suggesting a `Tokenizer` class). Recommended exercise: sketch
effects for a large class, strip away the existing names, look purely at how
bubbles cluster, then invent a name for each cluster as a candidate new
class. This works best as a **team exercise** — the naming discussions it
provokes "help you and your team develop a common view of what the system is
and what it can become," a payoff beyond the immediate refactoring.

Writing tests at a pinch point "carves out" a set of classes as a little
oasis where subsequent changes become easy — but see
[pinch point traps](pinch-point-traps.md) for why this needs to stay
temporary rather than becoming the permanent test strategy for that area.
