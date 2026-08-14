---
type: concept
title: Phased Explore-Write-Early Pattern
description: >
  For a long-running autonomous exploration task, mandate a checkpointed
  partial write well before completion and periodic updates after — so a
  useful artifact exists even if the run is cut off early.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. B.3"
---

An agent given a long, open-ended exploration task (map a codebase and write a
development guide; research a topic across dozens of web searches and produce
a reference doc) has an obvious failure mode: it accumulates hours of useful
findings and never writes them down before running out of budget, hitting a
timeout, or being interrupted — total loss of otherwise-good work. The
**phased explore-write-early pattern** removes that risk by making the write
step mandatory and early, not a final step the agent might not reach:

1. **Hard early-write deadline.** Require the first version of the output
   file to be written well before the exploration is expected to finish — even
   if it's incomplete, with explicit placeholder markers (e.g. `[TODO]`) for
   sections not yet researched. A rule stated as a hard iteration ceiling
   ("must call write before iteration 20, no exceptions") is stronger than
   general advice to "write things down as you go," because it forces the
   first checkpoint to actually happen rather than being deferred indefinitely
   by whatever feels more urgent in the moment.
2. **Periodic mandatory updates, not one deferred final write.** After the
   first checkpoint, require the file to be updated at a fixed cadence (e.g.
   at least every N iterations) as new findings accumulate, rather than
   holding everything in working memory for a single write at the end.
3. **Priority-ordered sections.** When the exploration covers several
   sub-topics, fix the order they get written in by importance, so a run that
   terminates partway through still has the highest-value sections filled in
   rather than an arbitrary subset determined by exploration order.
4. **Citation discipline throughout.** Require every claim in the output to
   carry its evidence inline — a file:line reference for source-code
   exploration, a source URL for web research — so the output stays
   independently verifiable rather than becoming an unsourced summary that
   later readers (including the agent's own downstream consumers) can't check
   against the original evidence.

This is the crash-resilience analog of the progressive disclosure that
[Agent Debugger trajectory distillation](agent-debugger-trajectory-distillation.md)
applies to a *reader's* consumption of a large trace corpus — applied here to
the *writer's* side instead: rather than structuring an existing large
document for cheap partial reads, it structures the *production* of a
long-running task's output so a partial, still-useful document exists at
every point in the run, not only at a final write that might never happen. Use it for any agent dispatched to build a durable
artifact (a report, a reference doc, a skill file) over a run long enough that
early termination is a real possibility — which includes most subagent
research or documentation tasks with an open-ended time budget.
