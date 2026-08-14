---
type: concept
title: Choosing Architecture Views
description: >
  Which architecture views to produce is decided by mapping stakeholders
  to their concerns and questions, then selecting the smallest set of
  views that covers them — not by adopting a fashionable set of diagrams.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 9"
---

Architecture documentation exists to support stakeholders doing real
tasks, not to satisfy a fixed checklist of diagram types. The method is:
list the stakeholders, list each one's concerns and the specific questions
or tasks they need the documentation to support, map those concerns to
candidate [views](view-and-viewpoint.md) and supplementary information,
then select the smallest set of views that covers them. Prioritize and
document that set, validate the selection with the stakeholders it's
meant to serve, and revisit the selection as requirements and audiences
change.

Typical stakeholder needs differ predictably: developers need
decomposition and interfaces; testers need behavior and fault/coverage
implications; operators need deployment and installation information;
managers need work assignment, schedule, and risk information; customers
and users need context and capability; analysts need whatever structures
support the quality-attribute reasoning they're doing. A missing view is
only a risk if it leaves a real stakeholder concern uncovered — producing
a view nobody asked a question that requires is waste, not thoroughness.
