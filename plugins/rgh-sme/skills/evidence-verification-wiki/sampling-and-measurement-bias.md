---
type: concept
title: Sampling and Measurement Bias
description: Checking how a number was actually produced — from a full count, a biased sample, a self-reported measurement, or an indirect model — before trusting its precision.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Sampling and Measurement Bias

Most quantitative claims are not exact counts — they are estimates, and how the estimate was produced determines how much it can be trusted. A reviewer should identify which of these production methods generated a cited number before accepting its apparent precision.

## Sources of Numeric Error
- **Sampling error**: a small sample can be misleading purely by chance (e.g., measuring the height of a handful of unusually tall people and generalizing to the population).
- **Measurement bias**: self-reported or self-collected measurements are systematically skewed in a predictable direction (e.g., self-reported height tends to be inflated, more so among shorter people).
- **Selection bias in sampling**: the population actually measured differs systematically from the population the claim is about (e.g., measuring average height only among people at a basketball court overstates the general population's average).
- **Indirect inference through models**: some quantities are never measured directly at all, only inferred through a model requiring calibration (e.g., a radar gun inferring speed via Doppler shift, or a population estimate derived from a mark-recapture-style method rather than a direct count). The number's accuracy is then bounded by the model's assumptions and calibration, not by direct observation.

## Verification Action
When a draft cites a number, ask: was this counted directly, sampled, self-reported, or inferred through a model? For anything other than a direct full count, check the sample size, the collection method, and whether the sampled or self-reporting population plausibly matches the population the claim is actually about.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Poll Methodology Assessment](poll-methodology-assessment.md)
