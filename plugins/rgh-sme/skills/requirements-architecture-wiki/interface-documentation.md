---
type: concept
title: Interface Documentation
description: >
  An interface is the boundary across which elements interact; fully
  documenting one means specifying resources, syntax, semantics,
  protocol, state, error behavior, and quality constraints — not just a
  signature.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 7"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (ed. Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 7"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 7"
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 15"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

An interface is the boundary across which one element interacts with
another. An API or a function signature is a narrower, syntactic concept —
interface documentation exists to serve implementers, users, integrators,
testers, maintainers, and analysts, who each need more than a signature to
do their job safely.

Full interface documentation specifies: the resources provided and
required (not just their name and type, but what they actually do);
syntax; semantics; sequencing and protocol (what order calls must happen
in); state and its transitions; preconditions, postconditions, and
invariants; errors and exceptions; timing and concurrency behavior; side
effects; and quality constraints. Where an audience or purpose genuinely
differs, use separate interfaces rather than overloading one — and never
let a single example diagram stand in for the actual behavioral contract;
examples illustrate, they don't specify. See [integration
distance](integration-distance.md) for the specific kinds of mismatch —
beyond simple type mismatches — this documentation has to rule out, and
[interface evolution](interface-evolution.md) for how to change a
published interface without breaking everyone already depending on it.

This is also an architectural choice with a documentation consequence:
requiring interaction through explicit, structured interfaces — never
through shared internal data structures or schemas — is what "loose
coupling" concretely means (a **bounded context**, to use Domain-Driven
Design's term), and it is why structured interface types (e.g. Protocol
Buffers or Thrift schemas) tend to produce better-documented, more
reasoned-about systems than an ad hoc key/value API: the structure forces
the design decisions that free-form documentation might otherwise skip.
See [connector semantics](connector-semantics.md) for the corresponding
concept at the level of a whole interaction mechanism rather than a single
interface.

For remote APIs specifically, an **API description** (a variant of the
interface-description pattern) documents the contract clients and providers
share: request and response message structures, error reporting, dynamic
behavior (invocation sequences, pre-/postconditions, invariants), and often
quality-management policies and organizational context beyond pure syntax.
Machine-readable contract languages — OpenAPI (formerly Swagger), API
Blueprint, WSDL, domain-specific languages such as MDSL — support
interoperability and information hiding: providers need not expose
implementation detail clients do not need, and clients need not guess
invocation rules. That independence from implementation detail is what
enables loose coupling and [interface evolution](interface-evolution.md),
but it creates an ongoing maintenance obligation: the description must
stay current as the API changes, which is a deliberate cost to accept in
the [architectural decision record](architectural-decision-capture.md)
when choosing elaborate contract documentation over none. Small or
prototype projects likely to change significantly may consciously defer
formal API description until the interface stabilizes.
