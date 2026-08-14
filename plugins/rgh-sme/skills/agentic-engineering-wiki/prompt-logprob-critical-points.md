---
type: concept
title: Prompt Logprob Critical Points
description: >
  Echo prompt-token logprobs to flag anomalies (typos, odd spans) and
  high-information passages — thresholds must tolerate model and position drift.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

With APIs that support `echo`, you can retrieve logprobs for **prompt** tokens
without requesting a completion. Abnormally low values mark surprising input
(typos that split tokens oddly, genre breaks) and can highlight denser passages
for user or agent attention under
[context engineering](context-engineering.md).

Heuristics: single-digit negative logprobs are common; double-digit negatives
often mean something genuinely odd — but there is **no fixed threshold**.
Values vary by model, genre, and position (often lower near the start before
topic/style settle). Floating-point deployment noise can swing readings by
roughly ±1, so unit tests must tolerate jitter or mock the model. Treat this as
a diagnostic for prompt/input quality next to
[logprob completion quality signals](logprob-completion-quality-signal.md), not
as a standalone correctness oracle.
