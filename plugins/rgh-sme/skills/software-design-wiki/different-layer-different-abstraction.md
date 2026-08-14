---
type: concept
title: Different Layer, Different Abstraction
description: >
  In a well-designed layered system, each layer presents a genuinely
  different abstraction from the layers above and below it; adjacent layers
  with similar or duplicated abstractions signal a class-decomposition
  problem.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

An operation moving up or down through a well-layered system should change
[abstraction](abstraction.md) at every call across a layer boundary: a file
system moves from a byte-range file API, to a fixed-size block cache, to
device drivers; TCP presents a reliable byte stream over a network layer that
only offers best-effort, bounded packets. Each layer is solving a genuinely
different problem than its neighbors.

**Red flag: adjacent layers with similar abstractions.** When two layers end
up looking alike, it means the class decomposition hasn't found the real
boundary between responsibilities. This shows up in a handful of recognizable
patterns: [pass-through methods](pass-through-methods.md),
[decorators overused](decorator-pattern-and-shallow-classes.md), interface and
implementation mirroring each other (see
[interface vs. implementation abstraction gap](interface-vs-implementation-abstraction-gap.md)),
and [pass-through variables](pass-through-variables.md). All of them are cases
where added structure fails to earn its
[complexity cost](design-cost-benefit-of-infrastructure.md).
