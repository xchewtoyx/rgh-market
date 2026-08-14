---
type: concept
title: Integration Distance
description: >
  Five distinct kinds of mismatch — syntactic, data-semantic, behavioral-
  semantic, temporal, and resource — that can exist between two
  integrating elements even when their published API types line up.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 7"
---

Two elements that integrate without incident on day one can still be
tightly, expensively coupled in ways a compiler and a code review will
never catch, because most of that coupling doesn't live in the
programming-language interface at all. Five kinds of "distance" between
integrating elements name where the mismatch can hide:

- **Syntactic distance** — mismatched data element count or type (an
  `int` where a `float` is expected, or disagreement over how a bit field
  is packed). The easiest to catch: a compiler flags type mismatches, and
  the subtler cases at least show up on code inspection.
- **Data semantic distance** — the same data type, but a different
  meaning (altitude in meters on one side, feet on the other). Nothing in
  the type system reveals this; only interface documentation or metadata
  does.
- **Behavioral semantic distance** — disagreement about states or modes
  (a field interpreted differently during startup than during normal
  operation) or about who is expected to initiate an interaction.
- **Temporal distance** — mismatched rate or timing assumptions: one side
  emits at 10Hz, the other expects 60Hz, or the two sides assume different
  latencies between related events.
- **Resource distance** — mismatched assumptions about a shared resource:
  one side assumes exclusive device access when it's actually shared, or
  combined bandwidth demand from several producers exceeds what the
  channel can carry.

None of these five typically appear in a function signature or an API
schema, which is exactly why [interface documentation](interface-documentation.md)
has to go beyond syntax to be useful: it exists specifically to make these
distances visible before integration, not to be discovered as an
incident afterward. A service boundary that decouples cleanly on the
syntactic dimension (a well-designed published interface) can still be
tightly coupled on the semantic, temporal, or resource dimensions — "the
service is decoupled because it has an interface" is not a safe inference
without checking the other four.

Integration difficulty is roughly a function of two things: how many
dependencies exist between the elements (**size**), and how much distance
has to be bridged at each one. Reducing either — fewer dependencies, or
smaller distance per dependency, achieved through an explicit interface,
an intermediary, or adherence to a shared standard — is what makes future
integration cheaper. This is the same forward-looking concern as
[modifiability](change-locality-classification.md): both are about
planning for an incompletely known future, one from the perspective of
changing your own system, the other from the perspective of connecting it
to something else.
