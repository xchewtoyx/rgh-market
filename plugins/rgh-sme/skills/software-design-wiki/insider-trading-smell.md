---
type: concept
title: "Code Smell: Insider Trading"
description: >
  Modules that trade too much data or knowledge between each other —
  "whisper to each other by the coffee machine" — raise coupling; inheritance
  is a natural breeding ground for it.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Insider Trading is modules trading too much data or knowledge between each
other — "modules that whisper to each other by the coffee machine." It is a
concrete symptom of [information leakage](information-leakage.md) between
modules that should each be hiding their own decisions. Cure: Move Function
or Move Field to separate over-chatty modules; if the modules genuinely
share a concern, introduce a third module to hold that shared knowledge
properly instead of letting either module reach into the other, or use Hide
Delegate to interpose an intermediary.

Inheritance is called out as a natural breeding ground for this smell —
subclasses inherently know more about their parent than the parent would
like exposed to arbitrary code. The fix there is Replace Subclass with
Delegate or Replace Superclass with Delegate, converting an inheritance
relationship (which grants automatic access) into an explicit delegation
relationship (which doesn't).
