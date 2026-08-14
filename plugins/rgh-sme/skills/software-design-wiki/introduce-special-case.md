---
type: concept
title: "Refactoring: Introduce Special Case"
description: >
  Collapse duplicated special-case handling scattered across many call
  sites into one special-case object that captures the shared reaction,
  migrating callers to a single comparison function before ever touching
  the underlying representation.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 10 (formerly Introduce Null Object)"
---

A recurring duplication pattern: many call sites check a data structure for
a specific value, and most of them react to it identically. The fix is the
**Special Case pattern**: create one special-case element that captures the
shared reaction, so most special-case checks become simple, uniform calls
instead of repeated conditionals. A special case can be as simple as a
literal object with the expected values pre-filled in (when only reads
happen), or a full object with behavior (when more than plain data access is
needed). Null is the most common value needing this treatment — the
[Null Object pattern](null-object-pattern.md) is one specific instance of
this more general idea, not a separate technique. This is the mechanical
refactoring that implements the broader principle of
[designing special cases out of existence](design-special-cases-out-of-existence.md).

**Mechanics**: starting from a container whose subject property clients
compare against a special-case value, add a check property to the *normal*
case returning `false`; create a special-case object or class with the same
check property returning `true`. Apply
[Extract Function](extract-function.md) to the comparison logic itself, and
migrate every client to call that new function instead of comparing
directly. Introduce the actual special-case object into the code. Update
the extracted comparison function's body to use the new check property
instead of the raw value comparison. Test. Use
[Combine Functions into Class](combine-functions-into-class.md) or
[Combine Functions into Transform](combine-functions-into-transform.md) to
consolidate the shared special-case *behavior* into the new element — often
reducible to a plain literal record, since a special case commonly just
returns fixed values. Finally, apply [Inline Function](inline-function.md)
on the comparison function wherever a caller still genuinely needs an
explicit special-case check.

**Why this ordering matters**: changing the underlying representation (say,
from a sentinel string to a real object) all at once would force every
comparison site to change simultaneously. Abstracting the check first,
migrating every caller to the abstraction, and only then swapping the
underlying representation is the generalizable technique for any "I need to
change something everywhere at once" situation — the same staged-migration
shape used elsewhere for renames and signature changes.

**Special-case objects are value objects**, and should always be immutable
even if the objects they're substituting for are not — a setter on a
special case can legitimately accept calls but silently do nothing. If a
special case needs to expose a related object, that related object is
usually itself a special case, recursively. However many callers share a
common fallback reaction, there's usually at least one that wants genuinely
different special-case behavior — for those, keep the explicit check,
narrowed down to read the object's own check property directly rather than
calling the shared comparison helper. A plain object literal with the
expected fallback values is a lighter-weight substitute for building a full
class whenever nothing ever writes to the special-cased field.
