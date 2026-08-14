---
type: concept
title: Me-First Prompt Collaboration
description: >
  Form your own answer before consulting the model, start with oversimplified
  prompts, and review outputs with distrust heuristics to avoid anchoring.
sources:
  - title: Taking Testing Seriously
    resource: "Taking Testing Seriously (Bach & Bolton), ch. 7"
---

When humans collaborate with GenAI (or approve agent plans), **Me First**:
produce an independent answer before reading the model’s, to avoid anchoring.
Start with an *overly simple* prompt to establish a doubting mentality rather
than accepting a polished first draft. Review heuristics: distrust first
impressions; probe understanding with self-validating questions; compare against
your independent answer; ignore flattery and projected confidence; ask how you
can evaluate the answer; check stability by re-asking differently.

After a productive session, ask the model to summarize questions asked and turn
that summary into a reusable prompt — feed the
[prompt catalog](prompt-catalog.md). This is operator discipline for
[human approval gates](human-approval-gates.md) and offline critique, not a
substitute for [offline prompt evaluation](offline-prompt-evaluation.md)
oracles. It counters the
[AI productivity paradox](ai-productivity-paradox.md) pressure to skip review.
