---
type: concept
title: Stay Strategic When Modifying Existing Code
description: >
  A mature system's actual design is shaped far more by the accumulation of
  changes made during its evolution than by its initial design, so every
  modification should aim to leave the system looking as if it had been
  designed from the start with that change in mind.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 16"
---

Applies [strategic vs. tactical programming](strategic-vs-tactical-programming.md)
specifically to the act of modifying existing code. The default tactical
instinct when fixing a bug or adding a feature is "what's the smallest
possible change that does what I need?" — sometimes rationalized as caution
around unfamiliar code, but functionally this is tactical programming: each
minimal patch quietly adds a special case, a dependency, or some other sliver
of complexity, and these accumulate change by change across the system's
evolution. See
[complexity accumulates incrementally](incremental-accumulation-of-complexity.md).

The strategic alternative: after each change, the system should look as if
it had been designed from the start with that change already in mind.
Concretely — resist the reflexive quick fix; ask whether the existing design
is still the right one given the new requirement; if not, refactor toward the
best design before or as part of making the change, so the design keeps
improving with every modification instead of eroding. Even when a specific
change doesn't strictly require refactoring, actively look for design
imperfections nearby and fix them opportunistically while already in that
code. There's no neutral option here: if you're not making the design
better, you are probably making it worse.

Real-world tension is acknowledged: sometimes a proper multi-month refactor
genuinely isn't affordable against a two-hour quick fix under deadline
pressure, or would ripple out to other teams' code, making it impractical
regardless of merit. Even so, resist the compromise as far as possible, via
the self-check "is this the best I can possibly do to create a clean system
design, given my current constraints?" Concrete tactics: look for a cheaper
near-equivalent to the full refactor — something almost as clean but doable
in days instead of months — or, if the full refactor truly can't happen now,
get organizational buy-in to schedule it explicitly for after the current
deadline rather than letting it evaporate. At the team level: budget a
standing fraction of total effort specifically for cleanup and refactoring
work, on the premise that it pays for itself over the long run — see
[how much to invest in design](design-investment-level.md).
