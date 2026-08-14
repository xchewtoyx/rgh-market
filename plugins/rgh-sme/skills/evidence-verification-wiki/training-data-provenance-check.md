---
type: concept
title: Training Data Provenance Check
description: Verifying a claim about a machine-learning system's output by scrutinizing the data it was trained on, rather than needing to understand its internal algorithm.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8"
---
# Training Data Provenance Check

A reviewer does not need to understand a machine-learning algorithm's internals to verify a claim about what it does — the far more tractable target is the **training data**: where it came from, who labeled it, and how representative it is of the population the claim is actually about. This follows the classic "garbage in, garbage out" (GIGO) principle: a model's output can only be as trustworthy as the data it learned from, regardless of how sophisticated the learning method is.

## Verification Action
When a draft cites a claim about what a machine-learning system found, predicts, or detects:
- Ask where the training data came from and who or what produced the labels — a system trained on data from one narrow, self-selected population (e.g., dating-site photos, one hospital's patients) supports claims about that population, not a general one; see [sampling and measurement bias](sampling-and-measurement-bias.md).
- Treat the training data's provenance as the primary object of scrutiny before the algorithm's design — interrogating data collection and labeling is tractable for a non-specialist reviewer in a way that auditing model internals is not.
- Separately verify the **output claim** itself against independent evidence — a well-sourced training set does not guarantee the paper's downstream causal or explanatory claims about *why* the model performs as it does; see [shortcut learning verification](shortcut-learning-verification.md) for a common way that gap shows up.

## See Also
- [Sampling and Measurement Bias](sampling-and-measurement-bias.md)
- [Shortcut Learning Verification](shortcut-learning-verification.md)
- [Fabrication Detection](fabrication-detection.md)
- [Black-Box Claim Verification](black-box-claim-verification.md)
