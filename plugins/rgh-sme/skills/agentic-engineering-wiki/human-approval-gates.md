---
type: concept
title: Human Approval Gates
description: >
  Explicit per-action automation levels so humans can supply plans, validate
  them, or approve irreversible tool calls before the agent proceeds.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

Humans need not be fully absent from an [LLM agent](llm-agent.md). They can
provide a high-level plan the agent expands
([hierarchical planning](hierarchical-planning.md)), validate a generated plan,
or execute risky steps themselves. The harness must define the automation level
allowed per action — for example, require explicit approval before a database
update, code merge, or bank transfer.

This is the agent-specific form of blast-radius control for
[write actions](agent-tool-categories.md): unreliable models should not hold
production delete keys by default. Pair gates with logging of
[function calling](function-calling.md) parameters so reviewers see what would
run before they approve — the same detail a
[tool-call transparency UI](tool-call-transparency-ui.md) surfaces to end
users. In product UIs, expose the same control as authorization prompts plus
inspectable/editable tool calls under
[agent UX steering affordances](agent-ux-steering-affordances.md).

Enforce the gate at the application layer, not the prompt layer: any tool call
with even a remote chance of being dangerous (modifying real-world assets)
must require explicit user authorization before execution via harness-level
interception, not by instructing the model to ask first — application
interception, not prompt-level pleading. Prompted requests for permission can
be skipped by the model under the same failure modes as any other
instruction; an approval step the harness enforces before dispatch cannot be.

Human involvement need not be limited to pre-execution approval. Queue human
reviewers for [workflow tasks](task-io-schema-design.md) whose output needs
human-level judgment the harness cannot yet automate. And when a
[Reflexion](reflexion.md)-based task keeps failing on the same narrow subset
of work items despite retries, that is itself a signal worth routing to a
human: have someone inspect the recurring failure case and adjust the prompt,
rather than letting the task keep burning retries against a problem retries
can't fix.
