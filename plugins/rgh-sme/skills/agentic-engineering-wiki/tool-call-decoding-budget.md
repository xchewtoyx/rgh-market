---
type: concept
title: Tool Call Decoding Budget
description: >
  Control how freely the model may emit tool-call tokens at decode time — too
  tight under-calls, too loose destroys calibration of when tools help.
sources:
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17 (§5)"
---

When tools are inline next-token decisions
([inline API call interruption](inline-api-call-interruption.md)), the decode
harness can restrict how often call-start tokens appear among the top-\(k\)
candidates. Toolformer’s ablation: \(k=0\) disables tools; \(k=1\) (greedy)
already helps factual completion on some sets; larger \(k\) raises call rate
toward 100% and can raise accuracy further — but **calibration** of *when*
to call is strongest at low \(k\) (no-call subsets outperform average
no-API baselines) and is lost as \(k\) grows.

Treat \(k\) (or temperature / tool_choice analogs in chat APIs) as a
[configurable ACI](configurable-aci-harness.md) knob under
[offline prompt evaluation](offline-prompt-evaluation.md): measure both end-task
score and %API. Prefer the smallest budget that recovers the tasks that need
tools; forcing every generation to call is not the same as teaching the model
when tools reduce future loss
([self-supervised tool annotation](self-supervised-tool-annotation.md)).
