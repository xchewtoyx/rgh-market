---
type: concept
title: Skeletonize Methods vs. Find Sequences
description: >
  Two opposite ways to extract from a conditional-heavy method — split
  guard from body to prepare for reworking control structure, or keep
  guard and body together to reveal a linear sequence of steps — chosen by
  whichever design insight the extraction itself surfaces in the moment.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

Two structural strategies for breaking down a
[monster method](monster-methods.md), explicitly in tension with each other:

**Skeletonize Methods** — when a conditional's guard and body are both
candidates for extraction, extract them into **two separate methods** (a
predicate plus an action). This leaves the original method as a bare
skeleton of control flow and delegated calls, better positioned for later
reorganizing the control structure itself.

**Find Sequences** — the opposite move: extract the guard *and* body
**together** as one method wrapping the whole conditional. This can instead
reveal that the surrounding code is really just a linear sequence of such
steps, clarifying the method's overall shape without touching its control
structure at all.

These are acknowledged as contradictory advice on their face: "I often go
back and forth between skeletonizing methods and finding sequences. Chances
are, you will, too." Rough guidance: skeletonize when the control structure
itself will likely need reworking later; look for sequences when surfacing
an overarching sequence would clarify the code more than separating
condition from action would. A loose correlation (not a rule): bulleted
methods tend to favor finding sequences, snarled methods tend to favor
skeletonizing — but the real deciding factor is whatever design insight the
extraction itself reveals in the moment, not a fixed rule applied in
advance.
