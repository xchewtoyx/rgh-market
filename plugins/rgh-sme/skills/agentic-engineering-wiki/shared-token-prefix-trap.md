---
type: concept
title: Shared Token Prefix Trap
description: >
  Classification labels that share a starting token have their probabilities
  compound at that token, which can make a worse option outrank a better one.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

When using an LLM for classification — choosing one of a fixed set of
predefined categories — a subtle trap emerges from how tokenization
interacts with [logprobs](logprobs-fundamentals.md): if multiple candidate
labels share a starting token, their probabilities compound at that shared
token and can beat a genuinely more probable single option.

Example (real probabilities from a classification prompt over three
candidate regions — North America, Northeast Asia, Europe): "North America"
and "Northeast Asia" both start with the token "North." Their combined
probability mass at that shared first token beats Europe's standalone 44%,
even though Europe alone (44%) actually beats Northeast Asia alone (55% × 76%
= 42%) once you multiply out the full label's probability. The model's
apparent top suggestion, Northeast Asia, is therefore one the model itself
internally considers suboptimal to Europe — the shared prefix hid this by
inflating "North"-starting options as a group during token-by-token
selection.

The fix is straightforward: ensure every candidate label starts with a
unique token, so no two options can compound at a shared prefix. Combine this
with a [recognizable completion boundary](recognizable-completion-boundaries.md)
like a fixed answer format ("Please answer in the format: 1. [negative |
positive | neutral], 2. [explanation]") so the classification choice is both
unambiguous and safe from this compounding effect.
