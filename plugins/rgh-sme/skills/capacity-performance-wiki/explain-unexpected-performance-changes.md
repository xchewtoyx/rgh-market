---
type: concept
title: Explain Unexpected Performance Changes
description: A performance-analysis discipline of root-causing unexplained improvements as rigorously as regressions, since an unexplained win can hide a latent risk that has not yet manifested as a loss.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 16"
---

Performance investigations naturally focus on unexplained *regressions* — a metric got worse and needs a root cause. It is easy to skip the same rigor for unexplained *improvements*: if CPU utilization drops 30% after a migration, the instinct is to accept the win and move on. This is a mistake.

## Why Unexplained Wins Are Worth Investigating

An unexplained performance gain can be caused by the same class of change that causes regressions — it just happens to have landed favorably this time. Left uninvestigated, the underlying cause can:

*   **Mask a change that will regress under different conditions.** A gain that comes from an environment-specific side effect (a memory allocator change, a kernel version bump, a new instance type's alignment behavior) may not hold under a different workload shape, a future kernel upgrade, or at a different scale — and without knowing why the gain happened, there is no way to know when it might silently reverse.
*   **Hide an unrelated, currently-dormant problem** that the same change happens to have also introduced or obscured, which the win's investigation would otherwise have surfaced.
*   **Represent an unportable assumption** — a benefit tied to specific hardware, compiler, or OS behavior that quietly stops holding the next time any one of those changes.

## Applying the Discipline

This is the retroactive counterpart to [measuring before optimizing](measure-before-optimizing.md): that discipline establishes a baseline and confirms a *deliberate* change's effect before trusting it; this one applies the same before/after rigor after the fact, to a change whose performance effect wasn't the thing originally being tested for.

Treat an unexplained gain with the same [USE Method](use-method.md) / resource-triage rigor as an unexplained loss: verify the workload is actually identical, check every resource dimension for what changed, and drill down with hardware and software counters until the mechanism is understood, not just observed. A concrete example of this discipline uncovering a real mechanism is documented in [instructions per cycle](instructions-per-cycle.md) and [transparent huge pages](transparent-huge-pages.md): a 30% CPU utilization drop after a migration was traced, via `perf stat` instruction counts and page-fault tracing, to a compiler/allocator change that shifted heap allocations onto huge-page boundaries — a genuine, explainable win, but only confirmed as one after the investigation.
