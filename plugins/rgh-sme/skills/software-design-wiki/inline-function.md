---
type: concept
title: Inline Function
description: >
  When a function's body is exactly as clear as its name, the indirection
  is pure overhead — remove it by pasting the body into every call site and
  deleting the function.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6 (formerly Inline Method; inverse of Extract Function)"
---

The mirror image of [Extract Function](extract-function.md): when a
function's body is exactly as clear as its name — no semantic distance left
to bridge — the indirection is pure overhead and should be removed:
"needless indirection is irritating." Two other common triggers beyond that
base case: a cluster of badly-factored functions, which you inline all
together into one big function and then re-extract along better lines; and
a chain of functions doing nothing but delegate to one another, where you
"get lost in all the delegation" — inlining flushes out which indirections
were actually earning their keep versus which were noise, similar in spirit
to what [Middle Man](pass-through-methods.md) diagnoses at the class level.

**Mechanics**: confirm the function isn't polymorphic (a method overridden
by subclasses can't safely be inlined this way); find every caller; replace
each call site with the function's body, testing after each replacement —
it doesn't have to happen all at once, tricky spots can be deferred; delete
the function definition. A function that mutates an output parameter isn't
pure cut-and-paste to inline; the safer fallback is inlining one statement
at a time (Move Statements to Callers) rather than the whole body in one
shot.
