---
type: concept
title: "Refactoring: Remove Middle Man"
description: >
  Strip out a server's accumulated pile of thin forwarding methods and let
  clients call its delegate directly again, once so many exist that the
  server has become a pure Middle Man.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

The inverse of [Hide Delegate](hide-delegate.md), and the direct cure for
over-applying it: every time a client wants a *new* piece of delegate
functionality, another thin forwarding method has to be bolted onto the
server. After enough of these accumulate, the server becomes pure
[Middle Man](pass-through-methods.md), and it's time to let clients call the
delegate directly again. This smell often shows up from over-enthusiastic
application of the Law of Demeter — treat that law as an occasionally useful
suggestion, not an absolute rule.

There is no fixed "right" amount of hiding to aim for in the abstract, and
that's fine in practice: Hide Delegate and Remove Middle Man form a
reversible pair, so the boundary can be shifted freely later as the system's
shape changes, without treating either direction as a mistake to apologize
for.

**Mechanics**: add a getter exposing the delegate itself. For each client
call currently going through a forwarding method, replace it with a call
chained through the new delegate accessor instead, testing after each
replacement. Once every call to a given forwarding method has been replaced,
delete that now-unused forwarding method. An automated-tooling shortcut:
apply [Encapsulate Variable](encapsulate-variable.md) to the delegate field (routing the forwarding
method itself through the new public getter rather than the private field
directly), then [Inline Function](inline-function.md) on the forwarding
method to replace every caller in one shot.

A mixture is fine in practice — some delegations are common or convenient
enough to be worth keeping even while others get removed; particular
circumstances suggest which approach to take at each call site, and
reasonable people can differ on what works best.
