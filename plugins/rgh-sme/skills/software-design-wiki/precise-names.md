---
type: concept
title: Precise Names
description: >
  The most common naming failure is a name too generic or vague to convey
  real information; a name that's hard to make precise is itself a design
  smell pointing at a poorly-factored variable or method.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 14"
---

**Red flag: vague name** — "If a variable or method name is broad enough to
refer to many different things, then it doesn't convey much information to
the developer and the underlying entity is more likely to be misused."

Worked examples, each with a fix:

- `getCount()` on an `IndexletManager` — count of *what*? →
  `getActiveIndexlets` or `numIndexlets` lets a reader guess the behavior
  without consulting documentation.
- `x`/`y` used for a character's position within a line of text — could just
  as easily mean on-screen pixel coordinates → `charIndex`/`lineIndex` names
  the actual abstraction.
- `blinkStatus` (boolean, true = cursor visible) — "status" conveys nothing
  for a boolean, and "blink" doesn't say what's blinking → `cursorVisible`,
  with a separate comment explaining the blink behavior. General rule:
  **boolean variable names should always be predicates** (read as true/false
  claims).
- `VOTED_FOR_SENTINEL_VALUE = "null"` — signals "this is special" without
  saying what the special meaning *is* → `NOT_YET_VOTED` states the meaning
  directly.
- A variable named `result` inside a method with **no return value** —
  actively misleading (implies it becomes the return value) and uninformative
  about its actual content → should describe what it actually holds (e.g.
  `mergedLine`, `totalChars`). `result` is fine, if still a bit generic, in a
  method that *does* return a value, since the reader can consult the method
  doc and correctly infers it will end up as the return value.

Short, generic names (`i`, `j`) remain fine for loop variables when the
entire usage span is visible within a few lines — the meaning is self-evident
from the visible context, so a longer name buys nothing. Once a loop is too
long to see at a glance, or the iteration variable's role is genuinely
unclear, switch to a descriptive name; see
[name length versus distance from use](name-length-vs-distance.md).

The opposite failure is a name that's **too specific**: a `delete(Range
selection)` method whose parameter is named `selection` implies deletion
always applies to a UI-selected range, when the method is actually
[general-purpose](general-purpose-modules-are-deeper.md) and can delete any
range. The fix is to rename the parameter to the more generic `range`.

**Red flag: hard to pick name** — "If it's hard to find a simple name for a
variable or method that creates a clear image of the underlying object,
that's a hint that the underlying object may not have a clean design."
Difficulty finding a precise, intuitive, reasonably short name is itself a
diagnostic: the fix is often not a better name but a better factoring — e.g.
splitting an overloaded variable into two separate ones, each of which then
gets an easy, precise name. Naming is a diagnostic tool for finding design
weaknesses, not just a cosmetic exercise.
