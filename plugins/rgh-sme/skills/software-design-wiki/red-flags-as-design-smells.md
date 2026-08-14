---
type: concept
title: Red Flags as Design Smells
description: >
  A red flag is an observable pattern in code that signals it is probably
  more complex than it needs to be, used as a trigger to stop and look for an
  alternate design rather than a defect in itself.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 1"
---

Design problems are easier to spot in someone else's code than your own, which
is part of why code review works. Red flags give that review a name to reach
for: recognizable signs — such as a class doing too many unrelated things, a
change that has to touch many files, or a method whose name doesn't reveal
what it actually does — that code is probably more complicated than it needs
to be.

The right response to spotting a red flag is to stop and generate at least one
alternate design before committing to a fix; see
[design it twice](design-it-twice.md). Settling for the first fix that occurs
to you skips the step where most of the learning — and most of the complexity
reduction — actually happens.

As with any design heuristic, red flags can be taken too far: not every
deviation from a clean pattern is a real problem, and chasing every red flag to
its extreme can itself produce an over-engineered design. Judgment about
which red flags matter in a given context is part of the skill.

Most red flags are spotted by inspection, one file at a time. Some of the
costliest ones only show up at the scale of *several* files' relationships
to each other, and some are only visible in version-control history rather
than the code itself — see [architecture debt hotspot
anti-patterns](architecture-debt-hotspot-anti-patterns.md) and
[evolutionary coupling](evolutionary-coupling.md) for red flags that
inspection alone can't find.
