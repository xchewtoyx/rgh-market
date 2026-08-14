---
type: concept
title: Order Categorical Values by Magnitude
description: >
  When a categorical axis has no inherent order, sort its bars/slices by
  value rather than leaving them in an arbitrary or alphabetical order.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.7, ch. 8 §8.3"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2, ch. 9"
---

Unordered categorical bars or slices (e.g., products, sales reps, regions)
should usually be ordered by size, unless some other order is more meaningful
to the audience (e.g., a fixed process sequence or natural age brackets).
There should always be **logic** in the order — an order that exists but is
invisible (e.g., sorted by a satisfaction sum while color pulls the eye to
"have not used") fails as badly as no order. Ordering by magnitude surfaces
information — who's biggest, where the gaps are, how skewed the distribution
is — instantly, that would otherwise require the viewer to scan and mentally
re-sort. Because audiences typically scan from the top first, put the most
important category (often largest or smallest, depending on the message) at
the top of a
[horizontal bar chart](horizontal-bars-for-categorical-labels.md) and order
the rest to support that story.

When telling several stories from one categorical set live, **fix one base
order** across slides and change only color/callouts — rearranging order
between views imposes a mental tax. Preserve intrinsic ordinal order (age
bands, Likert poles) rather than re-sorting by value; direct attention with
[emphasis and annotation](progressive-emphasis-across-slides.md) on top of
that fixed construct. This is also what makes a
[Pareto chart](pareto-chart.md) work at all: ranking by value first is a
precondition for its cumulative-total line to be meaningful.

The same technique applies to monitoring displays, not just static reports:
a telesales-supervisor dashboard ranked reps by performance with the worst
performers listed first, so the reps most needing attention were always at
the top of the list rather than buried in an alphabetical roster — combined
with a visual flag (e.g., a colored rectangle) marking whoever fell outside
the acceptable range. Ranking-by-severity is a cheap, general way to make a
"what needs my attention" list self-prioritizing.
