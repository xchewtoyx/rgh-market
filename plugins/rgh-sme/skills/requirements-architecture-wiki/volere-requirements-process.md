---
type: concept
title: Volere Requirements Process
description: >
  The Volere process is a technology-agnostic roadmap for discovering,
  specifying, and verifying requirements — blastoff, scoping, trawling,
  scenario elaboration, atomic specification, and a quality gate — that
  adapts to waterfall, agile, or outsourced delivery.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 2"
---

The Volere process is a structured roadmap for requirements work, moving
through: [project blastoff](project-blastoff.md) (establish purpose,
stakeholders, and constraints), [scoping the work](scope-of-work-vs-scope-of-product.md),
[trawling for requirements](requirements-elicitation-techniques.md)
(active discovery, not passive gathering — see [requirements discovery vs.
gathering](requirements-discovery-vs-gathering.md)),
[elaborating scenarios and prototypes](scenario-for-business-use-case.md),
writing each discovered requirement as an
[atomic requirement shell](atomic-requirement-shell.md), and passing every
candidate requirement through the [quality gateway](quality-gateway.md)
before it enters the specification or backlog.

The process is deliberately technology- and methodology-agnostic. In a
waterfall or linear project, it produces a formal specification ahead of
construction. In agile or iterative delivery, the same stages still
happen, but progressively: blastoff and work scoping establish a
high-level roadmap once, business use cases become epics, and individual
[atomic requirements with fit criteria](fit-criterion.md) are discovered
just-in-time as user stories and acceptance criteria within sprints — see
[adapting the requirements process to delivery
model](adapting-requirements-process-to-delivery-model.md). In outsourced
or off-the-shelf (COTS) projects, the same stages shift weight toward
[non-functional requirements](non-functional-requirement.md) and fit
criteria as vendor-selection benchmarks.

What stays constant across all of these adaptations is the underlying
knowledge model: a project goal is achieved by
[business use cases](business-event-and-use-case.md), each requiring one
or more atomic requirements, each of which must have a fit criterion — see
[requirements traceability](requirements-traceability.md) for these
associations in full.
