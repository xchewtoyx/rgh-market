---
type: concept
title: Requirements Completeness Checking
description: >
  Systematic audits — CRUD checks, custodial-process checks, and
  event-response audits — find missing requirements that no single
  reading of the specification would surface.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 17"
---

A requirements specification can look thorough on a read-through and still
be missing whole categories of requirement, because the gaps are gaps in
*coverage*, not gaps in any individual statement. Volere's completeness
techniques check coverage systematically rather than relying on a careful
reader to notice an absence:

- **CRUD check** — for every entity in the data dictionary, confirm there
  is a [business use case](business-event-and-use-case.md) that Creates
  it, Reads it, Updates it, and Deletes or archives it. A missing CRUD
  operation for an entity that clearly needs one is a missing requirement,
  not an intentional omission — most such gaps are simply requirements
  nobody thought to ask for because they aren't the "main" feature.
- **Custodial process check** — confirm background management functions
  exist (adding a new resource, updating a limit, modifying a permission)
  that keep the system usable over time, as distinct from its primary
  transactional use cases.
- **Event response audit** — confirm every incoming data flow on the
  [context diagram](context-diagram.md) actually triggers an identified
  business use case with a defined output response.

These checks are only possible because [requirements
traceability](requirements-traceability.md) exists to walk against — you
can't run a CRUD check without a data dictionary linked to use cases, and
you can't run an event-response audit without a context diagram linked to
business events. Completeness checking is the traceability chain used as
an audit tool rather than a lookup tool. See also [quality
gateway](quality-gateway.md) for the per-requirement checks this
specification-level auditing complements.
