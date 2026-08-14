---
type: concept
title: External Calculator for CoT
description: >
  Post-process equations inside a chain of thought with a deterministic
  calculator so correct plans are not failed by arithmetic slips.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), Appendix B, D.2"
---

On arithmetic [chain-of-thought prompting](chain-of-thought-prompting.md), many
wrong finals are **calculator errors**: the plan is right but a numeric step
fails. Wei et al. apply a post-hoc **external calculator** (e.g. Python `eval`
on equations in the CoT, propagating string results across multiple equations)
and lift accuracy when the chain is otherwise correct — e.g. LaMDA 137B GSM8K
14.3% → 17.3% from calc-only fixes, with larger lifts on some models when
calc-only errors dominate.

Harness pattern: keep reasoning in the LM, offload exact arithmetic to a tool
(same spirit as [agent tool categories](agent-tool-categories.md) / Toolformer-
style APIs). Parse equations from the trace deterministically; do not ask the
model to “be more careful” as the only fix. External calc does **not** rescue
[CoT failure modes](cot-failure-modes.md) that are semantic, symbol-mapping, or
missing-step — measure the error mix before adding the tool. Prefer this over
trusting CoT arithmetic alone under
[offline prompt evaluation](offline-prompt-evaluation.md).
