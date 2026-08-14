---
type: concept
title: Toolformer Tool Use
description: >
  Train an LM to choose which API to call, when, with what arguments, and how
  to use the result — self-supervised, without tying tools to one task.
sources:
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

Toolformer-style tool use treats API calling as part of next-token prediction.
The model must decide **which** API, **when** to call it, **what** arguments to
pass, and **how** to incorporate the returned text into later tokens. Training
uses [self-supervised tool annotation](self-supervised-tool-annotation.md) from
a handful of demos per API, then
[inline API call interruption](inline-api-call-interruption.md) at inference.

Two desiderata: learn tools without large human annotations (what humans find
useful may differ from what helps the model), and **preserve generality** — the
LM chooses tools itself rather than being wired to a single task. Apply the
pipeline to the same pretraining-style corpus so core language modeling ability
is not sacrificed.

Canonical capability-extension tools — calculator, QA, search, translation,
calendar — target failures scaling alone does not fix: arithmetic, stale or
hallucinated facts, low-resource languages, and time awareness (see
[agent tool categories](agent-tool-categories.md)). Prefer this lineage when
you control finetuning; prefer provider [function calling](function-calling.md)
when the deployed model already speaks chat-style tool messages.

Evaluate **zero-shot** after finetuning: natural-language task instructions
with **no** in-context tool demos, decode with
[tool-call decoding budget](tool-call-decoding-budget.md) (for example allow
`<API>` in top-\(k=10\)) and **at most one call per input** to stop loops.
Expect strong gains on LAMA/math when the right tool is nearly always used
(~98% QA / calculator); weaker open-domain QA when search is non-interactive
BM25; TEMPLAMA gains often from search/QA rather than Calendar because
ideal Calendar→QA chains are barred. Ability to *leverage* tools emerges
around ~775M parameters under the same recipe — smaller models look similar
with vs without APIs. Finetuning on \(C^*\) need not raise disabled-API
perplexity vs finetuning on plain \(C\).

**Known limits (Schick et al.):** sampled calls are **independent per tool** —
no chained Calendar→QA exemplars in \(C^*\); no interactive multi-hit browsing
or query refinement; call decisions are **prompt-sensitive**; filtering is
sample-inefficient (millions of docs → thousands of useful calculator
examples — iterate the bootstrap); and there is **no cost awareness** when
deciding to call. Address chaining with harness-level
[function-call chaining](function-call-chaining.md) or ReAct-style loops;
address decode-time call rate with
[tool-call decoding budget](tool-call-decoding-budget.md).
