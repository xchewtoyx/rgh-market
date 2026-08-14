---
type: concept
title: Bar Graph Zero-Baseline Rule
description: >
  A bar's length is read as directly proportional to its value, so a bar
  graph's quantitative axis must start at zero or it creates a visually false
  ratio between values.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.8, ch. 6 §6.2.1"
  - title: Data Science from Scratch, 2nd Edition
    resource: "Data Science from Scratch, 2nd Edition (Joel Grus), ch. 3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

If a bar graph's vertical axis starts at, say, $500,000 instead of $0, two
bars whose true values differ by less than 2x can visually appear to differ
by 4x or more, because a bar's *length* — not the number printed at its tip —
is what viewers perceive as the value. A concrete case: two bars showing 500
and 505 (a 1% change) with the vertical axis starting at 499 instead of 0
looks like a dramatic increase; the same data with a zero baseline looks
unremarkable. Another public example: a tax-rate move from 35% to 39.6%
(about a 13% relative increase) plotted with a y-axis starting at 34 visually
implied a ~460% jump. Bar graphs must always start their quantitative scale
at zero; anything else is a graphical-integrity violation, not a stylistic
choice. Deliberately truncating a scale to reinforce a point is unethical and
also self-defeating — one discerning viewer who notices can destroy the
argument's credibility.

This is the bar-specific case of the general [proportional ink
principle](proportional-ink-principle.md): whenever ink (filled area or
length) represents a value, that ink must be proportional to the value.
This rule is specific to bars because length is the encoding. It does **not**
apply to [line graphs](line-chart-for-trend-shape.md), whose job is to show
the *shape* of change over time rather than absolute magnitude via a filled
length — a line graph's scale can be narrowed to just above/below the actual
data range to show more shape detail. Even then, flag a non-zero line baseline
clearly and use it cautiously so minor changes are not oversold. The same
zero-start requirement applies to the [bullet graph](bullet-graph.md)'s bar;
when the useful data range doesn't span down to zero, replace the bar with a
plain symbol marker instead of stretching or truncating the bar.

When exact values matter more than trend shape, prefer
[direct data labels](direct-labeling-over-legends.md) and mute or drop a
redundant axis; when big-picture comparison matters, keep a greyed axis and
skip labeling every bar.
