---
type: concept
title: Scale-Dependent Chain of Thought
description: >
  Useful chain-of-thought reasoning emerges only past a model-scale threshold
  and often hurts smaller models — do not extrapolate from tiny-model ablations.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), Appendix A.1; §5–§6"
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), Appendix E"
---

[Chain-of-thought prompting](chain-of-thought-prompting.md) is not a free
upgrade for every model. Wei et al. find successful CoT emerges only at
sufficient scale and cannot be predicted by extrapolating small-model curves;
below roughly ~10B parameters, CoT often **hurts** accuracy. Abstract symbol
manipulation on last-letter / coin-flip toys arises only around **~100B**
parameters — in-domain exemplars already encode the perfect procedure, yet
small models still fail to execute it. Preliminary PaLM
62B error categories (semantic misunderstanding, missing steps, hallucinations /
repetitions / symbol-mapping failures) all shrink substantially when scaling to
540B — success depends on several abilities arriving together (semantic
understanding, symbol mapping, staying on topic, arithmetic, faithfulness).
Kojima et al. replicate the pattern for
[zero-shot chain of thought](zero-shot-chain-of-thought.md): without CoT,
MultiArith/GSM8K rise slowly with scale; with Zero-shot-CoT, accuracy jumps
sharply only once Original GPT-3, InstructGPT, and PaLM are large — e.g. PaLM
GSM8K Zero-shot-CoT is ~2–10% at 8B/62B then **43% at 540B**, while sub-13B
open models stay near plain zero-shot (~1–3%). At large InstructGPT/davinci
scale the typical ordering is Zero-shot < Few-shot < Zero-shot-CoT <
Few-shot-CoT.

For harness design: treat CoT (and related
[self-consistency decoding](self-consistency-decoding.md) /
[Tree of Thoughts](tree-of-thoughts.md)) as a capability gated by
[LLM model selection criteria](llm-model-selection-criteria.md). Prototype
reasoning prompts on the class of model you will ship; a cheap small model that
“supports” step-by-step text may still amplify errors. Prefer
[when chain of thought helps](when-chain-of-thought-helps.md) as the deployment
gate, not “always enable CoT.” Measure
[CoT length generalization](cot-length-generalization.md) on longer-than-demo
cases before shipping short few-shots as covering production depth.
