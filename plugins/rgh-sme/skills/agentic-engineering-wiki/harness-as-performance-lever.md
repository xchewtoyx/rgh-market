---
type: concept
title: Harness as a Performance Lever
description: >
  Holding the base model fixed, harness design alone materially shifts task
  completion — and the best harness is model-specific, so it must be
  re-adapted every time the base model changes.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §1–2"
---

A harness — the system prompt shaping work style, the tools exposing file
system and shell, the middleware controlling context and recovery — is not
inert scaffolding around a fixed model. On long-horizon coding benchmarks,
swapping harnesses while holding the base model exactly fixed produces large
swings in task completion, which makes harness engineering "a first-class
lever, not an afterthought" for agent performance rather than a secondary
concern once the model is chosen.

The complication: the **optimal harness is model-specific**. A harness tuned
for one base model can underperform on another and needs re-adaptation as the
underlying model changes — the same tool descriptions, prompt phrasing, and
recovery hints that compensate for one model's blind spots may be redundant or
actively counterproductive for a model that doesn't share them. Manual
adaptation (a developer inspecting trajectories, spotting failure patterns,
hand-crafting fixes) cannot keep pace with how often base models ship,
"creating a widening gap between model capability and the harness needed to
realize it" — the harness a team shipped six months ago is quietly leaving
capability on the table against whatever model is deployed today.

The claim that makes this tractable to automate: harness evolution is
"bottlenecked by observability, not by agent capability" — once an editing
agent has structured evidence over a clear action space, it reliably converges
on better designs without needing new capability itself. That evidence comes
from three matched pieces: which components are editable at all
([component observability](component-observability.md)), what the
trajectories actually show
([Agent Debugger trajectory distillation](agent-debugger-trajectory-distillation.md)),
and whether a given edit's predicted effect held up
([evidence-driven change manifest](evidence-driven-change-manifest.md)).
Together these support an automated
[harness evolution outer loop](harness-evolution-outer-loop.md) that
re-adapts the harness at the pace base models actually ship, instead of at the
pace a team can hand-inspect trajectories.

A harness evolved this way is not automatically overfit to the benchmark it
was tuned on — see
[harness evolution transfer and generalization](harness-evolution-transfer-generalization.md)
for what does and doesn't carry over to unseen tasks and models.
