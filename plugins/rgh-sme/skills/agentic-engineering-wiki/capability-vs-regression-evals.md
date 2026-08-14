---
type: concept
title: Capability vs Regression Evals
description: >
  Capability evals should start hard and pass rarely, to give a target to
  climb toward; regression evals should pass almost always, so any drop is a
  signal something broke.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Two eval suites answer different questions and should be read with opposite
expectations for their pass rate:

- **Capability ("quality") evals** ask "what can this agent do well?" — they
  should target tasks the agent currently struggles with and start at a
  *low* pass rate on purpose. A capability eval that already passes nearly
  every time gives no hill left to climb; it's measuring something the agent
  already does, not the next thing worth improving.
- **Regression evals** ask "does the agent still handle what it used to?" —
  they should sit at a pass rate near 100%, so any decline is a legible
  signal that something broke, not statistical noise. This is the harness's
  early-warning system against backsliding while a team hill-climbs on
  capability evals elsewhere.

Both suites also need to settle which of [pass@k or
pass^k](pass-at-k-and-pass-hat-k.md) they're actually reporting — a
capability eval chasing "can it do this at all" usually wants pass@k (does
at least one attempt land), while a regression eval guarding reliability for
users usually wants pass^k (does every attempt land); conflating the two
under one unlabeled "pass rate" number hides which question is being
answered.

Both suites need to run together: optimizing hard against a capability eval
without a parallel regression suite is exactly the situation where a change
that raises the target metric silently breaks something else the agent used
to do reliably. This is the two-target refinement of
[eval test granularity](eval-test-granularity.md)'s regression/unit-test
split — that note is about *scope* (whole loop vs. one model pass);
capability-vs-regression is about *target pass rate and purpose* for evals at
any scope.

**Graduation pattern.** A capability eval doesn't stay a capability eval
forever: once an agent is launched and optimized against it, a capability eval
with a now-high pass rate can *graduate* into the regression suite, switching
its purpose from "can we do this at all?" to "can we still do this
reliably?" — the same test, re-purposed, rather than two separately
maintained suites drifting apart. Treat capability evals as a pipeline that
continuously feeds the regression suite as the frontier moves, not two static,
unrelated collections. A capability eval that reaches near-100% has stopped
giving useful signal at all — see [eval saturation](eval-saturation.md) for
why that specifically calls for graduation plus a fresh, harder eval to take
its place, not just for retiring the old one. [Eval-driven
development](eval-driven-development.md) is the deliberate version of
starting a capability eval at a low pass rate: writing it for a bet on a
future model before the current one can clear it.
