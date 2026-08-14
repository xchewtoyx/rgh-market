---
type: concept
title: Implementation Comments
description: >
  Implementation comments should convey what the code is doing and why, not
  a line-by-line how, and most short methods need none at all.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Most methods are short and simple enough to need zero implementation
comments — the code plus the [interface comment](interface-documentation.md)
already make things clear. When implementation comments are needed, their
goal is to convey *what* the code is doing, not a line-by-line *how* — once a
reader knows the intent, the mechanics usually follow easily.

For longer methods with multiple functionally distinct blocks, precede each
block with a short abstract label (`// Phase 1: Scan active RPCs to see if
any have completed.`). For loops, a preceding comment describing what happens
in a generic iteration is useful when the loop isn't trivially obvious;
short, simple loops don't need this.

Implementation comments are also the right place to capture **why**,
especially for non-obvious tricky code — documenting the reasoning behind a
bug-fix-motivated addition, for instance. For fixes tied to a tracked bug
report, point to the bug ID rather than restating its details inline
("Fixes RAM-436, related to device driver crashes in Linux 2.4.x") — the same
avoid-duplication discipline that applies to
[cross-module design decisions](cross-module-design-decisions.md).

For local variables, only the most important ones in longer methods
typically need comments; if every use of a variable is visible within a few
nearby lines, the code itself usually suffices. Variables used across a wide
span of code are the ones worth documenting explicitly, and — as with
[precision-adding comments](precision-adding-comments.md) — document what the
variable *represents*, not the mechanics of how the code manipulates it.
