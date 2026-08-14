---
type: concept
title: Architecture Tradeoff Analysis Method (ATAM)
description: >
  A structured, outsider-led evaluation that walks an architecture's
  approaches against stakeholder-prioritized quality-attribute scenarios
  to surface risks, non-risks, sensitivity points, and tradeoffs before
  they become expensive to fix.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 21"
---

Architecture evaluation exists because architecture is supposed to let
you predict a system's qualities before it's built — evaluation is where
that prediction is actually checked, and it's worth doing whenever its
cost stays below the risk it can catch. Risk here is concrete: probability
of a bad outcome times its impact, and evaluation *identifies* that risk
rather than fixing it, which is a separate cost/benefit call made
afterward.

ATAM is the comprehensive, outsider-led version of this: a 3–5 person
evaluation team external to the project (with named roles — team leader,
evaluation leader, scenario scribe, questioner) works with the project's
decision makers and a broader stakeholder group (often 10–25 people) over
four phases — informal preparation, a two-part evaluation session, and a
follow-up report. The evaluation session itself walks nine steps:
presenting the method, presenting business goals, presenting the
architecture, identifying the architectural approaches (patterns and
tactics) actually used, building a [utility tree](utility-tree.md) that
turns vague goals into ranked concrete scenarios, analyzing the
architecture against the highest-ranked scenarios, then — after adding the
full stakeholder group — brainstorming and prioritizing a second,
broader scenario set the same way a [Quality Attribute
Workshop](quality-attribute-workshop.md) does, re-analyzing against that
set, and presenting results grouped into cross-cutting **risk themes**
mapped back to the specific business goals each theme threatens.

**Lightweight Architecture Evaluation (LAE)** is the same method scaled
down for routine, project-internal peer review: run by the project's own
architect in hours rather than days, usually scoped to just what changed
since the last review rather than the whole system, with the full-blown
stakeholder-brainstorm step dropped or heavily abbreviated. It trades
some objectivity — an internal team surfaces fewer novel or dissenting
views than a genuine outsider does — for being cheap enough to run
routinely rather than reserved for major milestones. An even lighter
option for a single quality attribute is the [tactics-based
questionnaire](tactics-based-questionnaire.md), usable solo by the
architect in about an hour per attribute.

See [risk and tradeoff points](risk-and-tradeoff-point.md) for the
vocabulary these evaluations use to record what they find, and
[architecture documentation review](architecture-documentation-review.md)
for the related but distinct activity of reviewing whether the
*documentation* itself is correct and complete, as opposed to whether the
*design* it describes is fit for purpose.
