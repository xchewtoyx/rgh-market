---
type: concept
title: Fine-Tuning Approach Comparison
description: >
  Full fine-tuning, LoRA, and soft prompting trade training-document volume
  and duration against how much genuinely new behavior they can teach.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

Once a [fine-tuning decision](fine-tuning-decision.md) is made, three
approaches differ in how much they can teach and how much data and time they
need:

- **Full fine-tuning / continued pre-training** — every parameter is
  adjusted by continuing the training process on new documents; think of it
  less like explaining a concept to a human and more like a riverbed
  forming — pouring thousands of documents over the model slowly carves a
  new groove. This is the only approach that can teach genuinely new facts
  and whole new domains, not just style, but it needs tens of thousands of
  training documents and weeks to months of training time.
- **LoRA (low-rank adaptation)** — a parameter-efficient technique: freeze
  most parameters and train a small, low-rank "diff" matrix added to a few
  key parameter matrices. Diffs are small and shareable across machines, so
  one deployment can serve multiple diffs on the same underlying model, and
  training takes hours to a few days rather than weeks. The tradeoff is that
  LoRA is limited by its rank (its degrees of freedom) in how much it can
  learn: it doesn't teach genuinely new tricks so much as teach the model
  *which* of its existing tricks to expect to use and how — what to attend to
  in the prompt, how to interpret it, what's expected in the completion.
  Format and style are easily LoRA-learnable, and hundreds to thousands of
  documents is enough. LoRA is also good at shifting the model's general
  prior distribution for a domain — a travel-recommendation app serving
  mostly European customers can skew toward European suggestions either by
  adding "customer is European" to the prompt, or by fine-tuning on telemetry
  that captures unstated preferences too (e.g. thumbs-down on distant
  destinations, purchases clustering after budget-friendly suggestions) —
  LoRA can condition on a distribution shift whether or not the driving
  factor was ever consciously identified.
- **Soft prompting** — goes further than crafting words to put the model into
  the right "state of mind": instead, give a few dozen example outputs and
  use machine learning to find a model state that most likely produces them,
  needing only hundreds of documents and hours of training. Availability
  depends on the model framework; many providers don't support it.

Both full fine-tuning and LoRA typically let you drop static prompt context
(general explanations and instructions) and [few-shot examples](few-shot-example-formatting.md)
from the prompt entirely, since those lessons get baked into the model's
parameters more durably than presenting them in-prompt on every call. In this
sense, **fine-tuning is a continuation of prompt engineering by other means**
— trading per-call prompt tokens for a one-time training cost.
