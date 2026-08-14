---
type: concept
title: "Refactoring: Hide Delegate"
description: >
  Add a forwarding method on a server object so clients call it instead of
  reaching through the server to call one of its own delegate fields
  directly, containing the blast radius of a future delegate-interface
  change to the server alone.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

[Encapsulation](information-hiding.md) is not only about hiding fields — it
also applies to hiding the *relationships between objects*. If client code
reaches through a server object to call a method on the server's own
delegate field (`aPerson.department.manager`), the client now has direct
knowledge of, and a dependency on, the delegate's interface: any interface
change to the delegate propagates all the way out to every client. The fix
is a simple forwarding method directly on the server (`Person.manager`,
delegating to `this._department.manager`), so future delegate-interface
changes only ripple as far as the server, never reaching the clients at all.

**Mechanics**: for each delegate method a client needs, add a matching
simple delegating method on the server. Migrate clients to call the server's
new method instead of reaching through to the delegate directly, testing
after each change. Once no client needs direct delegate access anymore,
remove the server's delegate accessor entirely and test.

Applying this to every link of a long navigation chain is the standard cure
for [Message Chains](message-chains.md), but doing so at *every* link risks
turning the intermediate object into a [Middle Man](pass-through-methods.md)
— the inverse refactoring,
[Remove Middle Man](remove-middle-man.md), is the release valve when Hide
Delegate has been over-applied. The two form a reversible pair: what looked
like good encapsulation six months ago can become awkward today, and moving
the boundary back and forth as the system's shape changes is a normal,
low-cost use of refactoring, not a sign either application was a mistake.
