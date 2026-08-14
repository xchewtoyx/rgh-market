---
type: concept
title: Broad vs Narrow Prompting
description: >
  Prefer task-agnostic prompts that elicit broad reasoning skills when you need
  one template across tasks; reserve narrow per-task templates for format-heavy
  niches.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §5"
---

Most prompts are **narrow**: few-shot by construction, or zero-shot templates
engineered per task. They elicit task-specific skills. **Broad** prompts are
multi-task cues that aim at a cognitive ability rather than a dataset —
[zero-shot chain of thought](zero-shot-chain-of-thought.md)’s fixed “Let’s
think step by step” is the canonical example for system-2 / multi-hop
reasoning.

Harness guidance: start with a broad reasoning trigger (and measure under
[reasoning trigger sensitivity](reasoning-trigger-sensitivity.md)) before
authoring per-task exemplar packs. Broad prompts are orthogonal to instruction
tuning — they still help InstructGPT, vanilla GPT-3, and PaLM-class models —
so do not assume chat-tuned models make CoT triggers redundant. Keep narrow
prompts when answer **format** or domain demos are the bottleneck
([cross-task few-shot CoT transfer](cross-task-few-shot-cot-transfer.md);
[when chain of thought helps](when-chain-of-thought-helps.md)). Version both
kinds in the [prompt catalog](prompt-catalog.md).
