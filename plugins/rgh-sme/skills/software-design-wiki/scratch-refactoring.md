---
type: concept
title: Scratch Refactoring
description: >
  Deliberately refactor unfamiliar code purely to learn it, with zero
  intention of keeping the result — then throw the changes away rather than
  committing them.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 16"
---

Check out from version control and freely extract methods, rename things,
and move code around — without writing tests first, since nothing here is
meant to survive — purely as a way to learn unfamiliar code. When you're
done, **throw the changes away** rather than committing them. A skeptical
developer who thought this "wasteful" was converted after a single half-hour
scratch session taught them "an incredible amount" about a piece of code
they'd otherwise have had to read passively.

Two named risks: (1) you might make an outright mistake mid-refactor and walk
away with a *false* belief about what the system actually does, since
nothing here is checked by tests — this can bite you later if you don't
verify surprising conclusions against the real, unmodified code. (2) you can
become too attached to the scratch version's structure and lose openness to
better structures discovered later, once more of the system's context is
understood. The point of scratch refactoring is understanding, not
commitment to any specific end-state — it's a reading aid, not a design
proposal.
