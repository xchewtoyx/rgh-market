---
type: concept
title: Non-Abstract Large System Design (NALSD)
description: An iterative capacity-modelling methodology that grounds every design candidate in concrete, calculated resource estimates — machines, disks, RAM, network — rather than stopping at a whiteboard sketch.
sources:
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 12"
---

**Non-Abstract Large System Design (NALSD)** is an iterative system design methodology built around one discipline: every candidate design must be grounded in concrete, calculated resource estimates — number of machines, disk IOPS, RAM, network bandwidth — because the design ultimately runs on finite, real hardware, regardless of how elegant it looks as an abstract diagram. Perfect precision isn't the point; combining several *reasonable* approximations into a real number is what surfaces whether a design is actually viable, in a way an abstract sketch cannot.

## The Four Questions

NALSD structures a design iteration around four questions, revisited at every stage of the design's evolution:

1.  **Is it possible?** Ignoring resource constraints, does this design satisfy the stated requirements at all?
2.  **Can we do better?** Is there a more efficient algorithm or architecture — a better algorithmic complexity class, less redundant work — before scaling the current approach up?
3.  **Is it feasible?** Once the design survives (1) and (2), does it fit real budget, hardware, and time constraints when the resource math is actually done? A design that is "possible" in the abstract can still fail this question once translated into machine counts and cost.
4.  **Is it resilient?** What happens when a component — or an entire datacenter — fails? A design that meets throughput and latency requirements but has no failure story is incomplete.

## Two-Phase Structure

The four questions split into two phases:

*   **Basic design phase:** questions 1 and 2, worked out without resource constraints — establish that the approach is sound before pricing it.
*   **Scale-up phase:** questions 3 and 4, plus revisiting question 2 again at scale — establish that the sound approach actually survives contact with real capacity limits and real failure modes.

The process is iterative and nonlinear: a design that passes the basic phase can still flounder in the scale-up phase, forcing a specific component to be replaced rather than the whole design being discarded — a batch-processing stage that can't meet a freshness requirement, say, gets replaced by a streaming stage while the rest of the design carries over.

## Why "Non-Abstract"

The discipline that gives NALSD its name is refusing to let a design pass a stage on the strength of a diagram alone. A single-machine design that "obviously" won't scale still gets its resource math worked out explicitly (data volume, required IOPS, required RAM) so the *reason* it fails feasibility is concrete and specific, rather than a vague intuition — that concreteness is what makes the next iteration's fix targeted rather than guesswork. This grounding is the practical application of the [Utilization Law](utilization-law.md) and [RAID write penalty](raid-write-penalty.md)-style physical-resource math to whole-system design, not just single-component sizing.

## Relationship to Resilience Trade-Offs

The resilience question (4) routinely trades latency or cost for durability — e.g., replicating state across multiple sites via a consensus protocol to survive a datacenter-level outage costs additional round-trip latency per write. NALSD treats this as an explicit, calculated trade-off (how much latency, for how much additional survivability) rather than an unstated assumption, consistent with the [throughput vs. latency trade-off](throughput-vs-latency-tradeoff.md)'s emphasis on making such trade-offs deliberate.
