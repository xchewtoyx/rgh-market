---
type: concept
title: Requirements Traceability
description: >
  A fixed chain of associations — goal, business event, use case,
  requirement, fit criterion — lets any requirement be traced back to why
  it exists and forward to what satisfies it.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 2, Appendix D"
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 10"
---

Volere's requirements knowledge model fixes a specific chain of
associations, and traceability means keeping every requirement
attached to it, in both directions: a **project goal** (set at [project
blastoff](project-blastoff.md)) is achieved by one or more
[business use cases](business-event-and-use-case.md); a business event
triggers exactly one business use case; a business use case contains one
or more product use cases; a product use case requires one or more atomic
requirements; and every atomic requirement must have exactly one [fit
criterion](fit-criterion.md). A requirement that can't be traced back
along this chain to a business event, or forward to a fit criterion, is
incomplete — this is exactly what the [quality
gateway](quality-gateway.md) checks for.

On the architecture side, the same discipline continues past the
requirement into the design: architecture documentation packages record
requirement-to-element mappings and CRUD-style mappings that make the
correspondence between a requirement and the structural elements that
satisfy it inspectable, rather than assumed — see [architecture
documentation package](architecture-documentation-package.md). Notations
like SysML make this explicit with named relations (satisfy, verify,
derive, refine) between a requirement and a design element; see
[architecture modeling notations](architecture-modeling-notations.md).

Traceability is what makes [requirements completeness
checking](requirements-completeness-checking.md) possible in the first
place: you can only audit "does every entity have a Create, Read, Update,
and Delete process" or "does every incoming data flow trigger a defined
response" by walking this same chain of associations systematically,
rather than by re-reading the whole specification looking for gaps.
