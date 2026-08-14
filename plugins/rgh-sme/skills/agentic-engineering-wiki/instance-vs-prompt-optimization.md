---
type: concept
title: Instance vs Prompt Optimization
description: >
  Optimize one test-time solution for a single query, or optimize a prompt that
  must generalize across many queries — different variables, same feedback loop.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), ch. 2"
---

TextGrad-style [textual gradient descent](textual-gradient-descent.md) supports
two harness patterns:

1. **Instance optimization** — the variable is a single solution (answer, code
   patch, plan, domain artifact) refined at test time for that query. Closest
   kin to
   [reflection and error correction](reflection-and-error-correction.md) /
   [Reflexion](reflexion.md), but driven by graph-local
   [textual gradients](textual-gradients.md) rather than only episodic memory.
   See [test-time solution refinement](test-time-solution-refinement.md) for
   the self-supervised LLM-loss pattern (e.g. GPQA/MMLU gains) and
   [test-time code refinement](test-time-code-refinement.md) when local tests
   exist. Domain simulators (molecules, treatment plans) can be loss edges
   too — use **multi-metric** objectives when no single score suffices, and
   treat in-silico wins as provisional under
   [compound AI system optimization](compound-ai-system-optimization.md).
2. **Prompt optimization** — the variable is a prompt (often a system
   instruction) trained on a small set so it generalizes to new queries —
   [instruction vs demonstration optimization](instruction-vs-demonstration-optimization.md)
   and [strong-to-weak prompt optimization](strong-to-weak-prompt-optimization.md).

Do not confuse them in the harness: instance updates are per-episode and must
not silently rewrite shared templates; prompt updates are offline artifacts
that need validation suites before becoming the default
[system prompt architecture](system-prompt-architecture.md).
