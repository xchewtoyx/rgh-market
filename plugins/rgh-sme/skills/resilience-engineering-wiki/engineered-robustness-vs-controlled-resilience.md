---
type: concept
title: Engineered Robustness versus Controlled Resilience
description: >
  Design features that make a system robust against expected anomalies are
  not the same thing as resilience — resilience additionally requires
  deliberately harnessing human adaptive capability, which is itself a
  double-edged asset that must be tuned, not just permitted.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 5"
---

Fujita's distinction: engineered features built into an artefact by its
designers give it **robustness** against the anomalies those designers
anticipated. Robustness alone does not add up to resilience, because it can
only cover the envelope the designer thought to build for — see [the
boundary of potential variability](boundary-of-potential-variability.md) for
why events outside that envelope are a qualitatively different problem that
engineered robustness cannot, by construction, reach.

The remaining capability a system needs comes from its front-line
people — operators, maintenance staff — who bring genuine adaptiveness and
proactive problem-solving that no design process can fully specify in
advance. But this capability is a **double-edged asset**: the same
adaptiveness that lets an operator improvise a save no designer anticipated
can also, uncontrolled, precipitate a catastrophe no designer anticipated
either. Human flexibility is not automatically a safety asset; it is
inherently unresolved in direction until something channels it.

**A system is resilient, on this view, only when it is deliberately tuned to
use its total potential — engineered robustness and human adaptive capacity
together — in a *controlled* manner, across both expected and unexpected
situations.** Controlled here does not mean suppressed: it means the
adaptive capacity is actively integrated with the engineered design rather
than left as an unmanaged wildcard bolted on beside it. This is the same
underlying trade-off [adapted versus adaptive](adapted-vs-adaptive-trade-off.md)
names at the level of a whole system's tuning between optimisation and
flexibility, applied specifically to the human-versus-engineered split: a
design that treats robustness as sufficient and human adaptiveness as noise
to be minimised has picked "adapted" and given up the "adaptive" half of the
trade-off, while a design that leaves human adaptiveness completely
unconstrained has kept flexibility but abandoned the control that [resilience
as control](resilience-as-control.md) argues is what "in control" actually
means.
