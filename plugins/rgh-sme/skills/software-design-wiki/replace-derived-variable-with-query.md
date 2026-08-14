---
type: concept
title: "Refactoring: Replace Derived Variable with Query"
description: >
  Delete a stored variable that could just as easily be computed on demand
  from other data — a calculation documents its meaning more clearly and
  can never drift out of sync the way a stored copy can if an update site
  is ever missed.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 9"
---

[Mutable data](mutable-data-smell.md) is one of the biggest sources of
problems in software: updates to data couple distant parts of a program
together in ways that are easy to miss, producing knock-on effects that are
hard to trace. Since eliminating mutable data entirely usually isn't
realistic, the practical goal is to minimize its scope wherever possible.
Deleting any variable that could just as easily be computed on demand is a
concrete, high-leverage way to do that — the value it held is a form of
**data duplication**, distinct from the more commonly discussed code
duplication, and duplicated data can drift out of sync exactly the way
duplicated code can.

**Stated exception**: when the source data feeding the calculation is
itself immutable (or the result can be forced immutable), pre-computing and
storing a derived structure is equally reasonable to keep as a plain
calculation — there's no drift risk if nothing can change underneath it.
There's a duality here between [Combine Functions into
Class](combine-functions-into-class.md) (an object wrapping a data
structure with a series of calculated properties) and [Combine Functions
into Transform](combine-functions-into-transform.md) (a function
transforming one data structure into another) — two views of the same
underlying idea. The class/object route wins decisively once the source
data can actually change, since otherwise the derived structure's lifetime
and staleness would need separate management; if the source is immutable,
or the derived structure is short-lived, either approach works equally
well.

**Mechanics**: identify every point where the variable gets updated — if
there's more than one and they interact, apply
[Split Variable](split-variable.md) first to cleanly separate them. Write a
function that calculates the variable's value from scratch. Add an
[assertion](introduce-assertion-for-fail-fast.md) checking that the stored
variable and the freshly-calculated value always agree at the point(s) of
use (encapsulating the variable first via
[Encapsulate Variable](encapsulate-variable.md) if there's no natural home
for the assertion yet). Test — this is the step that actually validates the
underlying hypothesis that the derivation is safe to inline; if the
assertion never fires, that's the evidence needed to proceed confidently.
Once confirmed, replace every reader of the stored variable with a call to
the new calculating function. Test again. Finally, apply
[Remove Dead Code](delete-unused-code.md) to delete the now-unused variable
declaration and its update sites.

Not every derived value needs to be collapsed all the way down to a single
inline expression — a named intermediate query is sometimes worth keeping
on its own for the clarity its name provides, even once it's no longer
backed by a stored field.
