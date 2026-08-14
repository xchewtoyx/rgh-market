---
type: concept
title: Sensitivity Points and Tradeoff Points
description: >
  Label each decision point in an options analysis as moving one
  criterion (a sensitivity point) or several criteria in opposite
  directions (a tradeoff point), so the analysis names exactly
  where the real disagreement lives.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 21"
---

Not every decision inside an options analysis carries the same kind
of consequence, and naming the difference makes the analysis more
useful than a flat list of pros and cons per option. A **sensitivity
point** is a decision with a marked effect on a single evaluation
criterion — moving it materially changes how well one thing is
served, without meaningfully touching the others. A **tradeoff
point** is a decision where two or more criteria are both sensitive
to it, but move in opposite directions — improving one necessarily
costs the other. Worked example: raising a monitoring system's
polling frequency is a sensitivity point for detection speed alone if
nothing else moves; it becomes a tradeoff point the moment the same
frequency increase also degrades response time, because now the
decision is simultaneously helping one criterion and hurting another.

The distinction changes what kind of scrutiny a decision needs.
Sensitivity points can usually be pushed as far as the single
criterion warrants, limited only by cost — there is no opposing
force to balance against. Tradeoff points are exactly where a
recommendation needs to state, explicitly, how much of one criterion
was given up for how much of the other, and why that exchange rate
was accepted — a tradeoff point left unnamed is a decision whose real
cost is invisible to anyone reading the recommendation later.

This gives
[fair-treatment-of-objections](fair-treatment-of-objections.md) a
concrete place to focus: an objection to a sensitivity point is
usually an objection to how far it was pushed, while an objection to
a tradeoff point is usually a disagreement about which criterion
should have won — a different kind of disagreement that needs the
underlying weights made explicit, not just more evidence for the
side already chosen. It also sharpens
[multi-lens-comparison-without-false-precision](multi-lens-comparison-without-false-precision.md):
tradeoff points are precisely the decisions where collapsing lenses
into one score would hide the exchange being made, so they are the
first candidates to keep visibly separate rather than combined.
