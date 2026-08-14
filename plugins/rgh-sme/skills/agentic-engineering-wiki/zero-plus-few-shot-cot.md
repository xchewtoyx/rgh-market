---
type: concept
title: Zero-Plus-Few-Shot CoT
description: >
  Insert a zero-shot reasoning trigger into few-shot CoT exemplars so each demo
  still shows steps but also cues the model with the task-agnostic phrase.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §3 Table 2"
---

**Zero-Plus-Few-Shot-CoT** mixes [zero-shot chain of thought](zero-shot-chain-of-thought.md)
with Wei-style few-shot CoT: keep ⟨question, reasoning, answer⟩ exemplars, but
insert the reasoning trigger (e.g. “Let’s think step by step”) into those
demonstrations (and typically into the query). On MultiArith / GSM8K with
InstructGPT / PaLM-class models, Kojima et al. report this hybrid above
plain Few-shot-CoT and above Zero-shot-CoT alone.

Harness use: when you already maintain exemplar packs, try adding the same
trigger used for zero-shot CoT rather than treating the two as mutually
exclusive. Still gate with [when chain of thought helps](when-chain-of-thought-helps.md)
and [offline prompt evaluation](offline-prompt-evaluation.md); stacking
trigger + exemplars + [self-consistency decoding](self-consistency-decoding.md)
multiplies cost. Prefer this before inventing new exemplar content when the
gap is “forgot to reason” rather than “wrong domain demos” —
[cross-task few-shot CoT transfer](cross-task-few-shot-cot-transfer.md).
