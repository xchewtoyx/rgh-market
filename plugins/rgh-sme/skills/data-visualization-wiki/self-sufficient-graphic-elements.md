---
type: concept
title: A Standalone Graphic Must Be Self-Sufficient
description: >
  Unlike a dashboard tile that lives inside a persistent interactive
  interface, a standalone chart may be viewed, printed, or copied out of
  context, so its title, axis labels and units, legend, and data source must
  all be readable on the graphic itself.
sources:
  - title: The Craft of Research, Fifth Edition
    resource:
      "The Craft of Research, Fifth Edition (Booth, Colomb, Williams, Bizup,
      FitzGerald), ch. 13"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 5"
---

A dashboard tile can lean on context that surrounds it permanently on
screen — a page header naming the metric, a filter bar showing the selected
date range, a consistent color key established elsewhere on the same view. A
standalone graphic (a figure in a report, a chart pasted into a slide or
email, an image saved and reopened later) has no such surrounding context
guaranteed to travel with it. If a viewer sees only the image, everything
needed to read it correctly has to be present in the image.

That means five elements are load-bearing, not optional decoration:

- An **informative title** that states what the graphic shows — prefer an
  [action title](action-titles-and-on-chart-annotation.md) that states the
  finding or recommendation when the graphic is meant to persuade or decide,
  not a generic label like "Chart 3."
- **Axis labels with units** — a number without a unit is ambiguous (dollars?
  thousands of dollars? percent?), and this is where
  [customize numeric presentation to the audience](customize-numeric-presentation-to-audience.md)
  applies to labels, not just to the data values themselves.
- A **legend or key**, wherever the mapping from color/shape to category
  isn't otherwise explained — though prefer
  [direct labeling over a legend](direct-labeling-over-legends.md) whenever
  the graphic has room for it, since a standalone graphic's viewer can't
  hover for a tooltip to recover a forgotten mapping. **On-chart
  annotations** explaining peaks, events, or the intended conclusion belong
  here too when marks alone would leave the "so what" ambiguous.
- A **source citation** — where the data came from, so a reader can trace and
  verify the claim the graphic is making, and so the graphic doesn't
  implicitly claim more authority than its data supports.
- A **visual hierarchy among these elements**: the title and data should
  dominate; supporting elements (axis labels, legend, source line) should be
  present but visually recessive — muted, smaller, out of the way — the same
  "necessary but not competing for attention" treatment described in
  [data-ink ratio](data-ink-ratio.md) and
  [visual affordances](visual-affordances-for-charts.md).

Missing any of these doesn't just look incomplete — it silently shifts work
onto the viewer (to guess units, to remember what a color meant, to take the
data on faith without a traceable source) in exactly the way
[axis manipulation](axis-manipulation-antipatterns.md) and other integrity
failures do, even without any intent to mislead.
