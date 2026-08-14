---
type: concept
title: Visual Affordances for Charts
description: >
  Form follows function in data display: decide what the audience must do
  with the data, then make that use obvious through highlighting at most
  about 10% of the visual, removing distractions, and a clear visual
  hierarchy.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 5–6"
---

Affordances are design cues that make the intended use obvious (a knob
affords turning). On a chart, visual affordances tell the audience where to
look and how to read without conscious decoding — when they are sufficient,
good design fades into the background. Start from **form follows function**:
decide what the audience should be able to do with the data, then choose a
form that enables it easily.

Three complementary moves create those affordances:

1. **Highlight the important stuff.** Use
   [preattentive attributes](preattentive-attributes-for-dashboards.md), but
   only on a fraction of the visual — Lidwell et al. recommend highlighting at
   most about **10%**; beyond that, emphasis dilutes. Prefer bold over italics
   or underlining for short text; use uppercase for short scanned labels, not
   typeface-switching; combine color sparingly with another cue; use size for
   importance; avoid blinking/flashing in explanatory communication. Layer
   attributes when something is truly critical (large + colored + bold). If
   the wrong series is darker by default, recolor so only the story series
   carries the accent and everything else sits in grey — see
   [vivid color restraint](vivid-color-restraint.md).
2. **Eliminate distractions.** Perfection is having nothing left to take away.
   Interrogate both [clutter](minimize-extraneous-cognitive-load.md) and excess
   context. Cut noncritical series, summarize when detail is unnecessary, ask
   whether removing an element changes anything, push necessary-but-
   non-message items to light grey, and park supplementary detail in an
   appendix rather than diluting the main view. Prefer chart types that reduce
   element count when they still answer the question (e.g., four lines instead
   of twenty-five bars for a trend story). Match
   [numeric precision to the audience](customize-numeric-presentation-to-audience.md).
3. **Create a clear [visual hierarchy](visual-hierarchy-with-preattentive-attributes.md).**
   Pull some items forward and push others back so processing order is
   implicit. Super-category labels (e.g., grouping many demographics under
   age/race/income) give a simplifying construct; quadrant labels on a
   scatter can replace mental derivation of axis crossings. Different viewers
   may still enter at detail or at "so what" first — both work when hierarchy
   is clear.

Together, these moves make understanding *afforded* rather than forced.
There is rarely a single "right" chart — only intentional "flavors of good"
for the same data. Accessibility in the broad sense — usable by people
without the designer's specialist background — is the designer's
responsibility: if a graph looks complicated, audiences perceive it as harder
and invest less time (Song and Schwarz, 2008). Keep typefaces legible,
language straightforward, and complexity no higher than the question
requires.
