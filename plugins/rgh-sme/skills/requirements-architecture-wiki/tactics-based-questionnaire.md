---
type: concept
title: Tactics-Based Questionnaire
description: >
  A lightweight, per-quality-attribute audit that records whether each
  known tactic is supported, where the deciding design lives, its risk
  level, and the rationale — including the rationale for not using it.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 3"
---

A tactics-based questionnaire walks the known [tactics](architectural-tactic.md)
for one quality attribute and, for each one, records four things: whether
the system's architecture supports it (yes/no), the risk of using it or
not using it (high/medium/low), the specific design decision and where it
lives in the codebase (module, framework, package — useful for later
architecture reconstruction as well as review), and the rationale behind
the choice, including the rationale for deliberately *not* adopting a
tactic and what that costs in schedule, cost, or future evolution.

Its value is less in the checklist itself than in what filling it out
forces: a step back to a big-picture view of one quality attribute across
the whole system, in a form that takes roughly 30–90 minutes per attribute
and can be redone at any point in a design's maturity to see how the
answers have shifted. Because it captures rationale for tactics
deliberately rejected as well as ones adopted, it produces the same kind
of reviewable record that an [architectural decision
record](architectural-decision-capture.md) does, but scoped to a single
quality attribute and cheap enough to repeat routinely rather than reserved
for one-off significant decisions.
