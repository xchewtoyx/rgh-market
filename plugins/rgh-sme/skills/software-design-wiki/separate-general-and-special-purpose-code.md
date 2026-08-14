---
type: concept
title: Separate General-Purpose and Special-Purpose Code
description: >
  A module implementing a general-purpose mechanism should contain only that
  mechanism, with special-purpose code that specializes it for one use kept
  in a different module — but this rule applies per mechanism, not globally.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
---

Extends [general-purpose modules are deeper](general-purpose-modules-are-deeper.md):
a module implementing a general mechanism shouldn't also carry code that
specializes it for one particular use, and shouldn't have unrelated
general-purpose mechanisms bundled into it either. Special-purpose code
belongs in a different module, typically one tied to the specific purpose it
serves — general text operations belong in a text class; UI-specific
operations (deleting a selection) belong in the UI module that owns that
concept.

Architecturally, lower system layers tend toward general-purpose and upper
layers toward special-purpose. The way to enforce the separation is to
actively pull special-purpose code *upward* into higher layers, keeping lower
layers general, rather than letting special-purpose needs leak downward. When
a single class mixes both for the same abstraction, look to split it into a
general-purpose class plus a special-purpose class layered on top — see
[special-general mixture](special-general-mixture.md) for the red flag this
prevents, and its worked fix (extracting a standalone `History` class from an
editor's undo mechanism).

**Important nuance**: this rule applies *per mechanism*, not globally. It's
fine — even correct — for one class to combine special-purpose code for one
mechanism with general-purpose code for a *different* mechanism. A text class
can legitimately hold both general text operations and text-specific undo
logic, because that undo logic is closely tied to text functionality, even
though it must still stay separate from a generic undo-tracking mechanism
used elsewhere.
