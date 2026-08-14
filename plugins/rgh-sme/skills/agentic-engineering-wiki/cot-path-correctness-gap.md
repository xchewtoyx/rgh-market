---
type: concept
title: CoT Path Correctness Gap
description: >
  A correct final answer does not imply a correct reasoning path — treat CoT
  traces as debugging evidence, not as verified proofs of intermediate steps.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §6"
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), Appendix C.1"
---

[Chain-of-thought prompting](chain-of-thought-prompting.md) yields readable
intermediate steps, but Wei et al. emphasize there is **no guarantee** those
paths are correct even when the final answer matches gold. Paths can support
right or wrong answers; factual faithfulness of generations remains an open
problem. Kojima et al.’s CommonsenseQA sample study makes this concrete: among
**correct** predictions, ~22% still had incorrect CoT (often failing to narrow
to one choice while the first listed option matched gold). Wei et al. note
accidental correct finals are rarer in free-response math than in
multiple-choice / binary settings — choose eval formats carefully when auditing
faithfulness. Among incorrects, traces can be logically coherent yet miss
common-sense priors — see [CoT failure modes](cot-failure-modes.md).

For harness design, do not equate answer accuracy with verified
reasoning — especially when using CoT traces as audit artifacts or as feedback
into [reflection and error correction](reflection-and-error-correction.md) /
[self-critique prompting](self-critique-prompting.md).

Prefer independent oracles ([gold-standard matching](gold-standard-matching.md),
[functional completion testing](functional-completion-testing.md), unit tests)
over trusting the monologue. When intermediate steps must be reliable (agent
plans, tool arguments), add explicit validation —
[plan-validate-execute](plan-validate-execute.md),
[action format enforcement](action-format-enforcement.md) — rather than assuming
CoT self-explains correctly. [Self-consistency decoding](self-consistency-decoding.md)
can reduce reliance on any single path without proving faithfulness.
