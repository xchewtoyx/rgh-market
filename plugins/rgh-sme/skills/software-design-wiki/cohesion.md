---
type: concept
title: "Cohesion: Unity of Purpose Within a Module"
description: >
  Cohesion is the probability that a change scenario affecting one of a
  module's responsibilities also affects another responsibility in the
  same module — high cohesion means a module's contents genuinely belong
  together.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 8 (concept traces to 1960s structured-design theory)"
---

Formally: cohesion measures how strongly a module's responsibilities are
related — the probability that a change scenario touching one
responsibility inside a module also touches another responsibility housed
in that *same* module. High cohesion is good: it means a given change is
unlikely to spill across the module's own internal boundary into unrelated
territory it happens to share space with. Low cohesion is the opposite —
a module holding several responsibilities that change for unrelated
reasons, so any one of those reasons only ever exercises part of the
module while leaving the rest untouched and along for the ride.

This is the structural definition behind the [Single Responsibility
Principle](single-responsibility-principle.md)'s informal "one purpose, one
reason to change," and it's the diagnostic question underlying [Divergent
Change](divergent-change.md): when a module gets changed in different ways
for different, unrelated reasons, that's low cohesion made visible.

**Fixing low cohesion**: remove the responsibilities that aren't affected
by the changes you're actually anticipating — i.e., split them out into
their own module — rather than trying to force every responsibility a
module happens to hold into permanent unity. A useful identification
technique: hypothesize a handful of likely-change scenarios; if a scenario
only ever touches part of a module, the untouched part is probably a
separable responsibility; if a scenario spans several modules, the
responsibilities it touches may actually belong grouped together in one.

See [coupling](coupling.md) for the complementary measure — how much a
change to one module drags along a change to another — and note the real
tension between the two: abstracting a common service out of several
modules can reduce their coupling to each other while simultaneously
reducing each module's own cohesion, since the abstracted piece may not
share a unifying purpose with what's left behind. Neither move is free;
both are worth weighing against [what the added structure actually
buys](design-cost-benefit-of-infrastructure.md).
