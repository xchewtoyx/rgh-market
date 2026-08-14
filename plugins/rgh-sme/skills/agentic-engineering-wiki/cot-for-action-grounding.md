---
type: concept
title: CoT for Action Grounding
description: >
  Use natural-language chain-of-thought to map instructions onto discrete
  action sequences when the hard part is choosing and ordering grounded steps.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §4"
---

Commonsense [chain-of-thought prompting](chain-of-thought-prompting.md) is not
only for math: linguistic intermediate steps help tasks that need physical or
social background knowledge. On SayCan-style benchmarks, CoT helps map a
natural-language instruction to a **discrete action sequence** — the same shape
as tool/plan selection in agents. Wei et al. report large PaLM 540B CoT gains
on StrategyQA, Sports Understanding, Date Understanding, and SayCan, while
**CSQA gains stay minimal** (prior-knowledge MC that may not need multi-step
decomposition).

Harness takeaway: prefer CoT (or
[forced reasoning before tools](forced-reasoning-before-tools.md) /
[plan-and-solve prompting](plan-and-solve-prompting.md)) when the failure mode
is multi-hop strategy or action ordering — not when the bottleneck is a single
fact lookup. Still validate plans with
[plan-validate-execute](plan-validate-execute.md) and
[world-model-augmented planning](world-model-augmented-planning.md); a CoT
action list is not an executable world model. Gate with
[when chain of thought helps](when-chain-of-thought-helps.md) and
[offline prompt evaluation](offline-prompt-evaluation.md).
