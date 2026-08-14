---
type: concept
title: Limits of Pulling Complexity Down
description: >
  Absorbing complexity into a module is only a net win when the complexity
  is related to the module's own purpose, meaningfully simplifies things
  elsewhere, and simplifies rather than complicates the module's own
  interface.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 8"
---

[Pulling complexity down](pull-complexity-downwards.md) is not
unconditionally good — the reductio ad absurdum would be pulling an entire
application's functionality into one class. Three conditions distinguish a
genuine win from that extreme:

1. The complexity being absorbed is closely related to the module's existing
   functionality.
2. Absorbing it produces meaningful simplification elsewhere in the
   application.
3. Absorbing it actually simplifies — not complicates — the module's own
   interface.

The overriding goal is minimizing *overall system* complexity, not just
relocating complexity from one place to another. The counter-example from
[general-purpose modules](general-purpose-modules-are-deeper.md) fails all
three conditions: adding UI-specific methods like a backspace handler to the
text class does technically "pull complexity down" into the text class, but
it doesn't meaningfully simplify higher-level code, and UI knowledge isn't
related to the text class's core purpose. The net effect there was
[information leakage](information-leakage.md), not simplification.
