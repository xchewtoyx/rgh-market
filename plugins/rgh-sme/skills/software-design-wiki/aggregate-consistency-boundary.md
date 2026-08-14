---
type: concept
title: "Aggregate: Enforcing Invariants Through a Single Root"
description: >
  An aggregate is a graph of related objects whose parent (the aggregate
  root) is the only entry point for changing any of them, so every
  state-changing operation can enforce the aggregate's business rules
  inline and the aggregate can never be observed in an invalid state.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 4"
---

An aggregate groups one or more entities (and optionally value objects)
that must change together consistently — one aggregate instance reflects
the state of one coherent part of the domain model. Its parent entity, the
**aggregate root**, composes the rest of the graph and defines the
aggregate's entire public interface: nothing outside the aggregate reaches
into its internal objects directly, every interaction goes through the
root.

This gives the aggregate a natural place to keep its
[invariants](invariants.md) true at all times: each state-changing method
on the root validates the transition before applying it — a `close()`
method that only succeeds from an `OPENED` status, a `reschedule()` that
refuses to move a date once the aggregate is `CLOSED` — rather than trusting
every external caller to check those preconditions themselves before
mutating fields directly. Because the root is the *only* entry point,
**the aggregate can never be observed in an invalid state** by anything
holding a reference to it — the invariant isn't just usually true, it's
structurally guaranteed by the fact that no other path to mutation exists.
This is the same underlying mechanism as
[anemic domain model](anemic-domain-model.md)'s fix: behavior that
validates and enforces a rule belongs on the object whose state the rule
governs, not in a separate layer that manipulates the object from outside.

An aggregate is also naturally a **transactional/consistency boundary**:
because everything that must stay consistent together lives inside one
aggregate, persisting or loading the whole aggregate atomically is
sufficient to keep its invariants intact across a save — no cross-aggregate
transaction is needed for rules that are entirely internal to one
aggregate. State transitions on the root commonly also emit a **domain
event** (`CfpOpened`, `CfpClosed`) recording that the change happened,
giving other parts of the system — inside or outside the same module — a
way to react without reaching back into the aggregate's internals.
