---
type: concept
title: Self-Modifying Harness Controllability
description: >
  Scope a harness-editing agent's write access to the harness workspace alone
  so every measured gain is attributable to a harness edit, not a disabled
  check or a swapped model.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.3, App. B.2"
---

An agent that both edits a harness and is scored on the result has an obvious
shortcut available: disable the verifier, swap in a stronger model, or raise
the reasoning/token budget, all of which raise the score without improving the
harness at all. **Controllability** is the constraint that closes that
shortcut off by construction rather than by hoping the editing agent behaves:

- The editing agent may write **only** inside the harness workspace.
- The evaluation runs directory, tracer, verifier, and LLM configuration are
  **read-only** — explicitly including model choice, temperature, max tokens,
  and reasoning effort, since "LLM config changes consistently cause broad,
  hard-to-diagnose regressions" that would be misattributed to whatever
  harness edit shipped alongside them.
- The **seed** system prompt's original rules are **non-deletable** — an
  editing agent can add to them but not quietly strip out the baseline it's
  meant to be improving on.

This is the same family of concern as
[agent system-level defenses](agent-system-level-defenses.md) and
[human approval gates](human-approval-gates.md) for blast-radius limits on
model-generated write actions, specialized to the case where the actions in
question are edits to the very harness the agent runs inside — a
self-modification loop where the write surface must be sandboxed even more
carefully than a normal task's write surface, because an unconstrained
self-modifier's shortcuts are invisible to a score-only observer. Pair with a
[minimal seed harness](minimal-seed-harness.md) so there is nothing pre-tuned
for the editing agent to exploit at the starting point either.

**This is a partial guardrail stack, not a complete one.** Workspace scoping,
read-only infrastructure, and per-edit git-commit rollback bound *what* can be
edited and let a bad edit be undone, but they do not guarantee edits stay
useful or safe over an arbitrarily long horizon — treat an evolve loop built
this way as a controlled research capability, not a fully governed autonomous
system, until stronger regression-foresight and long-horizon cleanup exist.
