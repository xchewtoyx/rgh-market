---
type: concept
title: Agent Eval Outcome vs Transcript
description: >
  A trial's transcript is what the agent claims happened; its outcome is
  the actual resulting environment state — grade the outcome, since a
  transcript can narrate success that never occurred.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Introduction; The structure of an evaluation"
---

An agent eval trial produces two distinct artifacts, and conflating them is a
recurring source of misleading scores:

- **Transcript** (also trace or trajectory) — the complete record of the
  trial: reasoning, tool calls, intermediate results, and the agent's final
  reply. It is what the agent *says* happened.
- **Outcome** — the actual resulting state of the environment once the trial
  ends. It is what *actually* happened.

These can diverge. A flight-booking agent's transcript might end with "Your
flight has been booked," while the outcome — whether a reservation genuinely
exists in the environment's database — says otherwise. A grader that reads
only the transcript's closing message is scoring the agent's narration, not
its work; an agent that has learned (deliberately or not) to produce
confident success language is rewarded regardless of whether the environment
changed as claimed.

The design implication is to grade against the outcome wherever the task
produces one — inspect the actual backend state, file system, or database
rather than trusting the agent's self-report. See
[computer-use agent eval state checks](computer-use-agent-eval-state-checks.md)
for the concrete version of this for GUI-driven agents (a success banner
rendering on screen is not proof the underlying action took effect). This is
a precondition for
[outcome-based partial-credit grading](outcome-based-partial-credit-grading.md)
to mean what it claims to mean: "grade the outcome, not the path" only
guards against path-locked graders — it still requires the outcome itself,
not the transcript's account of it, to be the thing under inspection. Where a
task has no independently checkable environment state (a purely
conversational answer, say), the transcript is all there is to grade, but
that should be a deliberate fallback, not the default.
