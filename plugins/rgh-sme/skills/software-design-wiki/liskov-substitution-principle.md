---
type: concept
title: Liskov Substitution Principle
description: >
  Objects of a subclass should be substitutable for objects of their
  superclass throughout the code without callers getting silently wrong
  results, illustrated by the classic Rectangle/Square counterexample.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

"Objects of subclasses should be substitutable for objects of their
superclasses throughout our code. If they aren't we could have silent errors
in our code." The classic counterexample: subclassing `Square extends
Rectangle` and inheriting `setWidth`/`setHeight` unmodified breaks the
invariant that setting width=3, height=4 yields area=12 — callers relying on
`Rectangle`'s contract get silently wrong results, whether from the
unmodified inherited setters or from overrides that "unsquare" a square to
compensate.

No fully mechanical test exists for LSP conformance — it's defined relative
to what a class's actual clients expect — but two rules of thumb help:

1. Avoid overriding concrete methods when possible.
2. If you must override one, try to still call the overridden method from
   within the override.

The risk of violating rule 1 is concrete: code elsewhere holding a reference
typed as the base class may be silently operating on a subclass instance
with materially different semantics, and a reader inspecting only the base
class's method would be misled about actual runtime behavior. See
[programming by difference](programming-by-difference.md) for a worked
example that violates rule 1 outright (overriding a concrete method wholesale)
and the concrete confusion that follows from it, and
[normalized hierarchies](normalized-hierarchy.md) for the structural property
LSP-respecting hierarchies tend to have.
