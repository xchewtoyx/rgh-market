---
type: concept
title: Sensitive Dependence on Initial Conditions (in Accident Causation)
description: >
  A small, seemingly inconsequential early classification or design decision
  can cascade through a complex system's history and determine major
  downstream safety consequences decades later.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 1, ch. 2"
---

Borrowed from chaos theory's "butterfly effect": in a complex, tightly
coupled system, the size of a decision's downstream consequences bears no
relationship to the size or apparent importance of the decision itself. This
directly violates the proportional, linear cause-effect assumption of
[Newtonian-Cartesian accident thinking](newtonian-cartesian-accident-thinking.md)
— which is exactly why such decisions are invisible as risks when they are
made.

Two recurring shapes this takes in accident histories:

- **Grandfathering**: a component or subsystem, unchanged in a later product
  derivative, is exempted from re-certification under updated safety rules
  because only the *new* parts of the derivative are required to meet the
  newer standard. The result is a system still operating, decades later,
  under design assumptions that predate the regulatory regime everyone
  believes governs it.
- **Classification choice**: whether a piece of hardware is labelled a
  "structure" or a "system" (or similarly, "onshore" or "offshore") can
  determine which entire body of safety analysis applies to it. The
  classification is a localised, persuasion-driven engineering judgment made
  once, early, by people with no view of the decades of consequences it will
  gate — not a technical fact discovered by calculation.

A related design-time trap is [false analogue
transfer](false-analogue-transfer.md): justifying a decision by pointing to
a superficially similar precedent system that turns out to differ on
exactly the dimension that matters.

The practical implication: early classification and grandfathering decisions
deserve safety scrutiny disproportionate to how mundane they look at the
time, precisely because "mundane-looking but consequential" is what
sensitive dependence produces. By the time the consequence surfaces, the
original decision is long forgotten and does not read as part of the causal
story at all — reinforcing the [root-cause fallacy](root-cause-fallacy.md)
by making the actual sensitive point invisible to a chain-of-events search.
