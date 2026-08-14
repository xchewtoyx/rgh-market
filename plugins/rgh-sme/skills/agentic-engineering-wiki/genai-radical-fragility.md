---
type: concept
title: GenAI Radical Fragility
description: >
  Small prompt or model changes produce unforeseeable behavioural shifts, so
  agent harnesses need continuous offline regression—not one-time validation.
sources:
  - title: Taking Testing Seriously
    resource: "Taking Testing Seriously (Bach & Bolton), ch. 7"
---

GenAI systems are “grown, not built”: builders cannot precisely predict how a
prompt tweak, training change, or silent cloud model swap will move behaviour.
Bach & Bolton call this **radical fragility** — a massive regression-testing
problem rooted in the model, not only in application code. Stochastic output
and chaotic sensitivity (a path that works on one dataset fails on a slight
variant) compound the issue.

Harness implication: treat every prompt, tool schema, and model pin as a
regression surface under [harness drift awareness](harness-drift-awareness.md)
and [offline prompt evaluation](offline-prompt-evaluation.md). Prefer
[per-task offline harness tests](per-task-offline-harness-tests.md) that re-run
on provider updates. Do not ship agent autonomy upgrades without re-checking
the suite — see [genai use safety modes](genai-use-safety-modes.md).
