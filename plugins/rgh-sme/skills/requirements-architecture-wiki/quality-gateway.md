---
type: concept
title: Quality Gateway
description: >
  The quality gateway is a formal review that every candidate requirement
  must pass — completeness, traceability, consistency, measurability, and
  necessity — before it is accepted into the specification or backlog.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 13"
---

The quality gateway is the checkpoint every candidate requirement passes
through before it is accepted into the specification, product backlog, or
architecture baseline — rejected requirements return to the originating
analyst or stakeholder for revision rather than silently entering the
system half-formed. The checks:

1. **Completeness** — are the mandatory fields (ID, type, description,
   [rationale](requirement-rationale.md), [fit criterion](fit-criterion.md),
   originator) all filled in?
2. **Traceability** — is the requirement linked to a specific [business
   use case](business-event-and-use-case.md) and the project goal? See
   [requirements traceability](requirements-traceability.md).
3. **Consistency** — does it contradict an already-accepted requirement?
4. **Ambiguity** — does the wording contain subjective or fuzzy language?
5. **Measurability** — does it have a valid, quantifiable fit criterion?
6. **Viability/feasibility** — is it achievable within budget and
   schedule?
7. **Gold plating** — is it actually necessary for business success, or an
   expensive extra one stakeholder wants?

The gateway's value is catching a flawed requirement while it's still
cheap to fix — before it has propagated into a design, an implementation,
or a test suite built to satisfy it. It plays the same structural role for
requirements that [architecture documentation
review](architecture-documentation-review.md) plays for design: a
checkpoint with an explicit question set, applied before the artifact's
cost of being wrong goes up.
