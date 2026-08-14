---
type: concept
title: Irony of Resilience
description: >
  Blunt-end efforts to standardize and pre-plan every response strip
  sharp-end operators of exactly the autonomy and adaptability the system
  ends up depending on the one time an event falls outside what was
  anticipated.
sources:
  - title: Resilience Engineering in Practice
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

# Irony of Resilience

Jean Pariès's **irony of resilience** is the general form of [Bainbridge's
irony of automation](automation-bias.md): blunt-end managers and system
designers try to maximize safety by prescribing procedures, standardizing
behavior, and pre-planning responses for every contingency they can
anticipate. Within the boundaries those plans cover, this works — it raises
discipline, predictability, and efficiency. But when a real event falls
outside the anticipated envelope, the system has nothing left to fall back
on except sharp-end operators' autonomy, creativity, and adaptability — the
exact capabilities that the standardization effort spent years suppressing.

Where the irony of automation is specifically about a human losing manual
skill because a machine now performs a task, the irony of resilience is
broader: it applies to any blunt-end effort to eliminate operational
variability — procedures, checklists, standard operating boundaries,
automation — not automation alone. The mechanism producing it is the
[efficiency-flexibility trade-off](efficiency-flexibility-tradeoff.md): the
more tightly a system is adapted to a standard, expected environment, the
less adaptation bandwidth it retains for environments outside that standard.

Two things drive organizations into this trap without anyone deciding to
take the risk on purpose:

- The [fallacy of predetermination](fallacy-of-predetermination.md) — the
  belief that enough upfront planning and rule-writing can anticipate all
  future operational states, which makes each new round of proceduralization
  feel like it's closing a gap rather than narrowing the system's adaptive
  range.
- [Safeguards against runaway automation](safeguards-against-runaway-automation.md)
  and similar rule-based controls are, by construction, limited to the cases
  their rules cover — which is exactly why they need a deliberate human
  foothold left in place for the cases they don't.

Design responses that keep the irony from compounding into brittleness:
[unbriefed exposure to surprise](unbriefed-surprise-builds-uncertainty-competence.md)
deliberately rebuilds the sharp-end adaptive competence that proceduralization
erodes, and [embedding decision support directly into the
automation](embedding-decision-support-to-reduce-sharp-end-load.md) reduces
how much of that competence a sharp-end operator has to supply unaided
during a genuine surprise.
