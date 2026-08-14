---
type: concept
title: Extract Function
description: >
  The deciding question for pulling code into its own function isn't length
  or reuse, it's the semantic distance between what a fragment does and how
  it does it — extract and name for the "what" whenever that distance
  exists.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (formerly Extract Method; inverse of Inline Function)"
---

One of the most common refactorings performed. The deciding question for
whether to carve code into its own function is *not* length-based ("fits on
a screen") or reuse-based ("only extract what's used twice or more") — it's
the **separation between intention and implementation**: if you have to
expend effort figuring out what a fragment does, extract it and name the new
function after the "what." Readers then rarely need to look at the "how"
(the body) at all. This leads naturally to very short functions — even a
single function call is worth extracting if the new name reveals intent
better than the inline expression did. If you can't find a name more
meaningful than the code itself, that's a signal *not* to extract — though
it's fine to try, fail, and inline the attempt back: "as long as I've
learned something, my time wasn't wasted." An existing explanatory comment
on a fragment is a strong hint for what the extracted function's name should
be, and is itself a smell worth acting on — see [comments as a design
diagnostic](comments-as-a-design-diagnostic.md).

**Mechanics**: create a new function named for intent; copy the target code
into it; scan for variables local to the source function that the extracted
code references — pass unmodified ones as parameters, move in declarations
used only inside the extracted code, and for a variable that's *reassigned*
inside the extraction, treat the extraction as a query and assign its result
back to the original name at the call site. If too many locals are being
reassigned inside a candidate extraction, abandon it and first simplify the
surrounding code — extraction should follow simplification, not force it.
Functions should return one value; when a candidate extraction would need to
return several, prefer choosing different extraction boundaries over
bundling values into a returned record.

This is the tests-present counterpart to [extracting with a comment-first
rollback](extract-method-with-comment-first-rollback.md) (for legacy code
you don't yet trust) and to [extracting what you know, guided by coupling
count](extract-what-you-know-and-coupling-count.md) (for legacy code with no
tests at all yet) — all three are the same underlying move, adapted to how
much safety net exists at the time.
