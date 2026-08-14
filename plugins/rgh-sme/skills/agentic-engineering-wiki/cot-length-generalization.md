---
type: concept
title: CoT Length Generalization
description: >
  With sufficient scale, chain-of-thought exemplars of short chains can transfer
  to longer out-of-distribution step counts where standard prompting fails.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §5–§6"
---

On toy symbolic tasks (last-letter concatenation, coin-flip state tracking),
Wei et al. evaluate both **in-domain** items (same step count as few-shot
exemplars) and **OOD** items (more words / flips than shown). Standard
prompting collapses on longer OOD sequences. With
[chain-of-thought prompting](chain-of-thought-prompting.md), models of
sufficient scale show upward OOD curves — CoT **facilitates length
generalization** beyond seen chain lengths, though still below in-domain
ceilings.

Harness implications: when few-shot CoT demos are cheaper to author at short
length, still measure longer / harder held-out cases under
[offline prompt evaluation](offline-prompt-evaluation.md) — in-domain solve
rates can look “toy perfect” while OOD fails. Length generalization still
depends on [scale-dependent chain of thought](scale-dependent-chain-of-thought.md)
(~100B-class models for these symbol-manipulation toys); small models can fail
even in-domain despite exemplars that already encode the perfect procedure.
Pair with [when chain of thought helps](when-chain-of-thought-helps.md) before
treating short demos as covering production depth.
