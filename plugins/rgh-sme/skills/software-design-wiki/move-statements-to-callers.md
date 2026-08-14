---
type: concept
title: "Refactoring: Move Statements to Callers"
description: >
  Relocate a shared function's tail of behavior out to each of its callers
  once that behavior needs to start varying per caller, letting each copy
  evolve independently after the split.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

Function boundaries are abstractions, and abstractions drift out of
alignment as software's capabilities change — what was once one cohesive
unit of behavior can become a mix of two or more different things as the
codebase evolves. The specific trigger for this refactoring is behavior
currently shared by several callers that needs to start *varying* per
caller. The fix is to relocate the varying part out of the shared function
and into each caller directly (using [Slide Statements](slide-statements.md)
first to push the soon-to-be-extracted code to the very start or end of the
function, making the split boundary clean), after which each caller is
free to evolve its own copy independently. This is the inverse of
[Move Statements into Function](move-statements-into-function.md).

**Scope caveat**: this refactoring suits small, localized boundary
adjustments. If the caller/callee split genuinely needs a *complete*
rework rather than peeling off one varying tail, the better move is to
[Inline Function](inline-function.md) everything together first, then
re-slide and re-extract fresh boundaries from scratch — the same
"collapse then re-split" strategy used by
[Inline Class](inline-class.md) / [Extract Class](extract-class.md).

**Mechanics**: for the simplest case (one or two callers, a simple
function), just cut the lines to move and paste them into each caller
directly, fitting as needed; test and stop there. For the more involved
case: apply [Extract Function](extract-function.md) to everything you want
to *keep* inside the shared function — extract the *stable* part, not the
varying part — into a temporarily-but-easily-greppable-named function. If
the function is a polymorphic method overridden by subclasses, this
extraction must be done identically across every override until the
remaining method body is byte-for-byte the same everywhere, at which point
the now-identical subclass overrides can be deleted entirely. Then apply
Inline Function on the *original* function at each call site — this is
what physically moves the varying tail out to sit beside each caller.
Finally, [Change Function Declaration](change-function-declaration.md)
renames the extracted (stable) function back to the original's name, or a
better one.
