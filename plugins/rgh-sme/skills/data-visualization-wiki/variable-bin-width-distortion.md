---
type: concept
title: Variable Bin Width Distorts Bar and Histogram Comparisons
description: >
  When bars represent counts grouped into ranges, unequal bin widths let bin
  width itself — not the underlying density of the data — drive apparent bar
  height, which can manufacture a visual pattern that isn't really there.
sources:
  - title: Calling Bullshit
    resource: "Calling Bullshit: The Art of Skepticism in a Data-Driven World (Carl T. Bergstrom, Jevin D. West), ch. 7"
---

A histogram or binned bar chart groups continuous data into ranges; each
bar's height should reflect the density of observations, but if the ranges
(bins) aren't equal width, height is confounded with bin width. A real
example: an income-distribution chart used bins as narrow as $5-10k at some
points and as wide as $100k elsewhere, so the widest bins collected far more
observations by virtue of their width alone — producing an artificial "hump"
in the middle of the distribution that supported a particular political
argument. The same underlying data, rebinned differently, can be made to
support entirely different conclusions.

A related distortion: averaging data within bins and plotting only the
per-bin averages can make a weak relationship look like a strong trend,
because binning hides the spread of the raw observations. A genetics/
educational-attainment scatter plot binned into 10 groups and averaged
looked like a strong linear trend; the un-binned raw data looked like a
diffuse cloud with the trend explaining under 10% of the variance. Where the
spread within a category matters, show it — see
[box plot](box-plot.md) — rather than collapsing it into a single per-bin
point.

Defense: check whether bins are equal width, and if summary points (means)
are being shown, ask whether the underlying spread would change the visual
impression of how strong the pattern really is.
