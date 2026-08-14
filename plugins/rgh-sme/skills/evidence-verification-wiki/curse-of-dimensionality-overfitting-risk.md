---
type: concept
title: Curse of Dimensionality Overfitting Risk
description: A model built from many candidate predictor variables can fit a training dataset by chance alone, which requires exponentially more data to rule out as the variable count grows.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8"
---
# Curse of Dimensionality Overfitting Risk

Adding more predictor variables to a model requires exponentially more data to reliably distinguish genuine predictive signal from chance alignment. With enough candidate variables, some combination of them will fit almost any dataset by luck alone — a fit that carries no predictive power going forward.

## Worked Example
A three-month stretch of the New York Yankees' win-loss record can be shown to "predict" the Dow Jones Industrial Average over the same period — a purely coincidental, non-replicable alignment, illustrating that with enough candidate variables in play, spurious fits of this kind are the expected outcome rather than a surprising anomaly.

## Verification Action
When a draft cites a model's strong fit to historical or training data as evidence of real predictive power:
- Check how many candidate predictor variables the model considered relative to its sample size — a model built from dozens or hundreds of candidate variables on a comparatively small dataset is at elevated risk of having fit chance alignment rather than durable structure, however good the reported in-sample fit looks.
- Look for evidence the model was validated on data independent of the data used to select and fit its variables, not just re-checked against the same data it was built from.
- This is the same underlying mechanism as [spurious correlation detection](spurious-correlation-detection.md)'s data-dredging problem, applied to model-building with many variables rather than pairwise time-series comparison — the more variables or comparisons in play, the more likely one clears a significance-looking threshold by chance.

## See Also
- [Spurious Correlation Detection](spurious-correlation-detection.md)
- [Predictive Model Generalization Check](predictive-model-generalization-check.md)
