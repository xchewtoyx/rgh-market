---
type: concept
title: Stateless Custom Method
description: >
  Custom methods that process input without persisting application state, often
  anchored to a parent for billing or permissions when pure statelessness is rare.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 9"
---

Some [custom methods](custom-method.md) neither read nor write stored
application state — for example `POST /text:translate` → `TranslateText` when
regulations require on-the-fly processing without retention (GDPR-style
residency). Overlaps with [computation function](computation-function.md)
semantics across the wire.

Pure statelessness is **rare in practice** — billing and authorization usually
need an anchor. Common patterns:

- Attach to a parent used only for billing/permissions:
  `POST /{parent=projects/*}/text:translate`
- Attach to a dedicated configuration resource with full CRUD when future
  variability appears (multiple models, glossaries):
  `POST /{id=translationModels/*}/text:translate`

**Caution:** statefulness often becomes necessary later; retrofitting is hard
once a free-floating stateless method is widely adopted. Example free validator:
`POST /emailAddress:validate` with no parent.

Use stateless custom methods cautiously — prefer a resource anchor when billing,
models, or audit trails may appear.
