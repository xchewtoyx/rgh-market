---
type: concept
title: "Ports and Adapters (Hexagonal) Architecture"
description: >
  Isolate business logic from its external environment behind ports
  (interfaces the business logic owns) and adapters (implementations that
  connect those interfaces to a specific technology), so swapping a
  technology touches only its adapter.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 4 (pattern originated by Alistair Cockburn)"
---

Ports and Adapters splits a module into an **inside** (business logic) and
an **outside** (everything the business logic talks to or is talked to by
— a web UI, a database, a message broker). The inside defines **ports**:
interfaces stating exactly what the business logic needs from, or offers
to, the outside world. The outside supplies **adapters**: concrete
implementations that connect a specific actor to a specific port. This is
[dependency inversion](dependency-inversion-principle.md) applied at
architectural scale — the interface is owned by, and lives inside, the
business logic; the technology-specific implementation depends on the
interface, never the other way around.

Two directions of port, matching the two directions of interaction:

- **Driving (primary) ports and adapters** — the outside initiates, the
  inside responds. A REST endpoint is a driving adapter calling into an
  application-service interface (the driving port).
- **Driven (secondary) ports and adapters** — the inside initiates, the
  outside responds. A **repository** interface — persisting and retrieving
  entities or aggregates — is the canonical driven port; a concrete
  database-backed implementation is the driven adapter. The
  domain-model-to-storage-format translation lives entirely in the adapter
  (or a dedicated translator alongside it), specifically so the inner
  domain model stays decoupled from persistence-technology concerns and the
  two can evolve independently.

**Payoff**: swapping an outside component — a different database, a new
message broker, a CLI in place of a REST endpoint — only requires writing
or adjusting its adapter; the inner business logic is untouched. Because
the inside depends only on interfaces it owns, it can also be
[tested in isolation](fake-objects.md) against a fake or in-memory adapter,
without needing the real database or broker running.

**Trade-off**: every port needs an interface, and every actor needs an
adapter, which is real added structure. This is well suited to a complex,
evolving, uncertain piece of business logic that will need its outside
swapped or tested independently — and likely overkill for a simple module
or short-lived prototype where the added indirection has no one to pay for
it. The pattern applies within a single cohesive module (a bounded context,
in DDD terms); it says nothing about how the inside itself should be
structured, though for logic complex enough to justify the pattern in the
first place, the inside is commonly organized as domain objects each
[enforcing its own invariants](anemic-domain-model.md) rather than as
passive data manipulated from outside.
