---
type: concept
title: Value of Automation
description: >
  Automation is worth building because it executes identically every time,
  runs faster than a human, hides low-level operational detail behind a
  declarative interface, and lets a small team manage a large, growing
  system without headcount growing to match.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7"
---

# Value of Automation

Four distinct benefits make automation worth the engineering investment,
and they're worth naming separately because a given piece of automation
might deliver only one or two of them:

- **Consistency**: the same operation executes identically every time,
  removing the variation a human introduces run to run.
- **Speed**: a machine executes a complex multi-step workflow orders of
  magnitude faster than a human working through the same steps.
- **Decoupling the operator from the platform**: automation abstracts
  low-level operational detail behind a declarative API, so the person
  invoking it doesn't need to understand every mechanical step underneath.
- **Scale**: a small team can operate a system with tens of thousands of
  components without headcount growing proportionally to that count.

That last point is the direct counterpart to
[the case for eliminating toil](case-for-eliminating-toil.md): automation is
the mechanism, sublinear headcount growth is the payoff. Where a piece of
automation sits on the [automation maturity
spectrum](automation-maturity-spectrum.md) determines how much of this value
it has actually captured — a playbook script delivers consistency and speed,
but only an internal service or autonomous system delivers the scale
benefit.
