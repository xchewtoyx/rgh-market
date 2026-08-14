---
type: concept
title: Horizontal Bars for Categorical Labels
description: >
  Horizontal bar charts are the default for categorical comparisons with
  readable labels: category names run left-to-right in natural reading order
  and are seen before the data under a top-left-first scan.
sources:
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 2"
---

For categorical data, a **horizontal** bar chart is usually easier than a
vertical column chart when category names are long or numerous. Labels sit
to the left and read left-to-right as ordinary text; under the usual
top-left-first/"Z" scan, the name is processed before the bar, so the viewer
already knows what the length represents — unlike vertical bars, which force
eye travel between an axis of tilted labels and the columns.

Horizontal bars still obey the
[zero-baseline rule](bar-graph-zero-baseline-rule.md) and the
[nominal/ordinal → bars](categorical-scale-types-and-bar-vs-line-choice.md)
choice. They support single-, two-, or multi-series layouts; more series
still make insight harder, so use multi-series cautiously. Order categories
by [magnitude or message priority](order-categorical-values-by-magnitude.md)
— put the most important category at the top, since that is seen first.
Stacked horizontal bars (including 100%-stacked) inherit the same
[stacking tradeoffs](stacked-bar-chart-tradeoffs.md); 100%-stacked horizontals
work especially well for negative-to-positive scales such as Likert survey
items, because both ends share consistent outer baselines.
