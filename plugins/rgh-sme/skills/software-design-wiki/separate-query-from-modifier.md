---
type: concept
title: "Refactoring: Separate Query from Modifier"
description: >
  Split a function that both returns a value and mutates state into a pure
  query and a pure command, migrating callers to call the query when they
  need the value and the command when they need the effect — the
  mechanical procedure for enforcing Command/Query Separation on existing
  code.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11"
---

A function that returns a value with **no observable side effects** is
unusually valuable: it can be called as often as needed, freely moved
around within a calling function, and is easier to test. This is the
refactoring that enforces [Command/Query Separation](command-query-separation.md)
on a function found violating it — not treated as an absolute rule to
follow blindly, but as a consistent refactoring target whenever a
value-returning function also mutates state.

An important nuance on "observable": caching a computed value in a field to
speed up repeated calls does technically change object state, but this is
not counted as an observable side effect, because any sequence of queries
still returns identical results regardless of the caching — the rule
targets externally visible behavioral changes, not internal implementation
detail.

**Mechanics**: copy the function, naming the copy after its query aspect —
if the original result was being stored in a variable, that variable's
name is often a good hint for the new name. Strip all side effects out of
this new query copy. Run static checks. At each call site that actually
uses the return value, replace the original call with a call to the new
query, followed immediately by a (return-value-discarding) call to the
original function beneath it — test after each site. Once every
value-using call site has been migrated, strip the return value out of the
original function entirely. Test.

A frequent follow-up: the original modifier and the new query often end up
duplicating logic, which is worth tidying — typically via
[Substitute Algorithm](substitute-algorithm.md), having the modifier call
the new query internally instead of re-deriving the same result. This turns
the modifier into an expression purely in terms of the query, eliminating
the duplication entirely.
