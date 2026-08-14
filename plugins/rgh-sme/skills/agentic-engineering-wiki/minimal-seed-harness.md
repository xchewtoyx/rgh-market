---
type: concept
title: Minimal Seed Harness
description: >
  Start an automatic harness-evolution loop from a deliberately minimal seed
  so every component the loop adds must earn its place against measured
  rollouts, not inherit unattributed credit from hand-tuning.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.1"
---

When bootstrapping an automated
[harness evolution outer loop](harness-evolution-outer-loop.md), the
temptation is to seed it from a reasonably capable starting harness so early
iterations aren't wasted on obvious gaps. That temptation should be resisted:
a seed harness already fitted to the target benchmark contaminates the
attribution of every edit that follows, because there is no way to tell
whether a later gain came from the loop's own evolution or from credit the
hand-tuned seed was carrying all along.

The alternative is a **deliberately minimal seed**: a single shell-execution
tool, no middleware, no skills, no sub-agents — nothing pre-tuned for the
target task or benchmark. "The minimal seed forces every component AHE adds
to earn its place against measured rollouts." This is the design-time twin of
[minimal prompt crafting](minimal-prompt-crafter.md): start from the smallest
functional harness, and let every addition beyond it be justified by an
[evidence-driven change manifest](evidence-driven-change-manifest.md) rather
than inherited from an unmeasured starting point.

A minimal seed can still be given a small, protected head start — for example
a one-shot bootstrap pass that seeds a handful of reusable skills from
framework source and public references before the evolve loop begins — as
long as that head start gets **no special protection** afterward: from the
next iteration on, the evolve agent is free to keep, refine, or delete those
seeded skills based on observed rollouts, the same as anything it wrote
itself. A protected head start that the loop can never touch would reintroduce
exactly the attribution contamination the minimal seed exists to avoid.
