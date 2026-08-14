---
type: concept
title: Requirements Reuse Patterns
description: >
  Reusable requirements artifacts — event-response patterns, domain
  models, and organizational reuse libraries — accelerate discovery and
  prevent missing well-known, recurring requirements.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 15"
---

Requirements discovery doesn't have to start from nothing every time.
Three kinds of reusable artifact accelerate it and improve consistency:

- **Requirements patterns** — a standardized response to a recurring
  business event across domains (e.g. a customer-registration pattern or
  an order-processing pattern), packaging the event trigger, the
  contextual data model, standard processing rules, and default
  [non-functional requirements](non-functional-requirement.md) together.
- **Domain analysis / domain models** — abstract models of a whole
  industry domain (logistics, financial services, telecommunications),
  containing generalized entity-relationship data dictionaries and
  standard [business use cases](business-event-and-use-case.md) that a
  specific project's requirements can be checked against or derived from.
- **Organizational reuse libraries** — a centralized store of reusable
  security constraints, regulatory compliance rules, style guides, and
  standard [fit criteria](fit-criterion.md), built up across projects
  within one organization.

The main payoff of reuse isn't just speed: it's that patterns and domain
models encode requirements — particularly safety and legal-compliance
requirements — that a fresh discovery effort is prone to missing simply
because nobody thought to ask. Reusing a vetted pattern imports that prior
project's hard-won completeness along with its structure.
