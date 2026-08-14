---
type: concept
title: Eval Test Granularity
description: >
  Test a single model pass or the whole application loop depending on what
  changed — unit-test isolated prompts, regression-test architecture changes.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

Evaluation can target three things: the model itself, a single interaction
with the model (one prompt), or how many interactions fit together across the
whole [LLM application loop](llm-application-loop.md). This maps onto
traditional software testing: **regression tests** cover the whole
interaction loop end to end; **unit tests** cover one isolated model pass.
Many applications have only a single model call, making the distinction
moot — but for apps with an iterated-call loop, choosing test granularity
means carving out a part of the loop and declaring "this is what I'm testing
right now." The ideal is regression tests covering as much of the
[feedforward pass](llm-application-feedforward-pass.md) as possible, plus
unit tests for every individual interaction judged both hard and important.

Which granularity fits which kind of change:

- **Swapping or upgrading the underlying model** — capture as large a part of
  the app as possible in regression tests, unless different calls
  deliberately use different models (e.g. for cost or latency reasons via
  [model tiering](model-router.md)), in which case test each affected pass in
  isolation instead.
- **Optimizing a prompt or generation parameters** (temperature, completion
  length) — focus on small unit tests of the single model pass being tuned,
  since that's what's directly affected. Regression tests can be used too if
  sensitive enough, but statistical noise more easily drowns an individual
  effect at whole-loop granularity.
- **Changing overarching application architecture** (the loop's shape itself,
  under [agent control flow](agent-control-flow.md)) — regression tests are
  required by definition, since there's no smaller unit that captures a
  structural change.

If forced to pick one starting point, favor something that tests the whole
loop, since testing should mirror the reality that's actually being
optimized; once a near-whole-loop harness exists, add targeted unit tests for
specific critical parts on top of it. In all tests, also record total latency
and token consumption — not the main signal, but worth tracking for
large effects that a pure quality metric would miss.

This is orthogonal to [capability vs regression evals](capability-vs-regression-evals.md):
granularity picks *what part of the loop* a test covers, while capability
versus regression picks *what pass rate to expect and why* — a unit test and
a whole-loop regression test can each be either a capability probe or a
regression guard depending on its target pass rate and purpose.
