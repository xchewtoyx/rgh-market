---
type: concept
title: Binning-Induced Distortion
description: Grouping continuous data into bins can manufacture or hide an apparent trend, through uneven bin widths or through averaging away the underlying spread.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7"
---
# Binning-Induced Distortion

Grouping continuous data into discrete bins for a histogram or bar chart is a modeling choice, not a neutral default — the choice of bin boundaries and widths can change the visual story the same underlying data tells, and averaging within bins can conceal how much spread the raw data actually has.

## Variable-Width Bins
When bins of different widths are shown at the same visual size (e.g., adjacent bars for a $5-10k-wide income bracket and a $100k-wide bracket), bin *width* rather than the underlying data's true density can drive the apparent bar height — a bin that's simply wider will tend to capture more observations regardless of whether the underlying distribution has any real concentration there. Different bin-width choices applied to the exact same underlying dataset can be used to support entirely different, even contradictory, narratives about where a distribution's mass really sits.

## Averaging Within Bins Hides Spread
Binning continuous scatter data into intervals and plotting only each bin's average can make a genuinely weak or noisy relationship look like a strong, clean trend line, because the plot no longer shows how much the individual observations within each bin actually varied. The un-binned raw data can look far noisier (in the most extreme cases, indistinguishable from an unstructured scatter) even when the binned-average version of the identical data looks like a clear trend.

A related error compounds this: if the error bars shown on a binned-average chart represent the **standard deviation of the mean** (which shrinks as more points are averaged into a bin) rather than the **standard deviation of the individual observations**, the chart will visually understate how much the raw data actually varies within each bin, making the apparent trend look tighter and more reliable than the underlying data supports.

## Verification Action
When a draft cites a binned chart (histogram or a binned-average trend line) as evidence:
- Check whether all bins are the same width; if not, ask whether the visual comparison implicitly (and wrongly) treats bar height as reflecting density rather than width times density.
- Ask to see the un-binned, raw underlying data alongside any binned-average summary, particularly for a scatter relationship — a clean binned trend line can mask an underlying relationship that explains only a small fraction of the total variance.
- Check what error bars on a binned chart actually represent (spread of the mean vs. spread of the observations) before reading tight error bars as evidence of a reliable, low-variance relationship.

## See Also
- [Mean vs. Median Selection](mean-vs-median-selection.md)
- [Numeric Sanity Checking](numeric-sanity-checking.md)
