---
type: concept
title: "Code Smell: Message Chains"
description: >
  A client chaining several navigation calls to reach the object it actually
  needs couples that client to every intermediate relationship along the
  way, so any of them changing ripples out to the client.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Message Chains are a client chaining `a.getB().getC().getD()...`, or an
equivalent chain of temporary variables, to reach the object it actually
needs. This couples the client to the intermediate navigation structure, so
any change to one of those relationships ripples out to every client that
chained through it.

Cure: [Hide Delegate](hide-delegate.md) at one or more points in the chain
— but applying this at every link risks turning every intermediate object
into a [Middle Man](pass-through-methods.md), so it's often better to look
at what the
final result of the chain is actually used for and push that usage down the
chain via [Extract Function](extract-function.md) plus
[Move Function](move-function.md), rather than hiding every
step. If multiple clients want to navigate the same tail of the chain, add a
single method that performs the full traversal once. No method chain is
automatically unacceptable — the smell is specifically about a client's
dependence on intermediate structure it shouldn't need to know about.
