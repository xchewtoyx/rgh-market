---
type: concept
title: Spurious Correlation Detection
description: Recognizing correlations that arise from chance or shared trends rather than any real connection, especially when many series are compared at once.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 4"
---
# Spurious Correlation Detection

A **spurious correlation** is a statistical relationship with no real causal connection behind it, arising by chance. These are especially common when comparing time series that are simply both generally trending in the same (or opposite) direction over time: nearly any two increasing series will correlate positively over time, and any increasing-vs-decreasing pair will correlate negatively, with no underlying link required.

## Data Dredging
Spurious correlations become far more likely to *find* when many series are compared against each other systematically. With roughly 100 time series, pairwise comparison yields roughly 10,000 comparisons — virtually guaranteeing some will show a spuriously high correlation purely by chance. This is the same underlying mechanism as [p-hacking](cherry-picking.md): the more comparisons run, the more likely one clears a significance-looking threshold with no real relationship behind it.

## Verification Action
- Be especially skeptical of a correlation between two generally-trending time series with no independently plausible mechanism connecting them.
- If a correlation was found by searching across many candidate variables or time windows rather than testing one pre-specified hypothesis, treat it as a candidate for further investigation, not as established evidence — see [p-value misinterpretation](p-value-misinterpretation.md) for the related statistical-significance framing of this problem.
- A statistically significant correlation between two things with no plausible causal mechanism connecting them is grounds to suspect coincidence over a real effect, regardless of the strength of the correlation coefficient.

## See Also
- [Correlation vs. Causation](correlation-vs-causation.md)
- [Cherry-Picking](cherry-picking.md)
