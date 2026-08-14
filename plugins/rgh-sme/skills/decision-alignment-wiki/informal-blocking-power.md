---
type: concept
title: Informal Blocking Power
description: >
  Stakeholders who hold no formal approval authority can still
  stall a decision indefinitely through routine levers they
  control, so excluding them as "attached to the old way" is
  a real risk, not just a courtesy failure.
sources:
  - title: "Observability Engineering (2nd Edition)"
    resource: "Observability Engineering (2nd Edition) (Charity Majors, Liz Fong-Jones, George Miranda), ch. 28"
---

Formal approval authority — who must sign off — is only part
of who can actually stop a decision from taking effect. Some
stakeholders sit outside the approver ring entirely and still
control a routine, unglamorous lever the implementation
depends on: an allocation queue, a configuration step, an
access grant, anything that requires their ordinary
cooperation to move at normal speed. Dismissing such a person
as merely "attached to the old way" and sidelining them from
the decision does not remove their leverage — it only removes
their motivation to use it in the decision's favor. A
documented case: an architect passed over during a
modernization effort, whose objections were read as legacy
attachment rather than substantive, controlled IP allocation
and silently slowed approvals for weeks — not through open
opposition, but through the ordinary friction of an
uncooperative gatekeeper doing exactly the job he still held.

This is a distinct failure from the one
[stakeholder-analysis-attributes](stakeholder-analysis-attributes.md)
already names — collapsing the *approver* ring to too few
people. Here the person was never meant to be an approver at
all; the miss is failing to recognize that **operational
levers grant a kind of blocking power that formal role does
not capture**, so a stakeholder map built only from titles and
sign-off authority can still miss the person actually able to
stall the work. When profiling stakeholders, ask explicitly
what routine approvals, resources, or steps this person
controls, independent of whether they hold a formal decision
role — and treat someone who has quietly "held it together" in
the current system as carrying standing and levers worth
including deliberately, not skepticism to route around.

The people holding this kind of power are also often carrying
institutional knowledge the new approach has not yet
accounted for, which makes early inclusion doubly valuable:
it converts a potential silent blocker into a source of
information that
[fair-treatment-of-objections](fair-treatment-of-objections.md)
can actually use, rather than a person deciding — invisibly —
whether the plan proceeds.
