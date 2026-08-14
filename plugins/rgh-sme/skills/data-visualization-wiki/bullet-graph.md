---
type: concept
title: Bullet Graph
description: >
  A dense, colorblind-safe replacement for circular gauges/meters: one bar
  encoding a measure, a tick mark encoding a comparison target, and
  background intensity bands encoding qualitative range.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 6 §6.2.1"
---

Stephen Few's own invention (originally named "performance bar," released
free for vendors to implement), designed specifically to replace circular
gauges and meters, which waste space (a radial shape doesn't pack densely)
and often chase real-world realism at the expense of communication — Few's
example: an ambiguous thermometer gauge where it's unclear whether sales rise
as the mercury rises or falls, and why "bad" red sits at the top.

Structure: a single horizontal (or vertical) bar encoding the key measure
(length = value, so it must
[start its scale at zero](bar-graph-zero-baseline-rule.md)), a perpendicular
tick or line marking a comparative measure (e.g., target), and background
fill-color bands of varying **intensity** (not hue — see
[colorblind-safe color encoding](colorblind-safe-color-encoding.md)) encoding
qualitative ranges (bad/satisfactory/good), capped at 5 bands for
perceptibility (see [perceptual distinctness limits](perceptual-distinctness-limits.md)).
When the measure bar meets or exceeds the comparison tick, a cross shape
forms that's perceived preattentively — so a whole panel of bullet graphs can
be scanned for good/bad status almost instantly (see
[preattentive processing](preattentive-processing.md)).

Variants: multiple comparisons can be shown via distinct marker stroke
weights or shapes; splitting the bar into "actual so far" plus "projected to
period end" segments shows progress toward a future target. If the useful
data range doesn't span down to zero (e.g., all values cluster between
$150k-$300k), replace the bar with a plain symbol marker instead — trading
visual weight for scale detail; both are legitimate depending on need.

Few describes small, informal comparisons against radial gauges finding
bullet graphs superior in both efficiency and accuracy of perception while
using much less space — though he is explicit the sample size was too small
to be a rigorous claim.
