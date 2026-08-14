---
type: concept
title: Requirements Are Discovered, Not Gathered
description: >
  Stakeholders do not hold a ready-made specification in their heads;
  requirements have to be actively uncovered through investigation, and
  stakeholders often only recognize what they want once they see a
  candidate solution.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 1"
---

Requirements are not sitting out there waiting to be collected from
stakeholders the way you'd collect answers to a survey. Stakeholders
generally don't hold a complete, coherent specification in their heads —
they hold habits, assumptions they've stopped noticing, and a tendency to
describe the solution they're used to rather than the underlying need.
Getting from that starting point to an actual requirement takes active
investigation ("trawling" — see [requirements elicitation
techniques](requirements-elicitation-techniques.md)), not passive
transcription of what someone says in one interview.

A related and equally load-bearing observation: stakeholders often don't
know precisely what they want until they see a candidate answer — a
prototype, a scenario walkthrough, a mockup. This is why requirements
discovery is treated as iterative rather than a single up-front
information-collection exercise: showing a concrete candidate and
capturing the "no, but..." reaction it provokes is itself a discovery
technique, not a validation step that happens only after requirements are
already written. See [scenario for business use
case](scenario-for-business-use-case.md) for the concrete technique this
motivates.

The practical consequence for documentation: a requirement that was only
ever asked for once, in one interview, without being cross-checked against
observed behavior or a walked-through scenario, should be treated as a
candidate, not as settled — it hasn't yet been through the discovery
process this principle describes.

An [opportunity solution tree](opportunity-solution-tree.md) is one
concrete way to keep this iterative discipline visible as a maintained
artifact rather than a one-off round of interviews: it makes the current
state of discovery — which needs are understood, which solutions are
being compared, which are still unverified — legible at a glance, and its
shape tells the team what kind of discovery work is still missing.
