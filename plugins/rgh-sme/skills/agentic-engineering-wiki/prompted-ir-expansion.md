---
type: concept
title: Prompted IR Expansion
description: >
  Expand compact intermediate expressions into flat outputs with a few-shot
  rewrite prompt when you lack — or prefer not to run — a dedicated executor.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 31–45"
---

[Least-to-most](least-to-most-prompting.md) pipelines often emit a compact
intermediate representation (e.g. SCAN’s Python-style `+` / `*` action
expressions) to save context. Expanding that IR to a flat sequence can be a
script **or** another LM prompt: few-shots that optionally `Rewrite` (fold
products) then emit enumerated actions. Zhou et al. report ~99.7% expansion
accuracy on 1000 random expressions under `code-davinci-002`, supporting
near-ceiling combined accuracy without a Python executor.

Use when IR is simple algebra over strings and executor sandboxing is costly;
prefer a real interpreter when IR can embed arbitrary code or when expansion
errors would silently poison [compositional mapping](compositional-mapping-exemplars.md)
results. Keep expand-stage prompts separate from decompose/solve contexts under
[domain-specific decomposition prompts](domain-specific-decomposition-prompts.md).
