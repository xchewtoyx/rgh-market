---
type: concept
title: "Refactoring: Remove Setting Method"
description: >
  Delete a setter for a field that shouldn't change after construction and
  fold its value into the constructor instead, so the field's immutability
  is documented structurally rather than left as an implicit expectation.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11"
---

The presence of a setter is itself a signal — it tells readers this field
is expected to change after construction. If a field genuinely shouldn't
change post-construction, remove its setter entirely (and make the field
immutable if the language allows), so the field is only ever set inside the
constructor. This both documents the intent clearly and, ideally,
structurally removes the possibility of later mutation — one of the
mitigations for the [mutable data](mutable-data-smell.md) smell, and a
prerequisite for treating an object as a
[value object](change-reference-value.md).

**Two recurring situations create removable setters**: a habit of always
going through accessor methods, even from within the constructor itself,
which leaves a setter whose *only* caller is the constructor — a strong
signal it should just be inlined away entirely; and objects built via a
**creation script** — a constructor call followed by a sequence of setter
calls used only to finish initializing a freshly-created object, with no
expectation those setters are ever called again afterward. In both cases,
removing the setters makes the "this only happens once, at creation" intent
explicit rather than implicit.

**Mechanics**: if the value isn't already accepted by the constructor, use
[Change Function Declaration](change-function-declaration.md) to add it as
a constructor parameter, and have the constructor call the setter
internally with it (when removing several setters at once, add all their
values to the constructor together first — this simplifies the remaining
steps). Then, at each place outside the constructor that currently calls
the setter, replace that call by passing the value through the constructor
instead — "create-then-set" becomes "create-with-the-value" — testing after
each site. **If this can't be done because you're mutating a genuinely
shared reference object rather than initializing a fresh one, abandon the
refactoring**, since the setter is serving a real ongoing purpose in that
case. Once no external caller of the setter remains, apply
[Inline Function](inline-function.md) to fold it directly into the
constructor, and make the underlying field immutable if the language
supports it. Test.
