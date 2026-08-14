---
type: concept
title: Avoid 3-D Effects and Occlusion
description: >
  3-D styling on business graphs rarely encodes real data and often actively
  hides it, since objects in front occlude — completely hide — objects behind
  them.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 3 §3.7, ch. 6 §6.2.1.10, ch. 8 §8.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

3-D effects on bars, pies, or lines add no value when the depth dimension
encodes nothing — it's pure decoration competing with the data for attention
(see [data-ink ratio](data-ink-ratio.md)). But even when depth *is* used to
encode a real variable (e.g., quarters of the year on a fax-revenue chart), it
introduces **occlusion**: bars or slices can end up completely hidden behind
others, silently deleting data from the display. The same problem shows up in
3-D-style area/pie charts, where entire quarter or region values can be
hidden from view. Gradient or drop-shadow "3-D-ish" shading on ordinary 2-D
bars, lines, or pie slices is the same mistake in a milder form — decorative
weight with no informational payoff, sometimes bad enough to be called
chartjunk.

Beyond occlusion, 3-D skews perceived size (tilted pies make nearer slices
look larger) and can make software compute bar heights in non-obvious ways —
e.g., some tools set 3-D bar height via an invisible tangent plane to the
y-axis, so a value that should read against a gridline appears substantially
lower. Never use 3-D to plot a single dimension of data.

The conclusion is close to absolute: avoid 3-D graphs for typical business
data. The only careful exception is when an actual third data dimension is
being plotted — and even then, proceed with caution. 3-D scatter plots or
other techniques for squeezing more than two correlated variables into one
plot should also be avoided — they demand too much study for dashboard
viewing (see
[scatter plot for correlation](scatter-plot-for-correlation.md)).
