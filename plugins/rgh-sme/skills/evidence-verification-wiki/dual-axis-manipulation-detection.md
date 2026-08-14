---
type: concept
title: Dual-Axis Manipulation Detection
description: Independently rescaling two y-axes on the same chart can force two unrelated series to visually appear correlated, and a physically impossible axis range is a strong tell that this happened.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 7"
---
# Dual-Axis Manipulation Detection

A chart plotting two series against two independently-scaled y-axes can be made to visually imply a tight correlation between them, regardless of whether the underlying data actually supports one — because each axis's scale and offset are free parameters the chart designer chooses, not something dictated by the data itself.

## The Technique
Rescaling and offsetting a second y-axis so that its curve's peaks and valleys line up with the first series' peaks and valleys manufactures the visual appearance of correlation. Two related checks catch this:
- **Zero-baseline test**: rescale both axes so both include zero and reflect their natural range. If the visual "tight correlation" disappears or weakens substantially once both axes are placed on a natural scale, the original alignment was a scaling artifact, not a property of the data.
- **Physically impossible range as a smoking gun**: if forcing the second axis to align its curve with the first requires that axis to extend into a range that isn't physically possible for the quantity it represents (e.g., a negative value for a quantity that can't be negative), this is strong direct evidence the axis was manipulated specifically to force the visual match, rather than chosen for any principled reason. The same manipulation technique, applied to the same first series, can typically be used to make it "correlate" with several different unrelated second series in turn — a useful check to demonstrate the technique proves too much to be meaningful.

## Verification Action
When a draft cites a dual-axis chart as visual evidence of a relationship between two series, check the scale and offset chosen for each axis independently. Replot both axes starting from zero (or another natural reference point for the quantity) and see whether the apparent relationship survives; if either axis's range doesn't correspond to a value the underlying quantity could plausibly take, treat the chart as manipulated regardless of how compelling the visual alignment looks.

## See Also
- [Chart Framing Verification](chart-framing-verification.md)
- [Spurious Correlation Detection](spurious-correlation-detection.md)
