---
type: concept
title: Eliminating vs. Encapsulating Complexity
description: >
  The two general strategies for fighting software complexity are removing
  it outright and hiding it behind a module boundary so most people never
  have to see it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 1"
---

Given [complexity](complexity.md) in a system, there are two general ways to
fight it:

1. **Eliminate complexity** — make the code itself simpler and more obvious:
   remove special cases, use identifiers and idioms consistently, avoid
   dependencies that don't need to exist. This reduces the total complexity
   in the system.
2. **Encapsulate complexity** — accept that some complexity is inherent to
   the problem, and confine it behind a module boundary so that a programmer
   working on one part of the system doesn't need to understand the details
   of another. This is the basis of modular design; see
   [information hiding](information-hiding.md) and
   [deep modules](deep-modules.md).

Encapsulation doesn't reduce the total complexity of a system — it redistributes
where that complexity is visible, so that most developers, most of the time,
only have to confront a small fraction of it. Good design combines both: strip
out complexity that serves no purpose, and wall off what remains so it stays
someone else's problem.
