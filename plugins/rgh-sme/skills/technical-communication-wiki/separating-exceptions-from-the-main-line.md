---
type: concept
title: Separate Exceptional Cases From the Main Line, Don't Interleave Them
description: >
  When a document has one primary path and several minor exceptions,
  pull the exceptions out to their own clearly marked spot instead of
  weaving them into the main explanation at equal weight, so the
  reader's model of "what this is really about" isn't interrupted.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler), ch. 10, Replace Nested Conditional with Guard Clauses"
---

Not every branch in an explanation carries equal weight. Some describe two genuinely alternative, equally normal cases the reader might be in — those belong side by side, given roughly equal space, since the reader really does need to weigh both. But often what looks like a branch is really one main line of explanation with a handful of minor exceptions nested inside or around it: a procedure with an edge case, a rule with a small number of special conditions where it doesn't apply. Presenting that second kind of content as if it were the first kind — a structurally symmetric "if this, then that; otherwise, this other thing" — misleads the reader about which branch actually matters, and forces them to hold both branches in mind with equal seriousness when only one of them is the point.

The fix, borrowed from the "guard clause" pattern in code (check the unusual condition, handle it, and move on, rather than wrapping the normal case in a conditional around it) is structural: state and dispense with the exception first, in a clearly marked, self-contained spot — a "before you begin" note, a prerequisites list, a short caveat sentence, a troubleshooting aside — and then let the main explanation run uninterrupted, written as if the exception didn't exist, because for the reader who isn't hitting it, it doesn't. This does two things a truly symmetric treatment can't: it signals, structurally, that one path is the default and the other is the exception (the same signal [disclosing limitations early](disclosing-limitations-early.md) sends when limitations are placed early and dispensed with rather than allowed to color the whole piece); and it keeps the main-line explanation legible on its own, since a reader who never needed the exception shouldn't have to read through it to reach the part that mattered to them.

This only applies when the branches genuinely are unequal in importance. Forcing a real two-sided choice — where a reader plausibly needs to weigh both options, not just get past one of them — into an exception-first structure hides the fact that a real decision is being asked of them; that case still calls for side-by-side, equal treatment.
