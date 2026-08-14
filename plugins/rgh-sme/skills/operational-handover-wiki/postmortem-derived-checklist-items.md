---
type: concept
title: Postmortem-Derived Checklist Items
description: Building and refining checklist items by systematically cataloguing past mistakes across every stage of a process, rather than deriving items from theory alone.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 8"
---

The most reliable source for a new checklist item is not a hypothetical failure mode reasoned out in advance — it is a mistake that actually happened. Practitioners across domains (aviation, surgery, investment management) converge on the same technique: catalogue errors as they occur across each stage of the process, then turn recurring or costly patterns into explicit, checkable items.

## The Technique

- **Segment the process into stages**: Break the overall workflow into distinct phases (e.g. research, decision, execution, post-decision monitoring) and track where failures actually occurred within that breakdown, not just that a failure occurred.
- **Catalogue specific incidents, not just categories**: A single well-understood incident can generate a precise, durable checklist item. For example, a specific missed-context mistake ("the target's recent financials looked strong but were inflated by a temporary boom condition") becomes a specific, checkable item ("confirm whether recent performance is inflated or depressed by temporary conditions") — not a vague reminder to "be careful."
- **Revisit the catalogue as new mistakes occur**: Treat the checklist as a running record of institutional near-misses and failures. Each new incident is a candidate for a new or revised item, not just an isolated lesson learned once and forgotten.

## Why This Beats Deriving Items from Theory

Items reasoned out from first principles tend to be generic and hard to act on ("consider all risks"). Items derived from an actual incident are specific, concrete, and immediately actionable, because they encode exactly what was missed and how it would have been caught. This also gives checklist authors a defensible answer to "why is this item here" during [item selection trade-offs](checklist-item-selection-tradeoffs.md) — it earned its place by having actually caused harm, not by seeming prudent in the abstract.

For the training practice of having individual operators study past incidents (as opposed to using them to author checklist items), see [On-Call Onboarding and Training](on-call-onboarding-and-training.md). For who is responsible for running this cataloguing process on an ongoing basis, see [Dedicated Function for Operational Learning](dedicated-function-for-operational-learning.md).
