---
type: concept
title: Referential Transparency and Pure Functions
description: >
  A method is referentially transparent when its call can be replaced by its
  return value without changing program behavior — the test for whether hidden
  inputs or outputs disqualify it from output-based testing.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 6"
---

Functional programming treats **mathematical (pure) functions**: no hidden
inputs or outputs — everything relevant appears in the signature; same input
always yields same output.

Hidden inputs/outputs that disqualify purity:

- **Side effects** — mutations, I/O not reflected in the return type.
- **Exceptions** — control-flow outputs bypassing the signature contract.
- **External or internal state references** — `DateTime.Now`, DB queries,
  private mutable fields.

**Referential transparency test**: can a call be replaced by its return value
without changing behavior? `Increment(int x) => x + 1` passes; a stateful
`Increment()` mutating a field fails because the mutation isn't captured in
the return value.

Immutable constructor dependencies (e.g. `_maxEntriesPerFile`) aren't hidden
inputs if immutable between construction and use — they're **values**, not
[collaborators](classical-vs-london-unit-testing-schools.md).

See [output-based testing](output-based-testing.md) and [functional architecture
for testability](functional-architecture-for-testability.md).

Michael Feathers: "Object-oriented programming makes code understandable by
encapsulating moving parts. Functional programming makes code understandable
by minimizing moving parts."
