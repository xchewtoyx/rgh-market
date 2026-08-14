---
type: concept
title: Per-Task Offline Harness Tests
description: >
  Collect task I/O examples and run offline prompt harnesses so each workflow
  step can change safely without regressing expected completions.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

As soon as [task I/O schema design](task-io-schema-design.md) is stable,
collect example inputs and expected outputs per task. Use them in an offline
harness that exercises the task prompt and checks completions against expected
behaviour before shipping the task — the regression surface for
[prompt and harness evolution](harness-drift-awareness.md) as models and
prompts change. This is the workflow-scoped form of
[offline prompt evaluation](offline-prompt-evaluation.md). For tasks with both
a "did it fix the thing" check and a "did it break anything else" check (code
edits are the canonical case), report outcomes using the fuller
[patch outcome taxonomy](patch-outcome-taxonomy.md) rather than a single
pass/fail rate — it separates safe-but-incomplete progress from actively
harmful regressions that a binary score would hide.

The same I/O examples feed automatic [prompt optimization tooling](prompt-optimization-tooling.md)
(DSPy, TextGrad, and similar), which need exemplars plus a metric. In
production, sample recorded task I/O to watch for quality drift and to A/B
competing task implementations. Runtime telemetry of those samples belongs to
observability practice; designing the per-task contracts and offline checks is
harness maintenance for modular workflows under
[workflow build process](workflow-build-process.md).
