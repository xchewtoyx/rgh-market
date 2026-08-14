---
type: concept
title: Shortcut Learning Verification
description: Checking whether a model's high measured performance comes from a spurious artifact in its training data rather than the capability actually being claimed.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8"
---
# Shortcut Learning Verification

A model can score well on its evaluation metric while having learned to key on a **spurious artifact** correlated with the label in the training data, rather than the underlying feature the claim attributes its performance to. High aggregate accuracy is not evidence that a model is measuring what it's claimed to measure.

## Worked Examples
- **Husky vs. wolf classifier**: a well-performing image classifier turned out, under post-hoc feature attribution, to be keying almost entirely on *snow in the background* rather than any feature of the animal — because wolf photos in the training set happened to be shot in snowy settings.
- **Pneumonia X-ray classifier**: performed well at its training hospital but poorly elsewhere, because it had learned to key on the word "PORTABLE" printed on images from portable X-ray machines — used preferentially for the sickest, bedridden patients at that hospital. This was a hospital-specific correlate of illness severity with no clinical meaning, and did not transfer to hospitals using different equipment conventions.

Both cases are a training-data-side [confounding variable](confounding-variables.md): a factor (snow, imaging-equipment type) coincidentally correlated with the label in the specific training set, which the model exploited instead of the causally relevant signal.

## Verification Action
When a draft cites a model's strong performance as evidence it has learned a specific capability:
- Check whether the paper or claim reports any post-hoc interpretability analysis (feature attribution, saliency, ablation) confirming the model relies on the claimed signal rather than an incidental correlate of the label.
- Be specifically skeptical of performance that doesn't transfer: a model reported to perform well only in the setting it was trained in, but untested or poor elsewhere, is a red flag for shortcut learning.
- Ask what else in the training images/data was systematically different between classes besides the feature the claim is about (background, equipment, formatting, source institution) — see [training data provenance check](training-data-provenance-check.md).

## See Also
- [Confounding Variables](confounding-variables.md)
- [Training Data Provenance Check](training-data-provenance-check.md)
- [Benchmark Claim Verification](benchmark-claim-verification.md)
