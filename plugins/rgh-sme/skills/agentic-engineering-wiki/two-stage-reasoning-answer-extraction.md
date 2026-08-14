---
type: concept
title: Two-Stage Reasoning–Answer Extraction
description: >
  First prompt for a reasoning trace, then a second self-augmented prompt that
  appends an answer-format trigger and parses the final answer.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §3.1"
---

[Zero-shot chain of thought](zero-shot-chain-of-thought.md) is implemented as
two feedforward passes:

1. **Reasoning extraction** — wrap the question as `Q: … A: [trigger]` (e.g.
   “Let’s think step by step”) and generate a continuation reasoning trace
   (often greedy for reproducibility).
2. **Answer extraction** — concatenate the first prompt, the generated
   reasoning, and a **format trigger** tailored to the output type
   (“Therefore, the answer (arabic numerals) is …”, “among A through E …”),
   then generate and parse \(\hat{y}\).

Few-shot CoT often embeds the answer format in exemplars and needs only one
call; zero-shot CoT buys lower exemplar engineering cost at the price of two
model calls plus cleansing/parsing. In a harness, treat the second stage as an
explicit post-processing contract: keep format triggers versioned with the
[prompt catalog](prompt-catalog.md), run deterministic
[answer cleansing](answer-cleansing.md), and fail closed when parsing cannot
recover a canonical answer (same discipline as
[action format enforcement](action-format-enforcement.md) for tool turns).
Use stop sequences (e.g. `"Q:"`) when needed to prevent the model from
emitting another question–answer turn instead of finishing extraction.
