---
type: concept
title: Distinguish Actual from Forecast
description: >
  When actual and forecast share one time axis, mark uncertainty explicitly —
  solid versus dotted lines, lighter weight, region shading, and labels —
  rather than plotting one undifferentiated series that hides where fact
  ends and projection begins.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 6"
---

A common mistake is drawing actual and forecast as one continuous line of
equal weight. Viewers then cannot tell where history stops and projection
starts. Fix it with layered cues:

- **Line style and weight** — solid and thicker for actual; thinner dotted
  (or dashed) for forecast, leveraging the connotation that dots mean lower
  certainty.
- **Region cues** — light background shading and/or "ACTUAL" / "FORECAST"
  axis-region labels (often in all caps for scan) reinforce the split.
- **Markers and labels** — place markers only at annotated points so each
  callout binds to the right value; bold the last actual point as the anchor
  into the forecast; label forward-looking points when expectations must be
  precise, while historical magnitude can ride a muted y-axis.

Keep non-focal chrome in grey so the
[visual hierarchy](visual-hierarchy-with-preattentive-attributes.md) leads
title → annotation dates → corresponding points. Same-hue family for last
year vs. this year (or actual vs. goal) can preserve [similarity](gestalt-similarity.md)
ties without letting context series compete — a goal line may stay thin and
grey while still present for reference. Pair with
[action titles and annotation](action-titles-and-on-chart-annotation.md) so
the forecast story is stated in words, not only implied by the line break.
