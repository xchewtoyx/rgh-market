---
type: concept
title: Developer Experience as Requirement
description: >
  Developer experience — function, stability, ease of use, and clarity — is
  a documentable quality requirement for APIs, with distinct short-term
  adoption metrics and long-term operational sustainment metrics.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 1"
---

Developer experience (DX) for an API is not informal polish; it is a set
of [non-functional requirements](non-functional-requirement.md) that
belong in the specification alongside functional behavior. A useful
decomposition (Cavalcante) treats DX as four parts:

- **Function** — processing and data-management features meet client goals;
  this is the core reason clients adopt the API.
- **Stability** — agreed runtime qualities (performance, reliability,
  availability) are met in production, not just in demos.
- **Ease of use** — documentation (tutorials, examples, reference),
  community knowledge channels, and tooling lower the cost of integration.
- **Clarity** — simplicity plus observability: consequences of actions are
  predictable, and failures distinguish invalid input from provider-side
  problems and suggest remedies (retry versus correct input).

Machine-to-machine communication differs from human-computer interaction,
so not all user-experience guidance transfers directly; DX also extends to
provider-side maintainers and (often underdocumented) operators who manage
the API at runtime.

API success has two measurable horizons worth capturing as [fit
criteria](fit-criterion.md):

- **Short term** — time to first successful call from documentation alone
  (lower is better); time to first level-n support ticket (longer is better,
  indicating fewer integration-breaking defects). These drive adoption.
- **Long term** — sustained performance, reliability, and manageability
  under real load; API lifetime and ability to adapt as client needs change
  without breaking dependents.

Commercial success is relative and business-dependent — from billions of
daily requests with minimal latency to a first external client succeeding
using only published [interface
documentation](interface-documentation.md). Document which success definition
applies, because it determines which DX and operational ASRs take priority
in [documenting trade-offs](documenting-trade-offs.md).
