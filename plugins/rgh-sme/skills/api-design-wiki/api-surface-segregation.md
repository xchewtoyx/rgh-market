---
type: concept
title: API Surface Segregation
description: >
  Splitting large partner-facing APIs by role and business process so changes
  affect only the clients that use that surface.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 10 (Terravis)"
---

Early integration APIs often grow **large and partner-type-centric** — one bank API
spanning many processes — coupling unrelated clients to shared churn. **Interface
segregation** for public or [community API](api-visibility.md) surfaces means
**smaller APIs partitioned by partner role and business process**: a mortgage-start
API for notaries differs from a query API for banks.

Benefits: easier stakeholder communication, narrower change-impact analysis when
[version identifier](version-identifier.md) or operation sets evolve, and alignment
with [operation responsibility patterns](operation-responsibility-patterns.md)
(naming like `start...` vs `request...` signals creation vs transition).

Trade-off: more endpoints and descriptions to maintain — usually cheaper than
forcing all partners to absorb unrelated process changes. Contrasts with a single
generic command-style facade that stays syntactically stable but pushes complexity
into opaque payloads.
