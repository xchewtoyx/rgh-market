---
type: concept
title: Deep Modules
description: >
  A deep module provides powerful functionality behind a simple interface,
  maximizing the ratio of hidden complexity to complexity imposed on callers
  — the central goal of good module design.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

Picture a module as a rectangle: its area represents the functionality it
provides, and the width of its top edge represents its interface's
complexity. A deep module is a wide, tall rectangle with a short top edge —
most of its bulk is hidden below the interface. Framing it as cost/benefit:
functionality is the benefit, [interface](module-interface-and-implementation.md)
is the cost (complexity imposed on the rest of the system), and the best
modules maximize benefit while minimizing cost. More, or larger, interfaces
are not necessarily better.

**Unix file I/O is the canonical example**: five system calls — `open`,
`read`, `write`, `lseek`, `close` — with simple signatures, behind which the
implementation (hundreds of thousands of lines) handles on-disk file
representation, hierarchical path resolution, permission enforcement,
interrupt-handler coordination, concurrent-access scheduling, in-memory
caching, and heterogeneous storage devices. Those five calls have stayed
essentially unchanged across decades of internal reimplementation — direct
evidence that the interface successfully decoupled callers from
implementation churn.

**Garbage collectors** are an extreme case: no interface at all (invisible
background operation), and adding one actually *shrinks* the caller-visible
interface of the whole system by eliminating manual free/delete calls, despite
the collector's own implementation being highly complex.

Deep modules are the opposite of [shallow modules](shallow-modules.md), whose
interface complexity is disproportionate to the functionality behind it.
