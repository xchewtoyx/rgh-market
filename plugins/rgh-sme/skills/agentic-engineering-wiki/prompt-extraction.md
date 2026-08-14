---
type: concept
title: Prompt Extraction
description: >
  Attacks that trick a model into revealing its system prompt or privileged
  context so an application can be replicated or exploited.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Functioning prompts are valuable and often treated as proprietary, which fuels
reverse prompt engineering: deduce the system prompt by analyzing outputs or by
instructing the model to ignore prior instructions and repeat them. Apparent
leaks are frequently **hallucinated**, which makes verification hard. Context
beyond the system prompt can also leak (for example a user location the model
was told not to reveal).

Practical stance for [defensive prompt engineering](defensive-prompt-engineering.md):
write the [system prompt](system-prompt-architecture.md) assuming it will one day
become public. Secrecy is a weak moat — prompts need ongoing maintenance as
models change ([prompt catalog](prompt-catalog.md)) — and extraction risk is
better mitigated by reducing the value of a leaked prompt (no secrets in the
prompt text) than by hoping it stays hidden.
