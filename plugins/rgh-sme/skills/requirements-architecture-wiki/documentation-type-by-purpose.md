---
type: concept
title: Documentation Type by Purpose
description: >
  Each documentation type — reference, design, tutorial, conceptual, landing
  — should serve one purpose and optimize a different balance of completeness,
  accuracy, and clarity.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

Every document should have a **singular purpose** and stick to it — just
as a well-scoped API does one thing well. Monolithic pages mixing links,
conceptual explanation, and API reference fail because they serve no single
audience task and grow long enough that nobody reads them. Progressive
disclosure for agents and humans alike depends on splitting by purpose,
not by source file convenience.

Common types and what each optimizes:

| Type | Primary job | Completeness / accuracy / clarity bias |
| --- | --- | --- |
| **Reference** | Document how to use code or an API correctly | Favor completeness; single-source from code comments where possible |
| **Design** | Record goals, strategy, and [architectural decisions](architectural-decision-capture.md) before build | Favor accuracy of rationale and trade-offs |
| **Tutorial** | Onboard a newcomer through a sequenced path | Favor clarity; explicit prerequisites; numbered user actions only |
| **Conceptual** | Explain cross-cutting behavior reference alone cannot | Favor clarity; may sacrifice edge-case completeness |
| **Landing** | Route readers to the right next document | Favor organization; no content that belongs elsewhere |

Reference documentation is often generated from in-code comments and should
stay single-sourced. Distinguish **API comments** (must not assume the
reader knows the interface as well as the author; must not discuss
implementation decisions) from **implementation comments** (may assume
more domain knowledge but should still state *why* code was written a
certain way, since authors leave projects). A common mistake is adding
design decisions to API reference — put those in a [design
document](design-document.md) instead.

Conceptual documentation augments reference; some duplication for clarity
is acceptable. Complex cross-API behavior needs a standalone conceptual
document when no single API's file comment can scope the explanation —
analogous to integration tests complementing unit tests.

Landing pages degrade when they accumulate "read this first!" essays,
team-internal notes, and customer-facing links on one scroll. Fix by stating
purpose explicitly, linking only, splitting by taxonomy when the list
grows, and separating **team** landing pages from **product/API user**
landing pages — what engineers need differs from what integrators need.

See [architecture documentation rules](architecture-documentation-rules.md)
for WHO/WHAT/WHEN/WHERE/WHY framing in introductions, and [deprecating
design documentation](deprecating-design-documentation.md) when a document's
purpose has expired.
