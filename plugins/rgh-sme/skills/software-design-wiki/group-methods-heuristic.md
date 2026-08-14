---
type: concept
title: Group Methods to Find Hidden Responsibilities
description: >
  List every method by name and visibility and look for clusters that
  suggest a distinct purpose — incrementally, without needing to categorize
  every method or extract a class before you actually need to touch it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Seeing [responsibilities](single-responsibility-principle.md) inside an
oversized class is a general design skill, not something unique to legacy
work — legacy code arguably offers *more* opportunity to practice it than
greenfield work, because the code and its real tradeoffs are already
concretely visible rather than speculative.

**Group Methods**: list every method on the class, with its visibility, and
look for names that cluster by evident purpose. This is incremental, not
all-or-nothing — you don't need to categorize every method, just find
responsibilities "a bit off to the side" of the main one, and it's fine to
defer actually extracting a class until you need to touch one of those
methods anyway. A useful team exercise: post the method-name list on a
poster board in a team room and let people mark up candidate groupings over
time, turning naming and grouping into an ongoing group conversation rather
than a single up-front analysis session.

Other heuristics for the same goal work at different levels of the code:
[looking at what a class hides](testing-private-methods.md) (many
private/protected methods often signal another class trying to get out),
[looking for decisions that can change](decisions-that-can-change-heuristic.md)
inside method bodies, and
[feature sketches](feature-sketches.md) for a more structural, dependency-
driven view of the same class.
