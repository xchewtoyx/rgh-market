---
type: concept
title: "Refactoring: Replace Query with Parameter"
description: >
  Push an internal reference a function makes into its enclosing scope —
  typically a mutable global — out to an explicit parameter instead,
  trading a more unwieldy call site for reduced coupling and restored
  referential transparency.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11"
---

The inverse of [Replace Parameter with Query](replace-parameter-with-query.md):
sometimes a function body references something in its enclosing scope that
you're unhappy about — a global variable, or an element from the same
module you intend to relocate later. The fix is to replace that internal
reference with a parameter, pushing responsibility for resolving it out to
the *caller*. This is fundamentally a dependency-management move, aimed at
breaking the function's coupling to whatever it was internally reaching
for.

**The inherent tension**: converting everything to parameters produces
long, repetitive parameter lists, while leaving things as shared scope
produces coupling between functions. Like most tricky design decisions,
it's not something that can be reliably gotten right once — which is
exactly why fluency with both directions of this refactoring pair matters:
having both well understood means never being stuck with an earlier
allocation-of-responsibility decision.

**Ties directly to referential transparency**: if a function reaches into
scope for something that isn't referentially transparent (a mutable
global, most commonly), the containing function inherits that same lack of
transparency. Moving that element to a parameter fixes this, at the cost of
pushing responsibility onto the caller. This is the tool for "purifying"
parts of a program toward a common architectural pattern: modules built
from pure functions, wrapped by a thin layer handling I/O and other
variable or impure concerns — making the pure core easier to test and
reason about. This is not a pure win: moving a query to a parameter
complicates the caller's life, working against the general design bias
toward easy-to-use interfaces for callers.

**Mechanics**: use [Extract Variable](extract-variable.md) on the "query"
expression to separate it from the rest of the function body. Apply
[Extract Function](extract-function.md) to everything in the body *except*
the query, giving the new function a temporary, easily-searchable name.
Use [Inline Variable](inline-variable.md) to remove the extracted variable,
folding the query expression back inline at its one remaining use — the new
function's call site. Apply [Inline Function](inline-function.md) to the
*original* function, propagating the query expression out to every caller.
Rename the new function to the original's name.

A class whose methods all end up referentially transparent this way — same
arguments always producing the same result, with no remaining internal
reaching into mutable external state — becomes dramatically easier to test
and reason about, even in a language that can't structurally enforce
immutability. A class merely *designed* to signal and encourage that
property is often good enough in practice.
