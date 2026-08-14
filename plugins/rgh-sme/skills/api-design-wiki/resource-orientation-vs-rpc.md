---
type: concept
title: Resource Orientation Versus RPC
description: >
  Modeling remote APIs as standard methods on named resources instead of bespoke
  procedure calls, trading perfect fit for learn-once composability.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 1"
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 7"
---

**RPC-style** web APIs expose arbitrary procedures (`predictWeather`,
`ScheduleFlight`, `ShowAllBookings`) — fine for **stateless** one-shot work but
sprawling as synonyms multiply (`ShowFlights` vs `ListAllFlights`) and stateful
flows (saved favorites, reservations) need ad hoc method names.

**Resource orientation** names the **things** managed (resources) and applies a
small [standard method contract](standard-method-contract.md) to each:
`CreateFlightReservation`, `GetFlightReservation`, `ListFlightReservations`,
`UpdateFlightReservation`, `DeleteFlightReservation` replace a long bespoke RPC
list. Learning one new resource type reuses five known verbs instead of five new
procedures — composable patterns beat one-off complex interfaces.

RPC is not wrong for purely stateless calls; resource orientation wins when
clients manage persistent entities and benefit from uniform CRUD semantics.
Non-standard actions still use [custom methods](custom-method.md). Naming and
field conventions for both styles are covered in [API wire naming](api-wire-naming.md).
