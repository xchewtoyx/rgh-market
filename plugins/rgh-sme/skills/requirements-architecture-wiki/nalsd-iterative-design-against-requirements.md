---
type: concept
title: Iterative Design Against Explicit Requirements (NALSD)
description: >
  Non-Abstract Large System Design states the problem and requirements
  first, then iterates concrete designs — accepting or rejecting each
  against those requirements with documented rationale — rather than
  starting from a preferred architecture.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (ed. Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 12"
---

Non-Abstract Large System Design (NALSD) is a repeatable method for
designing a system against explicit requirements rather than starting from
a favored architecture and justifying it afterward: state the problem,
gather the [requirements](functional-requirement.md), then iterate through
candidate designs until one satisfies the requirements and survives
failure analysis. "Non-abstract" means grounded in concrete resource
estimates — throughput, latency, storage, cost — not a whiteboard sketch
with no numbers attached to it.

The method runs in two phases, non-linearly: a **basic design** phase (is
this even possible? can it be done better?) followed by a **scale-up**
phase (is it feasible at real load? is it resilient to failure? can it
still be done better?). A worked example — designing a dashboard against
explicit SLOs for query latency, data freshness, and throughput — walks
through several design iterations, each one explicitly accepted or
rejected against the stated requirements, with the rejection reasoning
recorded at each step rather than only the final design being kept.

This is the same discipline as [documenting
trade-offs](documenting-trade-offs.md) applied as a repeatable design
loop rather than a one-off write-up: each iteration is itself a small
[architectural decision](architectural-decision-capture.md), and keeping
the rejected iterations' rationale is what lets someone later understand
why the final design looks the way it does, not just what it looks like.
