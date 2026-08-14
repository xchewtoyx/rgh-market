---
type: concept
title: "Refactoring: Split Variable"
description: >
  A variable reassigned to hold more than one unrelated piece of
  information over its lifetime should be split into one variable per
  responsibility — reusing one name for two different things is simply
  confusing to read, unlike a genuine accumulator that legitimately
  reassigns itself.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 9 (formerly Remove Assignments to Parameters, Split Temp)"
---

Some variables are legitimately reassigned repeatedly by design: loop
counters, and **collecting variables** that accumulate a result across a
method (sums, string concatenation, stream writes, pushing into a
collection). Other variables are reassigned only because they're being used
to hold more than one, unrelated piece of information over their lifetime —
each reassignment marking a new "responsibility." Rule: any variable serving
more than one responsibility should be split into one variable per
responsibility. This is one of several mitigations for the
[mutable data](mutable-data-smell.md) smell.

**The distinguishing test** for a collecting variable that should be *left
alone*: does each assignment look like `x = x + something` — building on
its own prior value? If so, it's a legitimate accumulator, not a candidate
for splitting. This applies to reassigned input parameters too, not only
local variables — a function that reassigns its own parameter to double as
its eventual return value is hiding two roles behind one name, even though
call-by-value semantics make the reassignment invisible to the caller; the
reader working through the function still has to track both roles.

**Mechanics**: rename the variable at its declaration and first assignment
to reflect only that first use (skip the whole refactoring if the
"reassignment" is actually a collecting-variable pattern). Make the
newly-named variable immutable if the language allows. Update every
reference between the declaration and the *next* assignment to use the new
name. Test. Repeat this same rename-and-redirect procedure at each
subsequent assignment point, working forward until the final assignment,
each stage getting its own new variable name and its own test pass.

When picking names for the split pieces, pick the name that reflects the
*intent* of a given reference, not merely whichever variable happens to
hold the same value at that point in the code — two variables can
momentarily agree in value while still meaning conceptually different
things.
