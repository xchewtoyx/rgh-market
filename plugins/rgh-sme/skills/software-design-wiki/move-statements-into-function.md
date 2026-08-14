---
type: concept
title: "Refactoring: Move Statements into Function"
description: >
  Fold code that runs identically right before or after every call to a
  function into the function itself, once that code is recognized as
  conceptually part of what the function does rather than incidental to
  the call site.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

A direct application of "remove duplication": if the same code runs every
time right before or after calling some function, fold that repeating code
into the function itself so future changes only need to happen in one
place. If the duplicated code should later need to vary again by call site,
it can just as easily be pulled back out later with
[Move Statements to Callers](move-statements-to-callers.md) — the two are a
reversible pair.

**The deciding factor for whether to fold statements in**: do they
conceptually belong as part of what the called function does? If yes, use
this refactoring. If the statements should still travel with the call but
don't semantically belong *inside* the function, plain
[Extract Function](extract-function.md) on the statements-plus-call is the
better tool — same underlying moves, just without the final inline-and-
rename step. It's not unusual to do the simpler Extract Function first and
only later, after further reflection, decide the code actually does belong
inside and finish the fuller move.

**Mechanics**: if the repeating code isn't already adjacent to the call,
use [Slide Statements](slide-statements.md) to bring it alongside first. If the target function
only has one caller, this is trivial: cut, paste into the target, test,
done. With multiple callers: apply Extract Function at one call site,
extracting both the call and the surrounding statements to move under a
deliberately temporary-but-greppable name; migrate every other caller to
use this new function one at a time, testing after each; once all callers
are converted, apply [Inline Function](inline-function.md) to fold the
*original* target function entirely into the new one, removing the
original; finally rename the new function back to the original's name (or a
better one, if one presents itself).
