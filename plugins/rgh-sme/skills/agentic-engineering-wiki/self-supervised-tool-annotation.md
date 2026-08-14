---
type: concept
title: Self-Supervised Tool Annotation
description: >
  Sample candidate API calls, execute them, keep only those that reduce future
  token loss, then finetune so the model learns when tools help.
sources:
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

Self-supervised tool annotation turns a plain-text corpus into a tool-use
dataset without human labels. For each tool, prompt the base LM to propose
inline API calls, execute candidates, and **filter** with a loss test: keep a
call only when prefixing the call *and* its result lowers weighted
cross-entropy on future tokens more than doing nothing or calling without a
result (\(L^- - L^+ \ge \tau_f\)). Merge survivors into the original texts and
finetune with a standard LM objective.

Critical properties for harness designers: \(C^*\) keeps the same underlying
documents as \(C\), so finetuning does not invent new content — only inserts
calls where they empirically help prediction. Filtering compares call+result as
a *prefix* (not mid-sequence insert) because the untrained model is not yet
fluent at API syntax. Sampling thresholds (\(\tau_s\), top-\(k\) positions,
\(m\) candidates) control cost before execution. High \(L^- - L^+\) usually
marks intuitively useful calls; low/negative scores match useless or wrong
ones — but **keeping some noisy survivors** can teach the finetuned model not
to blindly trust every tool result.

This is how [Toolformer-style](inline-api-call-interruption.md) models learn
tool timing without hand-labeled trajectories. Contrast provider
[function calling](function-calling.md), which usually relies on chat templates
and supervised tool-use finetunes rather than corpus-wide loss filtering. Pair
with clear [tool definition design](tool-definition-design.md) so sampled call
strings stay parseable and executable.
