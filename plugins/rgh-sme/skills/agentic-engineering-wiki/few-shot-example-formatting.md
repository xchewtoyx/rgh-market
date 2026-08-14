---
type: concept
title: Few-Shot Example Formatting
description: >
  Present few-shot examples either explicitly labeled as examples, or folded
  in as previously solved tasks the model believes it already completed.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Two ways to present [in-context learning](in-context-learning.md) examples in
a prompt:

1. **Explicit examples** — label them as such: "In the following, when I
   encounter a question like 'Who was the first President of the United
   States?' I will give an answer like 'George Washington.'" Simple to write
   and unambiguous to the model about what it's looking at.
2. **Integrated as prior solved tasks** — fold examples into the document as
   if they were previously solved tasks, rather than labeled examples. This
   requires more careful formulation but lets the model leverage the
   examples more naturally, producing a smoother prompt. It's especially
   effective in ChatML or conversation-transcript settings: the model is made
   to believe it already solved earlier tasks in the demonstrated style,
   which encourages it to continue that successful approach into the current
   task rather than treating the examples as a separate, detached reference
   section.
