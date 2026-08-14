---
type: concept
title: Combine Functions into Class
description: >
  When several functions closely operate on a shared body of data passed
  around explicitly, forming a class makes that shared context explicit and
  gives every derived value a live, on-demand recomputation instead of a
  stale precomputed one.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6"
---

Classes bind data and functions into a shared environment. When several
functions closely operate on a shared body of data — often passed as
arguments to each of them individually — that's a signal to form a class:
it makes the shared context explicit, shrinks argument lists (members no
longer need explicit passing), and gives the rest of the system a single
reference to hand around. It also creates a natural place to notice and pull
in other related computation as new methods later.

The key differentiator against the alternative organizing move, [Combine
Functions into Transform](combine-functions-into-transform.md), is
mutability: a class handles the case where the underlying source data gets
updated over time, because its methods recompute derived values on demand
from current state — a transform's precomputed derived fields go stale if
the source changes after enrichment. A class is required outright, rather
than a simpler grouping like nested functions, whenever more than one
function in the group needs to be exposed to outside collaborators, and is
generally preferred even for one function since nested functions are hard to
test in isolation.

**Mechanics**: apply [Encapsulate Record](encapsulate-record.md) to the
shared data record, turning
it into a class (first applying [Introduce Parameter
Object](introduce-parameter-object.md) if the shared data isn't already one
record). Move each function that uses the common record into the new class
via [Move Function](move-function.md) — parameters that are now members drop out of the
argument lists. Inline logic manipulating the data can be pulled out first
via [Extract Function](extract-function.md), then moved the same way.

A derived value moved onto the class this way is naturally exposed as a
read-only accessor property rather than a method call, so from the caller's
perspective it's indistinguishable from a plain stored field — an instance
of the **Uniform Access Principle**: callers can't tell, and shouldn't need
to care, whether a value is stored or derived.
