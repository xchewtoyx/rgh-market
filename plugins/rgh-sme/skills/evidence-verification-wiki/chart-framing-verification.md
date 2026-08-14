---
type: concept
title: Chart Framing Verification
description: Checking whether a chart's scale, axis range, or aggregation choice (rather than the underlying data) is what produces its apparent trend.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7, 11"
---
# Chart Framing Verification

A chart can be built from entirely accurate data and still misrepresent the trend it depicts, purely through framing choices — axis scale, time window, or aggregation method. The most direct way to check a suspicious chart is to replot the same underlying data with a different, more honest framing.

## Common Framing Distortions
- **Inappropriate axis scale/range**: zooming out an axis (e.g., a temperature axis spanning many more degrees than the actual variation) can visually flatten a real trend into apparent noise. Redrawing the same data at an appropriate scale restores the visible trend.
- **Cumulative vs. periodic aggregation**: a cumulative running-total chart (e.g., total units sold to date) can only ever go up or stay flat by construction, regardless of whether the underlying period-over-period rate is actually rising, flat, or declining. Replotting the same data as period-by-period figures (e.g., quarterly instead of cumulative) can reveal a decline that the cumulative framing structurally cannot show.
- **Axis inversion**: flipping the usual direction of an axis (e.g., zero at the top instead of the bottom) makes a genuine increase visually read as a decrease, and vice versa, without altering a single data point. A design choice like this can be a deliberate, non-deceptive stylistic decision (evoking a downward-pointing "negative" association) rather than an attempt to mislead — apply [charitable interpretation](charitable-interpretation-in-review.md) before assuming intent, but flag the resulting misreading risk regardless of intent.
- **Time-window selection**: charting only a short, cherry-picked window can make a routine fluctuation look like a dramatic, unprecedented move; replotting the same series over a much longer window can reveal it as one of many similar dips or rises in a stable longer-term trend. This is [cherry-picking](cherry-picking.md) applied to the horizontal axis.
- **Uneven tick spacing**: using inconsistent intervals between axis labels (e.g., 30 years, then 10, then 9, then 1) visually compresses a long period of steep change into a small span while stretching a short recent period, creating an apparent trend reversal or plateau that disappears once the same data is replotted with constant-interval ticks.

## Verification Action
When a chart supports a document's central claim, check what aggregation and scale choices were used, and consider replotting the same underlying data with a neutral default (linear scale spanning just the relevant range; period-over-period rather than cumulative; constant tick spacing) before accepting the chart's apparent story. If the replotted version tells a materially different story, the original framing — not the data — was doing the persuasive work.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Cherry-Picking](cherry-picking.md)
- [Proportional Ink Principle](proportional-ink-principle.md)
- [Dual-Axis Manipulation Detection](dual-axis-manipulation-detection.md)
- [Evidence Quality Dimensions](evidence-quality-dimensions.md)
