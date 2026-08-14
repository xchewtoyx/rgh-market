---
type: concept
title: Pattern Language Navigation
description: >
  Three axes — architectural scope, theme category, and project phase — for
  finding API patterns without reading the catalog linearly.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4"
---

The pattern catalog is large; navigation beats front-to-back reading. Enter by
any of three organizers, then follow inline related concepts in individual pattern
notes.

## Scope (structural)

From the [remote API domain model](remote-api-domain-model.md):

- **Whole API** — [API description](api-description.md), [API visibility](api-visibility.md),
  lifecycle patterns ([two in production](two-in-production.md)).
- **Endpoint** — [processing resource](processing-resource.md),
  [information holder resource](information-holder-resource.md) specializations.
- **Operation** — [operation responsibility patterns](operation-responsibility-patterns.md).
- **Message** — representation structure ([atomic parameter](atomic-parameter.md),
  [embedded entity vs linked information holder](embedded-entity-vs-linked-information-holder.md)),
  quality mechanisms ([pagination](pagination.md), [error report shape](error-report-shape.md)).

## Theme (topical)

Five categories mirror ADDR chapters: **foundation** (integration style, visibility,
documentation), **responsibility** (endpoint roles, operation types), **structure**
(message shapes and element stereotypes), **quality** ([API quality governance](api-quality-governance.md),
pagination, wish lists), **evolution** (versioning, deprecation). Some quality
patterns appear in message-structure chapters because they are special-purpose
representations ([API key as message element](api-key-as-message-element.md),
[context representation](context-representation.md)).

## Phase (time)

Rough lifecycle mapping — not waterfall; revisit within sprints:

- **Inception / Align** — visibility, integration style, initial description.
- **Elaboration / Define** — endpoint roles, auth surface, error and context shapes.
- **Construction / Design** — message structure, retrieval/computation/create/transition
  operations, client-driven efficiency patterns.
- **Transition / Refine** — SLAs, pricing, rate limits, versioning policy at go-live
  and beyond.

Patterns are platform-independent **guides**, not mandates — adapt forces to project
context. Production case studies (for example community APIs with [two in production](two-in-production.md)
plus [semantic versioning API](semantic-versioning-api.md)) show combinations in
the wild without replacing pattern-level reasoning.
