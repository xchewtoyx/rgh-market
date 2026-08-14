---
type: concept
title: Every Piece of Design Infrastructure Must Pay for Itself
description: >
  Every interface, argument, function, class, or definition imposes a
  complexity cost because developers must learn about it, so it is only
  worthwhile if it eliminates more complexity than it adds.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

This is the general principle behind
[different layer, different abstraction](different-layer-different-abstraction.md)
and its specific failure cases —
[pass-through methods](pass-through-methods.md),
[overused decorators](decorator-pattern-and-shallow-classes.md), and
[pass-through variables](pass-through-variables.md) are all instances of
added structure that failed to pay for itself in reduced complexity. A class
earns its keep by encapsulating functionality its users no longer have to
think about; if it doesn't remove more thinking than it demands, it's a net
cost dressed up as design. Any time you're deciding whether to introduce a new
abstraction, module, or parameter, this is the question to ask directly:
does this eliminate more complexity than it introduces? For a quantified
version of this question applied specifically to building a reusable
mechanism for a class of anticipated future change, see [the cost-benefit
inequality for building a change
mechanism](cost-benefit-of-a-change-mechanism.md).
