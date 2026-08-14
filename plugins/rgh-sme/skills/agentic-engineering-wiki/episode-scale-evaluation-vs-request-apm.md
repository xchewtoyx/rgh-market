---
type: concept
title: Episode-Scale Evaluation vs Request-Scale APM
description: >
  Judge harness changes on episode outcomes, trajectory phases, and budgets —
  not on sub-second per-tool-call latency habits borrowed from request APM.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–30"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 4"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
---

An LLM agent’s unit of work is an **episode** (or long trajectory): many
turns of thought, tool calls, and observations that may last minutes, hours,
or days before
[termination](agent-episode-termination-modes.md). Harness and prompt changes
must be scored at that grain — resolve rate, cost per resolved instance,
early-vs-late submit curves, phase failure under
[agent trajectory phases](agent-trajectory-phases.md), and offline regression
under [offline prompt evaluation](offline-prompt-evaluation.md) /
[ACI component ablation](aci-component-ablation.md).

**Request-scale APM** (sub-second latency SLIs, per-call p99, treating each
tool invocation like an HTTP handler) is the wrong *primary* lens for those
changes. A fast `search` or `edit` that leads the agent into a
[blind scroll loop](blind-scroll-loop.md) or an `exit_cost` tail is a harness
regression even when every individual call looks “healthy.” Conversely, a
slower observation that prevents exhaustive match-walking can raise episode
success while worsening naive per-call latency.

Design rule when reviewing a harness change:

1. Name the **episode success contract** first (resolved? intentional submit?
   task I/O correct under
   [per-task offline harness tests](per-task-offline-harness-tests.md)?).
2. Use turn/phase/budget metrics and ablations to attribute the change —
   not mean tool latency alone.
3. Treat token, wall-clock, and cost as **episode attributes** (and as
   secondary budgets), not as substitutes for outcome.

Runtime pipelines that record spans, tokens, and invariants across a long
episode still matter for live drift under
[harness drift awareness](harness-drift-awareness.md), but that instrumentation
practice is observability’s job. The harness-design obligation here is to
refuse APM-shaped questions (“did p99 of `bash` drop?”) when the decision is
episode-shaped (“did resolve rate and recovery after failed localization
improve?”).
