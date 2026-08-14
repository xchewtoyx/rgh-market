---
type: concept
title: API Design from Requirements Artifacts
description: >
  API design should start from user stories, documented quality attributes,
  a context map of bounded contexts, and prior architectural decisions —
  not from endpoint sketches in isolation.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 2"
---

Before specifying endpoints or choosing [API visibility](api-visibility-decision.md)
and [integration types](api-integration-type-decision.md), gather and
link the requirements artifacts that constrain and justify the interface:

- **User stories** with explicit [requirement
  rationale](requirement-rationale.md) — the functional need the API must
  serve (e.g., a customer updating contact information online to avoid
  costly agent channels).
- **Desired system qualities** captured alongside the story — performance
  targets with [fit criteria](fit-criterion.md) (e.g., 80 percent of
  updates complete within two seconds), scale assumptions (expected user
  count and concurrency), usability, availability windows, and
  maintainability/operability expectations. These become [architecturally
  significant requirements](architecturally-significant-requirement.md)
  and [quality attribute scenarios](quality-attribute-scenario.md) that
  the API contract and hosting choices must satisfy.
- **System context** — a [context diagram](context-diagram.md) or
  [context map](context-map.md) showing bounded contexts, which systems
  already expose interfaces, and which new relationships the capability
  adds. Named integration patterns (Customer/Supplier, Open Host Service,
  Conformist, and the rest) signal where new API design and development
  work is required and how tightly coupled the change will be.
- **Architecture overview** — existing components, communication
  mechanisms, and **prior [architectural
  decisions](architectural-decision-capture.md)** (e.g., a company-wide
  backend stack or microservices rationale for independent scaling) that
  new API design must align with or explicitly challenge.

Typical design activities for a sprint then proceed in order: (1) design a
platform-independent API for the upstream provider consumed by the
downstream client; (2) specify endpoints/resources, operations, request
parameters, and response structures; (3) **justify** each choice against
the artifacts above in [architectural decision
records](architectural-decision-capture.md), citing pattern forces where
applicable via [pattern-language documentation
format](pattern-language-documentation-format.md). An architectural spike
that discovers missing backend interfaces is itself an input — it surfaces
gaps between stated requirements and what existing systems can currently
expose, which the API design must close.

The analysis-level domain model (aggregates, identifiers, value objects)
informs message structure and endpoint responsibilities but does not
replace the requirements trace: every operation in the contract should
trace back to a story, quality, or context relationship it exists to
satisfy via [requirements traceability](requirements-traceability.md).
