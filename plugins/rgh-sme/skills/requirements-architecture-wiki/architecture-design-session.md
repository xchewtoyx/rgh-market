---
type: concept
title: Architecture Design Session
description: >
  A structured, whiteboard-driven workshop with business and technical
  stakeholders that produces a high-level architecture blueprint and a
  plan of action, run before any product or vendor is discussed.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (James Serra), ch. 3"
---

An Architecture Design Session (ADS) is a facilitated workshop that brings
business and technical stakeholders together to define and plan the
high-level design of a solution — distinct from a technical workshop,
training session, product demo, or low-level requirements session. It
produces two deliverables: a high-level architecture "blueprint" as a
starting point for the solution, and a plan of action (follow-on demos,
proofs of concept, product discussions). This is the same class of
technique as a [Quality Attribute
Workshop](quality-attribute-workshop.md) or [PALM](business-goal-driven-requirements.md)
— a facilitated, multi-stakeholder session that surfaces
[architecturally significant requirements](architecturally-significant-requirement.md)
directly from the people who hold them — specialized for the early,
whole-architecture stage of a data solution rather than for refining
quality-attribute scenarios against an architecture that already exists.

**Structure**: discovery first, solution later. The first hour or two is
spent entirely on the customer's current pain points, existing
architecture, prior technology decisions, use cases, and business context
— the customer does most of the talking. Jumping to a product
demonstration before discovery is complete risks solving a problem the
customer didn't actually have; see [requirement vs. design
decision](requirement-vs-design-decision.md) and [architecture before tool
selection](architecture-before-tool-selection.md) for the general
principle this discipline enforces at workshop scale. A [vendor-neutral
discovery questionnaire](vendor-neutral-discovery-questionnaire.md)
structures this discovery phase concretely.

**Whiteboarding, not slides**: the session is built around a live
whiteboard holding a rough architecture diagram plus running sections for
goals, pain points, and a parking-lot of off-topic or follow-up items.
Slides turn the session into a presentation; a whiteboard keeps it a
discussion. Pain points and goals are checked off as the architecture
addresses them, and by the end everything raised should be either resolved
on the whiteboard or explicitly scheduled as a follow-up — an
at-a-glance, self-auditing completeness check that also gives the debrief
materials a natural structure.

**Preparation** matters as much as the session itself: identify the
project's budget, timeline, and decision maker beforehand; hold a pre-call
with the customer to recap the understood problem, learn who's attending
and calibrate depth, walk the agenda, and ask what materials (existing and
draft architecture diagrams, supporting documents) they can bring;
rehearse with whatever whiteboarding tool will be used. Invite sponsors
from both business and IT, not just technical staff, so the session can
resolve cross-department blockers the same day rather than deferring them
— the same reason [Project Blastoff](project-blastoff.md) insists on
identifying every stakeholder class before analysis begins.

**Facilitation discipline**: park off-topic points on the whiteboard
rather than chasing them; check progress against the agenda at the
halfway point and, if behind, have the customer reprioritize the
remaining goals themselves rather than the facilitator silently dropping
items. Difficult participants (defensive, or convinced they already have
every answer) are defused by acknowledging the point and moving it
offline, not by arguing them down in front of the group.

**Follow-up**: shortly after the session, send the customer a summary
document, the exported whiteboard as the physical architecture record, an
action-item list, and detailed parking-lot items with owners — this is
the session's [requirement rationale](requirement-rationale.md) record,
capturing not just what was decided but what was raised and deferred and
why. Archive the whiteboard itself for reuse when planning future,
similar sessions.
