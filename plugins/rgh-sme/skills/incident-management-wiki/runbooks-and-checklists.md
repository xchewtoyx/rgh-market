---
type: concept
title: Runbooks and Checklists
description: Operational tools designed to reduce cognitive load, enforce discipline, and guide incident response under stress.
sources:
  - title: "The Checklist Manifesto"
    resource: "The Checklist Manifesto: How to Get Things Right (Atul Gawande), Introduction, ch. 1, ch. 2, ch. 3, ch. 4, ch. 5, ch. 6, ch. 7, ch. 8"
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 13"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan), ch. 2"
---

In high-stress incident environments, cognitive capacity degrades due to fatigue, distraction, and pressure. Runbooks (also known as non-normal checklists or emergency [playbooks](playbooks-layer-business-context.md)) protect systems by establishing minimum necessary steps and reducing cognitive load. See [checklist design rules](checklist-design-rules.md) for how to design one that survives actual use under stress.

### The Limits of Runbooks
While checklists enforce procedural discipline, they have limits. In complex socio-technical systems, not all failure modes are predictable. If organizations treat runbooks as rigid rules, they widen the gap between [work-as-imagined vs work-as-done](work-as-imagined-vs-work-as-done.md). Runbooks must be treated as flexible resources for action, supplemented by operator skill, and continually updated through [blameless postmortems](blameless-postmortems.md) and [preparedness drills](preparedness-drills.md).

A useful way to predict where a runbook will and won't hold up: Zimmerman
and Glouberman's distinction between **simple** problems (a repeatable
recipe reliably works — this is the checklist's home turf), **complicated**
problems (many simple parts coordinated by different specialists, where
timing and communication matter as much as any individual step — the
"communication forcing function" below exists for exactly this case), and
**complex** problems (unique, non-repeatable situations where past
experience doesn't guarantee the next outcome and real-time adaptive
judgment is required, not a fixed sequence). An incident that's actually
complex will defeat any runbook no matter how well designed — the runbook
gets a responder through the complicated, coordinable parts of the
incident, and skilled human judgment has to carry the rest.

### Two Kinds of Checklist Item
Effective checklists combine two complementary forcing functions, and
conflating them produces a checklist that's good at neither. A
**procedural forcing function** ensures a basic, predictable, but
easy-to-skip-under-stress step actually happens — the runbook items covered
by [checklist design rules](checklist-design-rules.md). A **communication forcing function** creates a mandatory touchpoint
for responders to exchange information and surface risks that no
individual step could anticipate — for example, a structured verbal
read-back between roles ("confirmed: rolling back service X") rather than
a silent assumption that an instruction landed, or a brief structured
huddle at incident start to share what's non-routine about this particular
situation before diving into the runbook. Both belong in a mature incident
response process; the runbook covers the first, and the [incident command
system](incident-command-system.md)'s status-update cadence covers the
second.

### Runbooks as Living Documents
A runbook that never changes has stopped tracking how the system actually
fails. Aviation checklists are revised constantly rather than treated as
settled — Boeing publishes more than 100 new or revised checklists a year,
each carrying a publication date as a reminder that it is expected to
change. A runbook is only useful as long as it aids the responder using it;
when it stops aiding them, the correct response is to fix the runbook, not
to keep following it out of deference to the document.

### Why Checklists Work as a Leverage Intervention
Compared to other ways of trying to improve how people behave under
pressure, checklists occupy a specific niche. Training programs are
expensive to deliver at scale and fade without reinforcement.
Pay-for-performance incentives produce only modest gains and invite gaming
the metric rather than the underlying behavior. Publishing comprehensive
expert guidance changes nothing on its own — a shelf of manuals doesn't
change what happens at the moment of pressure. A checklist works because
it's a **leverage intervention**: simple, measurable, and easy to transmit,
that intervenes at the exact trigger point where the behavior needs to
happen, rather than trying to upgrade the practitioner's general knowledge
or motivation beforehand.

An early, unrefined attempt shows what happens when a checklist is adopted
without rigorous design: in one field test, a circulating nurse completed
an entire draft checklist silently on paper beforehand ("where does it say
it's a verbal team checklist?"), and the list itself was long, ambiguous,
and confusingly worded enough to delay care and frustrate the team.
Checklists fail exactly the same way runbooks fail when they skip the
[checklist design rules](checklist-design-rules.md) (brevity, verbal team dialogue, iterative field
testing) — writing one down is not the same as making it work.

### Cultural Resistance to Runbooks
Adoption of checklists tends to be top-down (safety officers, engineering
leadership) rather than bottom-up, because practitioners often experience a
mandated procedure as interference with their professional autonomy rather
than as a tool. This resistance is a cultural obstacle, not a rational
objection to the evidence — see [procedural
heroism](procedural-heroism.md) for the belief driving it and why
disciplined procedure use, not improvisation, is the more reliable form of
skill under pressure.
