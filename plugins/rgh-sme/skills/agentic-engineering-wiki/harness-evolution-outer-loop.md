---
type: concept
title: Harness Evolution Outer Loop
description: >
  The rollout-attribute-distill-edit-commit cycle that drives automatic
  harness evolution one iteration at a time, with multiple rollouts per task
  so partial-pass signal survives into diagnosis.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3, Algorithm 1"
---

Automatic harness evolution runs as a fixed per-iteration cycle rather than a
single generate-and-check pass. Per iteration t:

1. **Rollout** — run the current harness H(t−1) against k≥2 rollouts per task.
2. **Clean** — normalize raw traces to a canonical form.
3. **Attribute** (t≥2 only) — compare the prior round's
   [change manifest](evidence-driven-change-manifest.md) predictions against
   what actually happened, and roll back edits whose verdict fails, *before*
   any new distillation runs — so the verdict lands inside the evidence corpus
   the next edit is written against, binding each prior manifest entry "as a
   contract rather than a rationale."
4. **Distill** — run
   [Agent Debugger trajectory distillation](agent-debugger-trajectory-distillation.md)
   over the cleaned traces.
5. **Evolve** — write new
   [component-observable](component-observability.md) edits plus a new change
   manifest, inside the
   [controllability](self-modifying-harness-controllability.md) constraints.
6. **Commit** — tag the iteration in version control; track the
   best-so-far harness by pass@1.

**Why k≥2 rollouts per task matters beyond averaging noise:** with only one
rollout, a task is binary evidence — pass or fail — and gives no signal about
*how close* a failure came to succeeding. With k≥2, tasks that pass some
rollouts and fail others become the single highest-value diagnostic case:
compare a passing and a failing rollout of the *same* task, find the exact
step where they diverge, and turn the passing rollout's strategy into the
reliable default rather than a lucky sample. **pass@k gauges a capability
ceiling but is explicitly not the optimization target** — the loop's job is
converting pass@k successes into pass@1 successes by making the winning
strategy consistent across rollouts, not by chasing whichever run happened to
succeed once.

When the loop dispatches several edit variants in parallel for the same
iteration (parallel exploration under a shared "MANDATORY strategy
constraint" so each explores a genuinely different direction), treat a losing
variant as data rather than discarding it outright: cross-variant analysis
that groups traces by variant can explain *why* one approach worked better for
specific tasks, and a losing variant can still have solved tasks the winner
missed — worth merging the effective parts of both rather than keeping only
the higher-aggregate-score variant.
