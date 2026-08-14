---
type: concept
title: Zero-Shot Chain of Thought
description: >
  Elicit multi-step reasoning with a fixed trigger such as “Let’s think step by
  step,” without per-task few-shot reasoning exemplars.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §1–§3; Table 1–2"
---

Zero-shot-CoT (Kojima et al., 2022) is
[chain-of-thought prompting](chain-of-thought-prompting.md) that drops human-
written step-by-step exemplars and uses one **task-agnostic** reasoning trigger
(classically “Let’s think step by step”) across arithmetic, symbolic, and
commonsense tasks. Compared with Few-shot-CoT (Wei et al.), it trades per-task
exemplar engineering for a second LLM call under
[two-stage reasoning–answer extraction](two-stage-reasoning-answer-extraction.md).
It usually underperforms carefully crafted Few-shot-CoT but **beats standard
few-shot** (answer-only exemplars, even at 8-shot) and massively beats plain
zero-shot on MultiArith / GSM8K-class tasks when the model is large enough —
and on some tasks (e.g. AQUA-RAT with PaLM 540B) Zero-shot-CoT already matches
Few-shot-CoT before adding [self-consistency decoding](self-consistency-decoding.md).
Treat it as the **minimalist strongest zero-shot baseline** for difficult
multi-step system-2 tasks before investing in exemplar packs or finetuning
datasets — Kojima et al.’s closing claim for the method. See also
[zero-plus-few-shot CoT](zero-plus-few-shot-cot.md) when you already have
exemplars.

Few-shot-CoT degrades when exemplar question types mismatch the task; a single
fixed zero-shot template can still produce a much better scaling curve on
MultiArith / GSM8K-class benchmarks when the model is large enough (see
[scale-dependent chain of thought](scale-dependent-chain-of-thought.md)). Use
it when you want multi-hop reasoning without maintaining exemplar packs, then
measure against few-shot CoT with
[offline prompt evaluation](offline-prompt-evaluation.md) —
[when chain of thought helps](when-chain-of-thought-helps.md) still applies
(large multi-step / symbolic / logical gains; easy one-step arithmetic and some
commonsense metrics can be flat or regress even when traces look sensible).
Sweep the exact cue under
[reasoning trigger sensitivity](reasoning-trigger-sensitivity.md); do not assume
paraphrases are equal. When few-shot exemplars must come from another task, see
[cross-task few-shot CoT transfer](cross-task-few-shot-cot-transfer.md).
Prefer [broad vs narrow prompting](broad-vs-narrow-prompting.md) as the
default design question: one task-agnostic trigger vs per-task demos.
