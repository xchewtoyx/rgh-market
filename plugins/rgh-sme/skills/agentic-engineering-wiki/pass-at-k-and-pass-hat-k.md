---
type: concept
title: "Pass@k and Pass^k"
description: >
  Two opposite ways to summarize an agent's per-trial success rate across k
  attempts — pass@k asks whether at least one attempt succeeds, pass^k asks
  whether all of them do — and they tell opposite stories as k grows.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Agent behavior varies between runs on the same task, so a single trial's
pass/fail result understates what an eval actually knows: a task can have a
90% success rate or a 50% success rate, and either can pass or fail on any
given run. Reporting *how often* an agent succeeds needs a metric over
multiple [trials](agent-grader-types.md), and there are two, built on the
same per-trial success rate but asking opposite questions:

- **pass@k** — the probability of at least one success across *k*
  independent attempts. This *rises* as k grows: more shots on goal raise the
  odds that one of them lands. pass@1 is just the raw per-trial success rate
  (a 50% pass@1 means the agent succeeds on its first try half the time).
  Use pass@k when a single success is all that's needed — proposing several
  candidate solutions and accepting any one that works, which is common for
  coding tasks where a human or a downstream check picks the winner.
- **pass^k** — the probability that *all k* attempts succeed. This *falls*
  as k grows: demanding consistency across more trials is a strictly harder
  bar. A 75% per-trial success rate only has a (0.75)³ ≈ 42% chance of three
  consecutive successes. Use pass^k when reliability on *every* attempt is
  the actual product requirement — a customer-facing agent that fails
  visibly on a fraction of interactions is a worse product than the raw
  per-trial success rate alone would suggest, and pass^k is what quantifies
  that.

At k=1 the two are identical — both reduce to the per-trial success rate —
but they diverge sharply as k grows: by k=10, pass@k approaches 100% while
pass^k falls toward 0% for the same underlying per-trial rate. Reporting only
one of them, or reporting a single pass rate without specifying which
regime it's in, hides which story is actually being told. Choose per
product requirement, not by default: pass@k when one success suffices,
pass^k when every attempt needs to land. This is also why a task scoring 0%
across a large k (pass@100 at 0%) is a strong signal to check the task and
[grader](grader-correctness-as-eval-hygiene.md) rather than assume the agent
is simply incapable — genuine per-trial rates rarely stay at exactly zero
across that many independent attempts.

Two practical refinements apply to whichever variant is in use: infrastructure
exceptions (sandbox crashes, API timeouts) should
[count as failed trials](infra-failure-as-eval-failure.md) rather than being
discarded, and when comparing configurations that trade accuracy for token
cost, fold pass@1 and mean token spend into a single
[successes-per-million-tokens](successes-per-million-tokens.md) figure.
