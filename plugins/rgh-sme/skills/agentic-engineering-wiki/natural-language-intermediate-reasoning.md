---
type: concept
title: Natural-Language Intermediate Reasoning
description: >
  Extra tokens or post-answer rationales are not enough — useful CoT needs
  natural-language steps before the answer, not only equations or padding.
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §3.3"
---

Ablations on arithmetic [chain-of-thought prompting](chain-of-thought-prompting.md)
isolate what the intermediate text must do:

- **Equation only** helps short one-/two-step sets but barely moves GSM8K —
  hard word problems resist a single equation map.
- **Variable compute only** (emit dots matching equation length) ≈ standard
  prompting — burning tokens without semantic steps does not help.
- **Reasoning after the answer** ≈ baseline — a post-hoc rationale does not
  substitute for sequential reasoning *before* committing.

So harness defaults should elicit **natural-language steps prior to the final
answer**, not merely longer completions or “explain yourself” after the fact.
This supports [when chain of thought helps](when-chain-of-thought-helps.md) on
hard multi-step tasks and pairs with
[two-stage reasoning–answer extraction](two-stage-reasoning-answer-extraction.md)
when you need a separate parseable answer. Prefer
[self-consistency decoding](self-consistency-decoding.md) over padding when you
want more compute on hard items.
