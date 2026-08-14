---
type: concept
title: Coding Agent Eval Design
description: >
  Coding agents grade naturally against deterministic test pass/fail signals,
  with transcript-level heuristics and rubrics layered on top for quality
  beyond correctness.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Coding agents are the easiest agent type to grade with
[code-based graders](agent-grader-types.md), because software usually ships
its own objective correctness check: does it run, do the tests pass. Two
named benchmarks anchor this design space at different task horizons:
repository-scale issue resolution graded by running a project's own test
suite after a patch is applied, and end-to-end technical-task benchmarks that
extend past a single patch into building or configuring a whole system from
source. Both fit the
[functional completion testing](functional-completion-testing.md) family this bundle already
covers in more depth, applied at agent (not single-completion) scale.

Once pass/fail outcome tests validate correctness, it's worth also grading
the **transcript**, not only the final result: heuristic code-quality rules
(complexity, style) catch things a test suite is blind to, and a model-based
rubric can assess process-level behavior — how the agent called tools, how it
interacted along the way — that a binary outcome check never sees. A worked
eval for a security-bug-fix task illustrates combining several grader types
at once: deterministic tests for the specific vulnerability classes, an LLM
rubric for code quality, static analysis (lint/type/security scanners), a
state check confirming a security-logging side effect fired, and a tool-call
check confirming the agent actually read the relevant files before editing —
plus transcript metrics (turns, tool calls, tokens) and latency metrics
tracked alongside, though not as the primary pass/fail signal. In practice,
most coding evals need far less than this full panel — unit-test correctness
plus one LLM rubric for overall quality is the common case, adding more
graders only when a specific failure mode demands it.

When a fix applies but doesn't fully resolve the issue, don't collapse that
into one failure bucket — see
[patch outcome taxonomy](patch-outcome-taxonomy.md) for why "broke something
else" and "made no progress" are different findings a binary score would
hide.
