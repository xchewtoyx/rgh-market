---
type: concept
title: Quantitative Encoding Accuracy Pitfalls
description: Several common chart choices — bar graphs with a non-zero baseline, pie charts, and area- or 3-D-encoded values — visually misrepresent the underlying ratios because humans can't accurately compare angles, 2-D areas, or occluded 3-D volumes the way they can compare aligned lengths, so a technically-correct chart can still communicate a false magnitude at a glance.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3"
---

Several widely-used chart choices systematically distort the magnitude a viewer perceives, independent of whether the underlying numbers are correct:

- **Bar graphs with a non-zero baseline.** A bar's length is supposed to represent its value directly; starting the axis above zero inflates the visual ratio between bars — a metric that's actually less than double another can visually read as four times larger. Bar graphs encoding a quantity should always start at zero.
- **Pie charts and other angle/area encodings.** Humans are poor at accurately comparing 2-D areas and angles, which is exactly what a pie chart or bubble-size chart asks the viewer to do — a slice that looks like 40% of a pie can actually be 13%, and a circle that's actually 9x another's area can read as only 3x larger because viewers instinctively compare diameter, not area. Prefer an aligned-length encoding (a bar) for anything where the actual ratio matters, and reserve pie charts for the rare case where only rough part-of-whole impressions matter (Few states he never recommends them at all).
- **3-D effects.** Depth that encodes nothing adds visual noise; depth that does encode a real variable still causes occlusion, hiding bars or slices behind others entirely — a normally-visible value can vanish from a 3-D chart because a nearer element blocks it.

The common thread for telemetry visualization: pick the encoding whose accurate reading matches how humans actually perceive that visual channel — aligned length (bar height, line position) is read accurately, area/angle/3-D-depth are not — rather than the encoding that looks most visually distinctive. This matters more for observability dashboards than for one-off reports, since a misleading encoding that's checked daily trains an on-call team to misjudge the same magnitude every time. See [heatmaps vs. percentiles for variance](heatmaps-vs-percentiles-for-variance.md) for a related case of choosing a visualization that matches what's actually being asked of the viewer, rather than the most familiar chart type.
