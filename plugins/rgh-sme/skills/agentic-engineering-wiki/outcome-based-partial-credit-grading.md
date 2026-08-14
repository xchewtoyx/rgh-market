---
type: concept
title: Outcome-Based Partial-Credit Grading
description: >
  Grade what the agent produced or achieved, not the specific tool-call
  sequence it followed to get there — and give multi-step tasks a continuum
  of credit instead of one binary pass/fail.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
---

Two related instincts make agent grading more brittle than it needs to be,
and both point the same direction: grade the **outcome**, not the exact path
taken to it. This assumes the outcome itself — actual environment state, not
the agent's narration of it — is what's under inspection; see
[agent eval outcome vs transcript](agent-eval-outcome-vs-transcript.md) for
that precondition.

**Grade outcomes, not paths.** It's tempting to check that an agent followed
a specific sequence of tool calls in a specific order, since that sequence is
easy to write down and diff against. But agents regularly find valid
approaches an eval designer didn't anticipate, and a path-locked grader
punishes exactly the kind of correct-but-different solution a capable agent
is likely to produce — it's testing "did you do it my way," not "did you
solve the task." Grade what the agent actually produced or achieved instead,
unless the *specific* path is itself part of the task's real requirement (a
required-tool-usage check under
[gold-standard matching](gold-standard-matching.md)'s tool-call criterion is
different from requiring one exact ordering of otherwise-equivalent steps).

**Give multi-step tasks partial credit.** A binary pass/fail on a multi-
component task collapses meaningfully different outcomes into one bucket — an
agent that correctly diagnoses a customer's problem and verifies their
identity but fails to process the resulting refund is doing much better than
one that fails at the first step, and a scoring scheme should say so. Build in
credit for each component a task decomposes into, so results represent a
continuum of success rather than an all-or-nothing signal. This is the eval-
design generalization of
[patch outcome taxonomy](patch-outcome-taxonomy.md)'s code-specific instance
of the same idea — for a code fix, "fixed the issue but broke something else"
and "made no progress at all" are both failures, but they are not the *same*
failure, and treating them as one loses exactly the signal that would tell you
what to fix.
