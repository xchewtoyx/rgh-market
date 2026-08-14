---
type: concept
title: Capability Model vs. Maturity Model
description: >
  A capability model treats delivery improvement as multidimensional and
  continuous, tied to outcome metrics, rather than a linear ladder of stages
  with a final "done" level.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 1"
---

# Capability Model vs. Maturity Model

Maturity models frame improvement as a fixed, linear sequence of stages
(Level 1 through Level 5) that every team progresses through in lock-step
toward a finite "done" state, usually assessed against static checklists or
tool-adoption counts (vanity metrics).

A capability model instead treats delivery practice as multidimensional,
dynamic, and tied directly to outcomes: each capability (e.g. trunk-based
development, deployment automation, test automation) is evaluated by whether
it measurably moves the [DORA four key metrics](dora-four-key-metrics.md),
not by whether a team has checked a box. There's no final destination, because
the target keeps moving as the industry's baseline performance improves —
"good enough" a few years ago is a low performer now.

This is a caveat on any staged assessment framework used for delivery
improvement, including the
[continuous delivery maturity model](delivery-maturity-model.md): use such a
framework to locate weak dimensions, but treat "reaching the top level" as a
category error rather than a goal, and always tie the assessment back to
whether it actually moves outcome metrics.
