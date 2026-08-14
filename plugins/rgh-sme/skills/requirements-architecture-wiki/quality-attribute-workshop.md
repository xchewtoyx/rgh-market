---
type: concept
title: Quality Attribute Workshop
description: >
  A facilitated, stakeholder-driven workshop that generates, prioritizes,
  and refines quality-attribute scenarios before the architecture is
  finalized, so architecturally significant requirements come from the
  people who hold them rather than from the architect's guesswork alone.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 19"
---

A Quality Attribute Workshop (QAW) is a structured session for surfacing
[architecturally significant
requirements](architecturally-significant-requirement.md) directly from
stakeholders, run before the architecture is settled rather than used to
validate it afterward. It runs in seven steps:

1. **Business/mission presentation** — a business stakeholder covers
   context, functional requirements, and constraints in about an hour;
   this is the primary source the later quality-attribute refinement
   draws on.
2. **Architectural plan presentation** — whatever architecture artifacts
   already exist are shared, so every stakeholder starts from the same
   picture of current thinking.
3. **Identification of architectural drivers** — facilitators present a
   distilled list of requirements, business drivers, constraints, and
   quality attributes, and stakeholders correct it until it reflects a
   shared understanding.
4. **Scenario brainstorming** — each stakeholder proposes a scenario for
   their own concern; the facilitator checks each one for an explicit
   stimulus and response before accepting it.
5. **Scenario consolidation** — near-duplicate scenarios are merged, but
   only with the proposer's agreement that nothing was diluted in the
   merge.
6. **Scenario prioritization** — each stakeholder gets a vote allowance
   equal to 30% of the post-consolidation scenario count, freely
   allocable across scenarios, tallied to produce a ranking.
7. **Scenario refinement** — the top-ranked scenarios are elaborated into
   the full six-part [quality attribute
   scenario](quality-attribute-scenario.md) form, with any satisfaction
   issues logged as they surface, for as long as the workshop has time.

The output — a driver list plus a stakeholder-ranked, fully elaborated
scenario set — is usable directly to refine requirements, clarify
disputed drivers, justify later design decisions against a documented
stakeholder consensus, guide prototyping priorities, and sequence which
parts of the architecture get worked out first. Because prioritization
happens by stakeholder vote rather than architect judgment, it also
produces a defensible answer to "why did we spend design effort here and
not there" that a design document can cite directly.

See [business-goal-driven requirements](business-goal-driven-requirements.md)
for a parallel workshop technique that starts from business goals rather
than stakeholder-proposed quality scenarios, and [requirements elicitation
techniques](requirements-elicitation-techniques.md) for the general
workshop discipline this specializes.
