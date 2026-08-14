---
type: concept
title: Mandated Constraint
description: >
  A mandated constraint is a boundary fixed on the solution before
  analysis begins — budget, deadline, target platform, or legacy
  integration — that requirements discovery must work within rather than
  question.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 3"
---

A mandated constraint is a limit on the solution that is fixed before
requirements analysis begins, rather than discovered during it: a budget
ceiling, a hard release date, a required target technology platform, or a
mandatory integration with an existing legacy system. It is set at
[project blastoff](project-blastoff.md), by people with the authority to
set it (typically the client or sponsor), and requirements discovery works
within it rather than questioning it.

This is a different kind of boundary from a
[non-functional requirement](non-functional-requirement.md): an NFR
describes a quality the product must have and is itself subject to
[fit-criterion](fit-criterion.md)-style discovery and negotiation; a
mandated constraint is a given, imposed from outside the requirements
process, that narrows what solutions are even considered. Confusing the
two — treating a genuine business quality goal as if it were
non-negotiable, or treating an imposed limit as if it were open to
requirements-style trade-off discussion — wastes stakeholder time solving
a problem that was never actually open. Recording mandated constraints
explicitly, and separately from requirements proper, is what prevents that
confusion.

The default stance should still be to leave a design choice open: most
requirements admit more than one implementation option, and picking among
them is best left to whoever is best positioned to weigh the technical and
economic trade-offs at build time, not fixed up front as if it were a
constraint. A design choice earns mandated-constraint status only when
leaving it open would itself cause a problem — commonly, protecting a
cross-cutting property like supportability (e.g. mandating one database
technology across a product suite specifically so the team that has to
support all of them isn't stuck learning several). Whatever the reason, it
belongs in the record alongside the constraint itself: writing down only
"use Oracle" without *why* leaves nobody able to tell, later, whether the
constraint still applies or has quietly outlived its reason. Watch in
particular for the [incorporation-by-reference
hazard](incorporation-by-reference-hazard.md) when a mandated constraint
cites an external standard.
