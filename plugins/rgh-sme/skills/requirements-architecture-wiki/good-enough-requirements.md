---
type: concept
title: Good-Enough Requirements
description: >
  Perfect requirements are never achievable; the goal of discovery is
  sufficient risk reduction to build the right product, not exhaustive
  certainty that delays every decision.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 1"
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (James Serra), ch. 15"
---

Requirements discovery never reaches a state of perfect, complete
certainty — stakeholders' understanding evolves, the business changes
underneath the project, and some ambiguity is only resolved by building
something and getting a reaction (see [requirements discovery vs.
gathering](requirements-discovery-vs-gathering.md)). The goal is not
perfection; it's discovering requirements good enough to materially
reduce the risk of building the wrong product, without tipping into
paralysis-by-analysis.

This is a genuine trade-off, not a license to skip discovery: the same
book that insists every requirement needs a
[fit criterion](fit-criterion.md) and must pass a [quality
gateway](quality-gateway.md) also insists that chasing an unreachable
standard of completeness is its own failure mode. The practical judgment
call is [requirements prioritization](requirements-prioritization.md) and
[completeness checking](requirements-completeness-checking.md) applied
with a sense of proportion — spend discovery effort where the cost of
being wrong is highest (high business value, high risk, high
dissatisfaction-if-missing), and accept residual uncertainty everywhere
else rather than trying to drive it to zero across the board.

Both directions of the trade-off have observable, concrete symptoms.
Spending too long on up-front discovery — one reported case ran requirements
gathering for over a year, producing hundreds of pages nobody read in
full — puts the entire project behind schedule before any code exists,
and the resulting document is often too large to actually be used as a
reference. Spending too little leaves developers guessing at what end
users actually want, producing the wrong features. The practical
resolution is the same one [requirements discovery vs.
gathering](requirements-discovery-vs-gathering.md) already argues for on
different grounds: bound the up-front discovery phase to a few weeks so
building can start, then keep discovering requirements in parallel with
development in a continuing, iterative cycle — building parts of the
solution, revisiting design and planning against real feedback, and
repeating — rather than treating discovery as a single phase that must be
exhaustive before anything else can begin.
