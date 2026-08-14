---
type: concept
title: Extract to the Current Class First, Even When It Belongs Elsewhere
description: >
  When an extracted chunk's natural name repeats one of its own parameters,
  that's a sign it belongs on a different class — but extract it to the
  current class first anyway, keeping the cross-class move as a separate,
  later, safely undoable step.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

A strong signal that an extracted chunk actually belongs on a *different*
class is that its most natural name keeps repeating one of its own
parameter or variable names — code operating on an `order` variable that
naturally wants to be called `recalculateOrder` is hinting that it really
belongs on `Order` itself, perhaps renamed `recalculate` once moved (with
the caveat of checking for and reconciling any existing same-named method
there).

The recommendation is to resist moving it immediately: keep the admittedly
awkward name and extract to the **current** class first. This keeps the move
small and safely undoable, and lets you validate that you've isolated the
right chunk before committing to a cross-class move — the relocation to the
"right" class, once the direction is clearer, can always happen as its own
later step. This is the same underlying discipline as
[designs emerge from zealous duplication removal](duplication-removal-as-emergent-design.md):
work in the smallest safe increment and defer the structural commitment
until it's actually warranted by what the extraction reveals.

Individual small extractions look inconsequential in isolation, but
accumulate into a clearer view of the method's real structure — sequences
and better organizations become visible only after several small pieces are
removed, and this is argued to be safer and more reliable than attempting
to carve a monster method into a few large chunks from the outset, since
large-chunk extraction is more error-prone and likely to lose exactly the
small details that make the code actually work. Expect some early
extraction choices to turn out suboptimal once more structure is visible —
undoing and re-extracting differently is normal, not wasted effort, since
even a discarded extraction provides real insight into both the old design
and a better path forward.
