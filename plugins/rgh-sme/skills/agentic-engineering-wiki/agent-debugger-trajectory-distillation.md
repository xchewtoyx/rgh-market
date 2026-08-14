---
type: concept
title: Agent Debugger Trajectory Distillation
description: >
  Turn millions of raw trajectory tokens into a navigable, per-task root-cause
  report plus a single benchmark-level overview, so a downstream agent can act
  on evidence without reading every trace.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.2"
---

Running k rollouts per task across a benchmark produces trajectories whose
harness-caused errors are individually actionable but collectively "scattered
across millions of tokens of raw messages" — far too much to hand a diagnosing
agent directly. The **Agent Debugger** pattern closes that gap with a two-stage
distillation, not a single summarization pass:

1. **Per-task analysis report** — for every task, analyze the root cause of
   failure (or the pattern behind success) and record it alongside pass/fail
   status. This is the unit that actually grounds a later edit decision.
2. **Benchmark-level overview** — aggregate every per-task report into one
   entry-point document per iteration, so a diagnosing agent can scan the
   whole run's failure landscape before drilling into any single task.

Two more design choices make this usable rather than merely comprehensive.
First, present trajectories as a **navigable, file-based environment** — each
trajectory message lives in its own file, reached through generic shell and
scripting tools, with traces that share a query sharing one environment —
rather than one flat transcript dump. Second, **keep the original traces
available** (raw and lightly cleaned) alongside every report so a consuming
agent can verify a report's claims against ground truth rather than trusting
the summary blindly.

Together these give progressive disclosure at the trajectory level: the
overview is the first hop, per-task reports the second, raw traces the last
resort — saving tokens on the common path while keeping full fidelity
reachable. This is the trajectory-side half of the pattern completed by
[evidence-driven change manifests](evidence-driven-change-manifest.md), which
consume exactly this per-task evidence to justify each proposed edit.
