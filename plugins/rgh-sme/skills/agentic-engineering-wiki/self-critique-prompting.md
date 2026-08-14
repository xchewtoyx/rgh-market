---
type: concept
title: Self-Critique Prompting
description: >
  Ask the model to check its own output for errors before accepting it, as a
  lightweight reflection step inside a single generation or agent turn.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Self-critique (self-eval) prompting asks the model to verify its answer,
nudging critical thinking the way [chain of thought](chain-of-thought-prompting.md)
nudges stepwise reasoning. It is a prompt-only form of
[reflection and error correction](reflection-and-error-correction.md) — useful
when a full multi-module [Reflexion](reflexion.md) setup is unnecessary.

Like CoT, it costs tokens and latency. Use it when silent wrong answers are
costly and when you can still afford the extra generation; do not treat
self-declared correctness as proof the goal was met (see
[agent planning failure modes](agent-planning-failure-modes.md)).
