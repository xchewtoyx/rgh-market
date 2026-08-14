---
type: concept
title: General-Purpose Modules Are Deeper
description: >
  A module's functionality should reflect current needs, but its interface
  should be "somewhat general-purpose" rather than tied to them — general
  interfaces end up simpler and deeper even when the module is never reused
  for anything else.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 6"
---

Two naive extremes: build a module fully general-purpose up front (may include
facilities never actually needed), or build it purely special-purpose for
today's specific need (refactor toward generality later if reuse demands it).
The recommended sweet spot is **somewhat general-purpose**: general enough for
multiple plausible uses, but still easy to use for today's actual need.
"Somewhat" matters — over-generalizing to the point that the current use case
becomes awkward is its own failure, checked by
[the generality questions](generality-questions-checklist.md).

The surprising part of the claim: this isn't a bet on future reuse. A
general-purpose interface is simpler and [deeper](deep-modules.md) than a
special-purpose one *even if the module is never reused for anything else*.

Worked example: a text-editor class built with UI-shaped methods —
`backspace(cursor)`, `delete(cursor)`, `deleteSelection(selection)` — feels
natural (mirror the UI 1:1) but accumulates shallow, single-call-site methods
and lets UI-specific concepts (`Selection`, "the backspace key") leak into the
text class, entangling the two classes' evolution: every new UI feature risks
needing a new text-class method. Replacing it with primitives ignorant of the
UI —

```java
void insert(Position position, String newText);
void delete(Position start, Position end);
Position changePosition(Position position, int numChars);
```

— lets UI operations compose from a handful of general primitives (backspace
becomes `delete(changePosition(cursor, -1), cursor)`). Call sites get slightly
longer but more *obvious*: a reader sees exactly which characters get deleted
at the call site instead of having to go read `backspace`'s implementation.
It also nets out to less total code system-wide, since many special-purpose
methods collapse into a few general ones — and, unprompted, the general API
turns out to support things it was never designed for, like a find-and-replace
utility that reuses it almost as-is with one added primitive.

Generality is also what produces good
[information hiding](information-hiding.md) here: the general API cleanly
separates text storage from UI concerns, so the text class no longer needs to
know how backspace is handled — that logic moves entirely into the UI class,
and new UI features need no new text-class methods at all.
