---
type: concept
title: Precision vs. Accuracy in Measurement
description: A measurement can be highly reproducible yet systematically wrong (precise but inaccurate), or noisy yet correct on average (accurate but imprecise) — and a reviewer should identify which kind of error, if any, a cited figure carries before trusting it.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 8"
---
# Precision vs. Accuracy in Measurement

Two distinct kinds of measurement error exist, and a single number can suffer from either, both, or neither:
- **Systemic error (bias)**: a consistent, predictable-direction error — e.g., sales staff routinely overestimating next-quarter revenue by a stable margin.
- **Random error**: unpredictable on any single observation, but following quantifiable probabilistic patterns in aggregate (averaging out over repeated measurements).

**Accuracy** means low systemic error (not consistently over- or under-shooting); **precision** means low random error (highly reproducible results, even if consistently wrong). A bathroom scale rigged to always read 8 lbs high is *precise* (consistent) but *inaccurate*; a correctly calibrated scale used on unstable ground gives inconsistent single readings (*imprecise*) but averages to the true weight over many readings (*accurate*). The two properties are independent — checking one does not tell you about the other.

## Why This Distinction Changes What "More Data" Fixes
Random error shrinks as more independent observations are averaged together — a well-known, quantifiable improvement. Systemic error does **not** shrink with more data, no matter how large the sample, because every additional observation carries the same bias. A large sample with unknown or unaddressed systemic bias does not become more trustworthy just by being large.

## A Smaller Random Sample Can Beat a Much Larger Biased One
The Kinsey sex-behavior studies (1940s-50s) interviewed roughly 18,000 people, but through non-random, referral-based sampling (whole bowling leagues, fraternities, and clubs recruited as a block), leaving unknown, unquantifiable systemic bias. A reviewing statistician's assessment: a genuinely random sample of just a few hundred, or even a few dozen, would have produced more trustworthy results than Kinsey's much larger but badly-sampled 18,000, because only the random sample's error is actually quantifiable and bounded — the large non-random sample's true error direction and size remain unknown regardless of its size. The common intuition that a bigger dataset is automatically more trustworthy than a smaller one conflates volume with quality of sampling.

## Verification Action
When a draft cites a number as reliable primarily because it comes from a large or exhaustive dataset, check how that dataset was actually assembled. A large sample collected through a non-random or self-selected process (referral sampling, opt-in surveys, whatever data happened to already exist) carries systemic bias that its size does not fix — see [sampling and measurement bias](sampling-and-measurement-bias.md). Conversely, don't dismiss a small but genuinely randomly-sampled figure as inherently less trustworthy than a much larger non-random one; ask which one has *quantifiable* error, not which one has more raw data points. When only measuring *change over time* rather than an absolute level, note that a stable, unknown systemic bias can sometimes be tolerated because it partially cancels between the two time points being compared.

## See Also
- [Sampling and Measurement Bias](sampling-and-measurement-bias.md)
- [Selection Bias](selection-bias.md)
- [Measurement as Uncertainty Reduction](measurement-as-uncertainty-reduction.md)
