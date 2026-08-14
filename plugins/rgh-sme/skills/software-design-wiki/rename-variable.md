---
type: concept
title: Rename Variable
description: >
  Naming effort should scale with a variable's scope and lifetime — a
  one-line lambda variable can be a single letter, but a field that persists
  beyond a single call deserves real naming care.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6"
---

Good naming is central to clear code, but getting a name right on the first
try is rare — understanding deepens, or requirements shift, over a
variable's life. Naming effort should scale with a variable's scope and
lifetime: a one-line lambda variable can be a single letter since context
makes its purpose obvious, short-function parameters can stay terse, but
fields that persist beyond a single function call deserve the most naming
care and attention.

**Mechanics**: if the variable has wide usage, first apply [Encapsulate
Variable](encapsulate-variable.md) — this reduces the rename to changing
just the accessor bodies instead of every call site. Otherwise, find and
change every reference directly. **If any reference lives in a different,
externally-owned codebase, the variable is effectively a published variable
and this refactoring cannot be done** — the same published-interface
boundary constraint that applies to [Change Function
Declaration](change-function-declaration.md). If the variable never changes
— it acts as a constant — you can instead declare the new name, alias the
old name to it, migrate references gradually while testing after each, and
delete the old declaration once done, without needing full encapsulation
first.
