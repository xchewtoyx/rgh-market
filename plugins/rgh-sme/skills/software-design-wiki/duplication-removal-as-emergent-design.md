---
type: concept
title: Designs Emerge From Zealous Duplication Removal
description: >
  A change needed in a dozen near-identical places doesn't require a
  reengineering effort — start with the smallest visible duplication and
  work outward mechanically, and the resulting design is often what was
  implicit in the code all along, not something newly invented.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 21"
---

The frustration of a change requiring the same edit in a dozen similar
places makes reengineering feel like the only real fix, and that feels too
big to justify. Counter-framing: removing duplication doesn't require a
grand reengineering effort — it's incremental work doable "in small chunks"
as you go, as long as duplication isn't simultaneously being reintroduced
elsewhere.

**Start with the smallest visible piece of duplication**, not a plan for the
entire end-state class structure. Stepping back to design the whole target
structure up front is an explicit anti-pattern to catch yourself doing —
clearing small duplication tends to make larger-scale duplication easier to
see afterward. A worked sequence on two near-identical wire-protocol command
classes shows the shape this takes mechanically: extract a small repeated
statement pair into a helper method; notice the same pattern recurring in a
sibling class and pull the helper up to a shared superclass; notice the
containing methods now share the same *shape* and extract their differing
part into its own method, leaving identical wrapper bodies that can then be
pulled up too; replace the one remaining per-subclass difference with an
abstract method each subclass overrides. The generalizing rule this
illustrates: **"When two methods look roughly the same, extract the
differences to other methods. When you do that, you can often make them
exactly the same and get rid of one."** Each pass toward more generality
(a single field, then a list of fields) makes the next duplication easier to
spot, until the original subclasses shrink to little more than a constructor
and a one-line override.

**The result is mostly mechanical, not creative** — nearly every step is
just paying attention to duplication and removing it; naming the newly
extracted methods is the only genuinely creative work. The underlying
concepts (a "field," a message "body") were already implicit in the
original, duplicated code — duplication removal doesn't invent a design so
much as reveal one that was struggling to get out: "moving the code closer
to its essence, what it really was." Broader claim: **designs emerge** from
zealous duplication removal — you don't have to plan most of an
application's extension points in advance. See
[orthogonality and the open/closed principle](orthogonality-and-open-closed-principle.md)
for the design property this process tends to produce, and
[thinness after deduplication is fine](thinness-after-deduplication-is-fine.md)
for why the resulting thin classes shouldn't be collapsed further just
because they look small.
