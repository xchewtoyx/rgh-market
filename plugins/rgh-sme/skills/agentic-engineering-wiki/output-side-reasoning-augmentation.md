---
type: concept
title: Output-Side Reasoning Augmentation
description: >
  Improve hard tasks by eliciting intermediate tokens before the final answer —
  orthogonal to input-side tricks like instructions, few-shots, or soft prompts.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §7–§8; Appendix C"
---

Many prompting methods improve the **input**: instructions, soft/learned
prompts, few-shot exemplars, retrieval. [Chain-of-thought prompting](chain-of-thought-prompting.md)
instead augments the **output** with intermediate natural-language steps that
decompose multi-hop work *before* the final answer. Wei et al. place CoT as
orthogonal to input-side instruction tuning: you can combine both.

Do not confuse this with post-hoc natural-language explanations that justify an
already-chosen label — those target interpretability; CoT’s goal is sequential
decomposition (see
[natural-language intermediate reasoning](natural-language-intermediate-reasoning.md)).
Harnesses should version output-side cues (triggers, plan formats) separately
from input packs in the [prompt catalog](prompt-catalog.md), and still respect
[scale-dependent chain of thought](scale-dependent-chain-of-thought.md):
output-side reasoning is an emergent ability, not a free upgrade for tiny
models. Pair with [broad vs narrow prompting](broad-vs-narrow-prompting.md)
when choosing a single multi-task output cue vs per-task input templates.
Discovering more broad prompts — not only CoT triggers — is the intended
research direction beyond this baseline.
