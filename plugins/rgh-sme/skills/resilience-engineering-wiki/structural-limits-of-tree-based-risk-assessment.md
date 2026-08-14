---
type: concept
title: Structural Limits of Tree-Based Risk Assessment
description: >
  FMEA, event trees, and fault trees all assume fixed structural
  relationships between components, which makes them blind to the dynamic
  couplings and simultaneous ordinary-event interactions that produce
  accidents in complex systems.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 1"
---

The standard risk-assessment toolkit mirrors whichever accident model
produced it, and each tool inherits that model's blind spots:

- **Failure Mode and Effects Analysis (FMEA)** — enumerates single-component
  failure modes and their local effects. Built for a model where components
  fail independently.
- **Event trees** — binary branching sequences projecting forward from one
  initiating event. Built for the [chain-of-events
  model](chain-of-events-model.md)'s assumption of a single originating
  cause.
- **Fault trees** — logical AND/OR combinations of conditions leading to one
  top-level failure. An improvement over event trees, but still a fixed
  graph of predetermined relationships.

All three represent risk as a fixed structure — a tree or graph whose edges
are decided in advance. That representation cannot capture **dynamic
couplings**: relationships between parts of the system that only exist,
or only matter, under specific transient conditions, and that no
fixed diagram anticipated. Nor can it represent **concurrence** — the
systemic-model insight that catastrophic outcomes typically arise from
several individually ordinary events or conditions happening to co-occur in
time, rather than from any single event propagating along a pre-specified
path. A tree has to be drawn before the co-occurrence it would need to
represent is known to matter.

The practical consequence is a form of [the root-cause
fallacy](root-cause-fallacy.md) built into the tooling itself: an
organisation using tree-based methods will keep finding single-component
failure modes because that is the only shape of answer its tools can
produce, regardless of whether the systems it analyses still fail that way.
Hollnagel's own response is a genuinely functional model — Functional
Resonance Analysis (FRAM) — built to represent variability and coupling
between normal functions directly, rather than forcing them into a
predetermined tree; the detailed method is outside this bundle's scope, but
the reason it exists is the gap documented here.
