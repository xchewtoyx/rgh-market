---
type: concept
title: Abstraction (Software Design)
description: >
  An abstraction is a simplified view of an entity that omits unimportant
  details so it can be thought about and manipulated more easily; a module's
  interface is its abstraction.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

Abstraction is a pervasive human strategy for managing complexity, not just a
programming technique — a microwave's control panel and a car's dashboard are
both simple abstractions over genuinely complex internals (RF generation,
engine and brake systems). In modular programming, a
[module's interface](module-interface-and-implementation.md) *is* its
abstraction over the implementation.

Abstractions fail in two opposite directions:

1. **Including unimportant details** needlessly complicates the abstraction
   and raises [cognitive load](cognitive-load.md) for no benefit — the detail
   didn't need to be surfaced.
2. **Omitting important details** produces a **false abstraction**: it looks
   simple, but callers actually need the hidden detail to use it correctly.
   This is [obscurity](obscurity.md) wearing a simple interface as a disguise.

The design skill is figuring out which details are genuinely important and
keeping that set as small as possible. A file system, for instance, correctly
hides block-allocation mechanics from most callers (unimportant to them), but
must expose flush and write-through timing semantics, because applications
like databases genuinely need to know exactly when data becomes durable on
storage — omitting that would make the abstraction false, not simple.

A false abstraction can look completely reasonable on its own. A text-editing
class's `backspace(cursor)` method looks like it hides "which characters get
deleted," but UI developers actually needed that detail to reason about their
own code, and would end up reading `backspace`'s implementation to confirm it
anyway — the abstraction hid something that mattered, creating
[obscurity](obscurity.md) instead of removing complexity. (The general fix in
that case was to replace the UI-shaped method with
[general-purpose primitives](general-purpose-modules-are-deeper.md) that make
the deleted range explicit at the call site.) The underlying principle:
determining *who needs to know what, and when* is one of the most important
elements of software design. When a detail is genuinely important to a
caller, make it explicit and obvious rather than hiding it behind an
interface that only pretends to remove it.
