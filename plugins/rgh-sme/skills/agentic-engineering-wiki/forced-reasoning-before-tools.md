---
type: concept
title: Forced Reasoning Before Tools
description: >
  Disable tool choice for a turn while still declaring tools so the model must
  plan in language before it is allowed to call functions.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

When a task jumps into [function calling](function-calling.md) without
planning, force a reasoning turn first: set `tool_choice` to `"none"` (or the
provider equivalent) while **still including** the tool schemas in the request.
The model sees what tools it will have next turn and must think in prose —
often with a [chain of thought](chain-of-thought-prompting.md) or
[plan-and-solve](plan-and-solve-prompting.md) cue — before a later turn enables
calls.

This is a harness control for task quality inside
[templated prompt tasks](templated-prompt-task.md) and
[ReAct](react-loop.md)-style loops: separate "think about the inventory" from
"invoke." Some models (for example Claude Opus) reason by default; others need
the explicit nudge. Pair with clearer prompts before escalating to
[Reflexion](reflexion.md) retries. It is a narrower, single-turn version of the
same thinking/acting split behind
[plan-validate-execute](plan-validate-execute.md) — a request-parameter toggle
rather than an architectural one.
