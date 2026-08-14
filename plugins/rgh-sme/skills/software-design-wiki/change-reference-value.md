---
type: concept
title: "Refactoring: Change Reference to Value"
description: >
  Turn a nested object that's mutated in place into one that's replaced
  wholesale on every update, opening the door to making it a proper
  immutable value object — easier to hand out safely and to duplicate
  without tracking shared identity.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 9"
---

A nested object or data structure can be treated either as a **reference**
(updates mutate the shared inner object in place, visible to everyone
holding it) or as a **value** (an update replaces the whole inner object
with a new one carrying the desired change). Choosing the value style opens
the door to making that inner class a proper immutable value object, and
immutable data is easier to reason about generally: it can be handed out to
other parts of the program with no risk it changes underneath the holder
unexpectedly, and it can be freely duplicated without needing to track or
manage shared memory identity. This is especially valuable in distributed
and concurrent systems, and is one of the standard mitigations for the
[mutable data](mutable-data-smell.md) smell.

**Boundary case for not doing this**: if the whole point is that several
owners should all see a change to one shared object, it needs to remain a
genuine reference — see
[Change Value to Reference](change-value-to-reference.md) for the inverse
move, needed when independent copies of what's conceptually one entity have
started drifting out of sync.

**Mechanics**: confirm the candidate class is (or can become) immutable.
Remove every setter (Remove Setting Method). Add a value-based equality
method built from the object's fields — most language runtimes provide an
overridable equality hook for this; overriding equality almost always also
requires overriding the paired hash-code method, so hash-based collections
keep working correctly with the new value semantics. Write a dedicated test
that constructs two *independently created* instances with the same field
values and asserts they compare equal — this is the property that
distinguishes value equality from a language's default reference equality,
and it's the one thing worth being certain the tests actually exercise. If
the value is shared by multiple clients rather than one, the same procedure
applies but touches more call sites, and it's worth also testing non-equal
values and comparisons against unrelated types and null.
