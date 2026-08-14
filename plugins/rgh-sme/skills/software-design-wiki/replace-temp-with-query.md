---
type: concept
title: "Refactoring: Replace Temp with Query"
description: >
  Turn a once-computed local temp into a method so other code — including
  parts of the same function extracted later — can call it by name instead
  of receiving it as a threaded-through parameter.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7, Encapsulation — Replace Temp with Query"
---

A local temp captures a computed value once so later code in the same
function can refer to it by name instead of repeating the expression.
Promoting that temp to a method (or accessor) instead goes a step further,
for three reasons:

1. **Easier [Extract Function](extract-function.md) later** — once the value
   is a method rather than a local variable, extracting other parts of the
   surrounding function no longer requires threading the variable in as a
   parameter. This is why the refactoring recurs constantly as prep work
   when breaking up long functions.
2. **Stronger boundaries** — pulling the calculation into its own function
   creates a clearer seam between it and the rest of the function, surfacing
   hidden dependencies and side effects that were easy to miss inline.
3. **Deduplication** — if the same temp-calculation pattern shows up in
   multiple functions, converting it to a shared method eliminates the
   duplicate logic outright.

This works best inside a class, which supplies a natural shared context
(`this`) for the extracted method — see [Extract Variable](extract-variable.md)
on why objects make this promotion cheap. Outside a class, a top-level
function version risks accumulating too many parameters, eroding the
benefit; nested functions dodge the parameter problem but limit how widely
the extracted logic can be reused across sibling functions.

**Applicability constraint**: not every temp qualifies. The variable must be
calculated once and only read afterward (a single assignment is simplest,
though a small lump of a few assignments can still be extracted wholesale as
long as *all* of it moves into the query together). Critically, the
calculation must be **idempotent relative to when it's read later** — this
rules out a variable holding a *snapshot* of a value that may since have
changed (e.g. one literally named `oldAddress`); re-invoking the "same"
calculation later would not reproduce the originally captured value.

**Mechanics**: confirm the variable is fully determined before use and that
recomputing it would yield the same value every time it's referenced (the
snapshot-safety check above). If the variable isn't already read-only, make
it so, and test — this doubles as a check that no reassignment was missed.
Extract the assignment's right-hand side into a function (a temporary name
if the function can't share the variable's name yet). Confirm the extracted
function is side-effect-free; if it isn't, apply [Separate Query from
Modifier](separate-query-from-modifier.md) first. Test. Finally, apply
[Inline Variable](inline-variable.md) to remove the now-redundant temp
entirely.

A worked example splits an `Order.price` getter's two local temps,
`basePrice` and `discountFactor`, into `get basePrice()` and `get
discountFactor()` accessors this same way — including a case where the
"one calculation" being extracted actually spans two statements (an initial
assignment plus a conditional adjustment) that must
[move into the new method](move-statements-into-function.md) together as a
single logical value. The end state reduces
`get price()` to `return this.basePrice * this.discountFactor;` — a
one-liner where every previously inline calculation is now an
independently named, independently reusable, independently testable method.
