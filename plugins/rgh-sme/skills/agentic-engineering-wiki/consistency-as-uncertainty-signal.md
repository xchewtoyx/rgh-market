---
type: concept
title: Consistency as Uncertainty Signal
description: >
  Use the fraction of sampled paths that agree with the majority answer as a
  cheap calibration cue — low agreement means the model may not know.
sources:
  - title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    resource: "Self-Consistency (Wang et al.), pp. 1–24"
---

When running [self-consistency decoding](self-consistency-decoding.md), the
**agreement rate** — share of samples whose final answer matches the
aggregated choice — correlates with accuracy. Low consistency is a harness-
usable “knows when it doesn’t know” signal without a trained calibrator:
abstain, escalate to tools/[RAG](retrieval-augmented-generation.md), fall back
to another mode (for example
[internal–external knowledge routing](internal-external-knowledge-routing.md)),
or spend more samples only when agreement is weak.

This is distinct from log-prob ranking of a single path: majority agreement
across *diverse* rationales is the feature. Treat generated rationales as
inspectable but potentially non-factual — useful for debugging biases, not as
ground truth without further grounding.
