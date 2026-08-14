---
type: concept
title: Numeric Sanity Checking
description: Cross-checking a quantitative claim against context, common sense, and unit consistency before accepting it as verified.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 4"
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Numeric Sanity Checking

**Numeric sanity checking** is a fast first-pass filter applied to every quantitative claim before deeper verification: does the number make sense against known context, or is it implausible on its face?

## Checks to Run
- **Order-of-magnitude plausibility**: Compare a figure against a known reference point (e.g., a claim of "8 billion people bought a smartphone" against a world population of ~7.8 billion — the writer likely meant *million*, not *billion*). The same check applies to an aggregate rate computed from a pipeline, not just a one-off reported number: a suddenly implausible positive-label rate in a dataset is a cheap, coarse signal that an upstream data feed may have silently failed rather than that the underlying phenomenon actually changed — see [default-negative values masking missing signal](default-negative-masks-missing-signal.md).
- **Unit conversions**: Re-derive conversions independently, especially when the source material used a different unit system than the draft.
- **Internal arithmetic**: If a document itemizes values that should sum to a stated total (e.g., itemized prices vs. a claimed kit total), re-add them.
- **Exact vs. rounded figures**: Prefer the exact number over a rounded one; if a rounded figure is used, surface both the exact and rounded values to the author/editor so they can choose deliberately rather than by default.

## Named Distinction: Percentage vs. Percentage Points
A change from 50% to 60% is a **10-percentage-point** increase but a **20-percent** increase (relative to the starting value). These two framings are commonly and easily confused in drafts — a reviewer must check which one the source material actually supports before the claim is restated either way. The confusion runs in both directions: a small percentage-point drop (e.g., from 2% to 1%) can also be described, correctly, as a much larger-sounding 50% *relative* reduction — reporting only the point difference ("only 1 fewer person per 100") can make a genuinely large relative effect sound negligible, exactly as reporting only the relative figure can make a negligible absolute effect sound large (see [relative risk vs. absolute risk](relative-risk-vs-absolute-risk.md)).

## See Also
- [Relative Risk vs. Absolute Risk](relative-risk-vs-absolute-risk.md)
- [Fermi Estimation for Verification](fermi-estimation-for-verification.md)
- [Mean vs. Median Selection](mean-vs-median-selection.md)
- [Mathiness Detection](mathiness-detection.md)
- [Significant Digit Discipline](significant-digit-discipline.md) — a companion check specifically for whether a calculated figure's reported precision is actually justified by its least-precise input.
