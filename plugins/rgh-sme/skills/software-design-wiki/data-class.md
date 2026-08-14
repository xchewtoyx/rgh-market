---
type: concept
title: "Code Smell: Data Class"
description: >
  A class that is just fields plus getters and setters and nothing else is
  usually a sign that behavior belonging with that data is sitting in the
  wrong place — with a carved-out exception for genuinely immutable results.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

A Data Class is a "dumb data holder" — just fields plus getters and setters
— typically manipulated in excessive procedural detail by other classes that
should instead be delegating that work to it. If fields are still public,
[Encapsulate Record](encapsulate-record.md) is the immediate fix; Remove Setting Method applies to
any field that shouldn't change from outside. The deeper cure is to trace
where the getters and setters are actually used and [Move
Function](move-function.md) — or first
[Extract Function](extract-function.md), then move — the surrounding behavior into the data class
itself; the smell usually indicates behavior sitting in the wrong place, an
instance of the same diagnosis behind
[encapsulation as a tool, not a goal](encapsulation-is-a-tool-not-a-goal.md).

Important carve-out: a genuinely immutable result record — the intermediate
data structure a [Split Phase](split-phase.md) computation produces, for
example — is fine as a plain data holder. Immutable fields need no
encapsulation against unwanted external mutation, and derived values can be
plain fields rather than computed accessors, since there's no mutation to
guard against invalidating them.

When this smell isn't confined to one class but pervades a whole object
model — every domain object a data class, all behavior siphoned off into
matching "service" classes — see [anemic domain model](anemic-domain-model.md).
