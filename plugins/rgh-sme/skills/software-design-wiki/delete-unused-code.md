---
type: concept
title: Delete Unused Code Rather Than Hoarding It
description: >
  Confirmed-unused code should be deleted outright, not commented out or
  preserved out of sentiment — version control already remembers it, and
  dead code's only real cost is the comprehension time it silently demands
  from every future reader.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 16"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8, Remove Dead Code"
---

If code is confirmed unused, delete it — don't preserve it out of a sense
that "someone spent time writing it," and don't comment it out "just in
case." Version control already preserves the history; hoarding dead code in
the live source only adds to the reading burden for everyone who encounters
it afterward, for no retrievability benefit that version control doesn't
already provide.

Unused code costs essentially nothing at runtime — modern compilers
routinely strip it, and a few unused lines don't meaningfully affect memory
or speed. The real cost is comprehension: dead code carries no visible
marker saying "you can ignore this," so anyone reading the system still has
to spend time understanding what it does and why touching it doesn't seem
to affect real behavior. Once code has no more callers, delete it outright
rather than keeping it "just in case" — a breadcrumb comment noting what was
removed and in which revision is rarely worth the trouble, and going back to
resurrect deleted code from history is rare enough in practice not to plan
around. Commenting code out instead of deleting it is a habit worth
retiring entirely now that version control is ubiquitous: it made sense
before, but not anymore.

**Mechanics**: if the dead code could plausibly still be referenced from
outside the current scope — most obviously, a full standalone function —
search for callers first to confirm it's truly unused. Remove it. Test.
