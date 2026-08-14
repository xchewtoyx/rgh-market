---
type: concept
title: "Refactoring: Preserve Whole Object"
description: >
  When code pulls a couple of values out of a record just to pass them
  into a function, pass the whole record instead and let the callee
  derive whatever it needs — shorter parameter lists, resilience to future
  needs, and a natural place to relocate duplicated extraction logic.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11"
---

When code pulls a couple of values out of a record just to pass them into a
function, prefer passing the **whole record** instead and letting the
callee derive whatever it needs internally. Benefits: resilience to future
change — if the callee later needs more data from the same record, the
parameter list doesn't need to change again; shorter, more readable
parameter lists in general; and deduplication — when several call sites
extract-and-pass the same subset of fields, they usually duplicate the
logic for manipulating those fields, and that logic can typically be
relocated into the whole object instead. The main reason *not* to do this:
if the callee shouldn't take on a dependency on the whole record's type —
typically an issue when caller and callee live in genuinely separate
modules that shouldn't know about each other's data shapes.

**Diagnostic framing**: pulling several values out of an object purely to
operate on them is literally the [Feature Envy](feature-envy.md) smell, and
usually signals the logic belongs inside the whole object instead. This
refactoring shows up especially often right after
[Introduce Parameter Object](introduce-parameter-object.md) — once a data
clump has been promoted to a real object, go hunting for remaining
scattered occurrences of the old, unpacked clump and replace them with the
new object. If several pieces of code all only touch the same *subset* of
an object's features, that's a signal for
[Extract Class](extract-class.md) instead. A commonly-missed variant: when
an object calls another method passing several of *its own* fields
individually, the fix is simply passing a self-reference instead.

**Mechanics**: create an empty function with the desired (whole-object)
parameter signature, given a deliberately ugly-but-greppable temporary
name. Fill its body with a call to the *existing* function, mapping the new
whole-object parameter down to the old individual parameters. Run static
checks. Migrate each caller to the new function one at a time, testing
after each — this often leaves some of the caller's own field-extraction
code newly unnecessary, cleanable via
[Remove Dead Code](delete-unused-code.md). Once every caller has moved,
apply [Inline Function](inline-function.md) to fold the original function's
body directly into the new one. Finally, rename the new function and every
caller to the original's name.

**Alternative construction**: when tooling has strong automated
Extract/Inline/Move support, the whole refactoring can be composed purely
from other named refactorings instead of writing the new function's body
freehand: reshape the caller's own code with
[Extract Variable](extract-variable.md) until the desired new function is
already sitting there as an extractable block, apply
[Extract Function](extract-function.md) to produce it at the call site,
then [Move Function](move-function.md) it to where the logic actually
belongs — after which the rest proceeds as in the direct version.
