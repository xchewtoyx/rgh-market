---
type: concept
title: Normalized Hierarchy
description: >
  A class hierarchy where no class overrides a concrete method inherited
  from a superclass, so "how does this class do X?" always has one
  unambiguous, inspectable answer.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 8"
---

A **normalized hierarchy** is one where every method is either fully
implemented in exactly one place, or declared abstract and implemented only
in subclasses — no class overrides a concrete method it inherits. The
benefit: "How does this class do X?" always has one unambiguous answer found
by inspection, with no risk of a hidden subclass override silently changing
the answer at runtime.

Occasional concrete overrides that don't violate the
[Liskov Substitution Principle](liskov-substitution-principle.md) aren't
inherently harmful — normalization is a property worth checking periodically
rather than an absolute rule to enforce everywhere, and it's especially worth
checking "when we prepare to separate out responsibilities," since a
drifted, non-normalized hierarchy makes it harder to tell which behavior
actually belongs to which class before splitting one up.
[Programming by difference](programming-by-difference.md) trades this
property away deliberately as a fast initial move, with the intent to
restructure once the tradeoff becomes visible.
