---
type: concept
title: When Chain of Thought Helps
description: >
  Prefer CoT for hard multi-step tasks on large models with flat baseline
  scaling; skip it when the task is already easy or the model is too small.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), Appendix A.3–A.4"
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §3 Table 1"
---

In principle [chain-of-thought prompting](chain-of-thought-prompting.md) applies
to any text-to-text task, but Wei et al. report the largest gains when three
conditions hold: (1) challenging multi-step reasoning, (2) a large language
model, and (3) a relatively flat baseline scaling curve. Benefits shrink when
any condition fails — e.g. easy MAWPS subsets already ≥90% with standard
prompting show little CoT lift, while PaLM 540B on GSM8K shows large gains.
Kojima et al.’s zero-shot table matches that gate: large lifts on harder
arithmetic (MultiArith, GSM8K, AQUA, SVAMP), symbolic (last letter, coin flip),
and BIG-bench logical tasks; near-parity on easy SingleEq / AddSub; mixed
commonsense metrics (StrategyQA up, CommonsenseQA flat/down) even when many
traces look coherent — prefer CoT for multi-hop strategy and
[action grounding](cot-for-action-grounding.md), not single-hop prior-knowledge
MC.
Treat standard prompting as a **lower bound** on what the checkpoint can do:
where baseline scaling is flat, CoT can unlock a larger solvable-task set
(arithmetic, commonsense, and OOD symbolic length) without finetuning.

Equation-only prompts can help short arithmetic sets but fail when the question
is too semantically hard to map to one equation; natural-language CoT can walk
clause by clause where equation templates mis-parse. Wei et al.’s arithmetic
ablations sharpen this: padding tokens or putting reasoning *after* the answer
also fails — see
[natural-language intermediate reasoning](natural-language-intermediate-reasoning.md).
Combine this gate with
[scale-dependent chain of thought](scale-dependent-chain-of-thought.md): if the
deployed model is below the emergence threshold, CoT may regress. Check
[CoT length generalization](cot-length-generalization.md) when demos are shorter
than production depth, and do not equate answer accuracy with
[CoT path correctness](cot-path-correctness-gap.md). Measure with
[offline prompt evaluation](offline-prompt-evaluation.md) on your task suite
before making CoT the default path in the harness.
