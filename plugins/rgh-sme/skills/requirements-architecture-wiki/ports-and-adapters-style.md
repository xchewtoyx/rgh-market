---
type: concept
title: Ports-and-Adapters (Hexagonal) Style
description: >
  Ports-and-adapters isolates a bounded context's business logic from its
  environment behind explicit interfaces, so the documentation of "what the
  system does" and "what it happens to be connected to" stay separable.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies (Susanne Kaiser), ch. 4"
---

Ports-and-adapters (Alistair Cockburn's "hexagonal architecture") is a
[component-and-connector style](component-and-connector-view.md) that
splits a system into an **inside** (business logic) and an **outside**
(environment), connected only through explicit interfaces:

- A **port** is an interface defining a boundary of the inside — what the
  business logic needs from, or offers to, the outside world, stated in
  the inside's own vocabulary.
- An **adapter** connects an actual outside actor (a REST endpoint, a
  database, a message broker, a UI) to a port, translating between the
  outside's technology-specific representation and the inside's model.
- **Driving (primary) ports/adapters** carry interaction inward — an
  external actor invoking the business logic (e.g. an HTTP request hitting
  a controller that calls through a port).
- **Driven (secondary) ports/adapters** carry interaction outward — the
  business logic invoking something in the environment (e.g. persistence,
  calling out to another system).

The documentation payoff is symmetry: because every crossing of the
inside/outside boundary goes through a named port, swapping what's on the
outside (a different database, a different message broker, a different
UI framework) only requires replacing the adapter behind that port — the
business logic, and its documentation, is unaffected. This is the same
discipline a [context map](context-map.md)'s Anticorruption Layer or
Open-Host Service applies at the boundary *between* bounded contexts,
applied instead at the boundary between one bounded context and its own
technical environment; a bounded context's [context-map](context-map.md)
translation mechanisms toward other contexts typically live in the outer,
adapter part of this same structure, for the identical reason — keeping
the inside insulated from integration-protocol churn.

The style adds real interface and translation overhead, so it earns its
keep specifically where the inside is complex and expected to keep
changing independently of its environment — a [core-domain](subdomain-classification.md)
bounded context is the typical case — and is often not worth it for a
simple, stable, CRUD-shaped one.
