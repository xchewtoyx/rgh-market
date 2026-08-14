---
type: concept
title: Volere Specification Template
description: >
  A 27-section template organizing everything a requirements
  specification needs to hold — project drivers, constraints, functional
  and non-functional requirements, and open project issues — into one
  non-redundant structure.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), Appendix A"
---

The Volere template organizes a complete requirements specification into
27 sections under four groups. **Project drivers**: purpose and
measurable project goal; stakeholders; [mandated
constraints](mandated-constraint.md). **Project constraints**: naming
conventions and terminology; relevant facts and assumptions.
**Functional requirements**: [scope of the work](scope-of-work-vs-scope-of-product.md);
the business data model; scope of the product; [functional and data
requirements](functional-requirement.md), written as [atomic requirement
shells](atomic-requirement-shell.md). **Non-functional requirements**:
the eight [Volere categories](non-functional-requirement.md) — look and
feel, usability, performance, operational/environmental,
maintainability/support, security, cultural, legal. **Project issues**:
open questions, off-the-shelf/COTS options, impact on existing systems and
workflows, tasks, migration plan, risks, costs, user documentation and
training, a "waiting room" for deferred requirements, and implementation
ideas captured without letting them constrain the requirement itself.

The template's purpose is completeness and non-redundancy: every kind of
requirements knowledge has exactly one designated place to live, so a
reader (or an auditor doing [completeness
checking](requirements-completeness-checking.md)) knows where to look for
something and can tell when a section has been left empty rather than
simply not written yet. The "waiting room" and "ideas for solutions"
sections are worth noting specifically: they give an explicit, sanctioned
place to record a good idea that isn't actually a current requirement,
rather than forcing it into the requirements list where it would
contaminate scope, or discarding it where it would be lost.
