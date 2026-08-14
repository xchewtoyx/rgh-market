---
type: concept
title: Axis Manipulation Antipatterns
description: >
  Beyond a non-zero bar baseline, an axis can mislead by being inverted, by
  cherry-picking the plotted time window, by spacing ticks unevenly, or by
  rescaling a second axis until an unrelated series appears to track the
  first.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 7"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

Beyond the [zero-baseline rule for bars](bar-graph-zero-baseline-rule.md) and
[proportional ink](proportional-ink-principle.md) generally, an axis has
several other ways to distort what a chart communicates:

- **Inverted axis.** Flipping which direction is "up" (e.g., zero at the top
  of a vertical axis) can make an increase visually read as a decrease. A
  real case: a homicide-count graphic with zero at the top made a post-law
  increase in deaths look like a decline. This can happen without any intent
  to deceive — an inverted axis is sometimes chosen for a thematic effect
  (e.g., to evoke a downward, negative feeling for "bad" data) — but a
  reader scanning quickly reads direction as a preattentive cue for
  [Gestalt](gestalt-continuity.md)-style trend perception, and an inverted
  axis breaks that reading. Always default to the conventional direction
  (up/right = more) unless there is a specific, clearly-labeled reason not
  to.
- **Cherry-picked time window.** Plotting only a narrow recent window (e.g.,
  four days of a stock price) can make an ordinary dip look catastrophic;
  the same data plotted over years can reveal it as one of many routine
  fluctuations inside a long-run trend. Choose the window that reflects the
  actual claim being made, not the window that produces the most dramatic
  shape.
- **Uneven tick spacing on a time axis.** Using irregular intervals (e.g.,
  30 years, then 10, then 9, then 1) compresses a long period of steep
  change into a small visual space while an actually-flat recent period gets
  stretched out — manufacturing the visual impression of a "plateau" that
  disappears once tick spacing is made constant.
- **Fabricated dual-axis correlation.** [Combining two series on left/right
  axes](support-meaningful-comparisons.md) is legitimate when both include a
  meaningful zero and the goal is genuinely comparing two differently-scaled
  series. It becomes deceptive when one axis is deliberately rescaled and
  offset — sometimes to a physically impossible range — purely to force the
  second curve's peaks to visually line up with the first's, implying a
  correlation the underlying numbers don't support. A telltale sign of this
  manipulation: an axis range that includes physically impossible values
  (e.g., a negative quantity of a substance that cannot be negative).

The general defense against all of these: check what happens to the chart's
apparent message if the axis is rescaled to a natural range (zero-based
where applicable, evenly spaced, and spanning a representative time window).
If the story changes, the original axis choice was doing the persuading, not
the data.

An honest axis is necessary but not sufficient — see
[a standalone graphic must be self-sufficient](self-sufficient-graphic-elements.md)
for the other elements (title, units, legend, source) a graphic needs to
avoid misleading or under-informing a viewer even once the axis itself is
honest.
