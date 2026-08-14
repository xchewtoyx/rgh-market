---
type: concept
title: Agent Grader Types
description: >
  Code-based, model-based, and human graders trade objectivity and cost
  against nuance and scale — choose the grader type the check actually needs,
  not whichever is easiest to wire up.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Any single check inside an agent eval — one grader over one portion of a
transcript or outcome — falls into one of three types, each with a distinct
cost/nuance trade-off:

- **Code-based graders** — string/regex/fuzzy match, fail-to-pass/pass-to-pass
  binary tests, static analysis, outcome verification, tool-call verification,
  transcript-shape checks (turns taken, tokens used). Fast, cheap, objective,
  reproducible, easy to debug. Weak where a valid completion doesn't match the
  expected pattern exactly, or the task is inherently subjective. This is the
  family [functional completion testing](functional-completion-testing.md) and
  [gold-standard matching](gold-standard-matching.md) instantiate.
- **Model-based graders** — rubric scoring, natural-language assertions,
  pairwise comparison, reference-based evaluation, multi-judge consensus.
  Flexible, scales past what humans can hand-check, captures nuance and
  open-ended output. Non-deterministic, costlier than code, and needs
  calibration against human judgment before it can be trusted — see the
  [SOMA LLM assessment](soma-llm-assessment.md) for structuring
  the questions and
  [grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md)
  for the calibration step itself.
- **Human graders** — subject-matter-expert review, crowdsourced judgment,
  spot-check sampling, A/B testing, inter-annotator agreement. The
  gold-standard-quality option and the one used to calibrate model-based
  graders in the first place, but expensive, slow, and often bottlenecked on
  expert availability at scale.

How these three types combine differs by agent type in practice — see
[coding agent eval design](coding-agent-eval-design.md),
[conversational agent eval simulation](conversational-agent-eval-simulation.md),
[research agent eval groundedness](research-agent-eval-groundedness.md), and
[computer-use agent eval state checks](computer-use-agent-eval-state-checks.md)
for what each domain leans on and why.

Whatever type a grader is, it should sit inside a suite that tests both
directions of any behavior it's checking for — see
[balanced eval problem sets](balanced-eval-problem-sets.md).

A single task commonly needs more than one grader — a code-based tool-call
check plus a model-based rubric plus an occasional human spot-check — and how
their individual results combine into a task-level pass/fail is itself a
design choice; see
[grader score combination](grader-score-combination.md). Choosing the right
grader type per check, rather than defaulting to whichever is easiest to
stand up, is as much a part of
[per-task offline harness tests](per-task-offline-harness-tests.md) design as
picking the example set to test against.
