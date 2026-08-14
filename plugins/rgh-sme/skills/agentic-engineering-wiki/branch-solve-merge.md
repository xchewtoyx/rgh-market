---
type: concept
title: Branch-Solve-Merge
description: >
  Spawn N independent solver trajectories on the same problem, then merge
  their outputs with a dedicated agent into a stronger combined solution.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

Branch-solve-merge fans a problem out to N independent LLM "solvers" —
separate conversations that each attempt the problem in isolation — then uses
a merging agent to combine all solvers' outputs into a better or more
complete solution. Solvers can be diversified in one of two ways: run
independently at higher temperature for sampling diversity, or explicitly
prompt each one to take a different perspective on the problem.

This is a [multi-agent architecture](multi-agent-architecture.md) pattern for
quality rather than role specialization along a pipeline: parallel
candidates, then a critic/combiner, trading extra tokens and calls (N solvers
plus a merge pass) for a higher chance that at least one branch — or the
combination — beats what a single pass would have produced. Cost and latency
scale with N, so use it when a single trajectory under
[compound mistake amplification](compound-mistake-amplification.md) is too
brittle and the merge step can reconcile conflicts. Pair with
[self-critique prompting](self-critique-prompting.md) or
[Reflexion](reflexion.md) *inside* each branch when individual solvers still
need local retries — but the branches themselves run independently rather
than retrying sequentially from feedback, unlike Reflexion applied at the top
level, so the technique overall is only as good as the merging agent's
ability to reconcile divergent outputs.

It sits alongside the selection-based variants in
[test-time compute sampling](test-time-compute-sampling.md), which pick one
candidate out of N rather than synthesizing a new answer from all of them;
merging is the right choice when the branches' outputs genuinely combine into
something better, selection when only one branch can be "the" answer.
Contrast also [self-consistency decoding](self-consistency-decoding.md) (vote
among finished CoT answers) and [Tree of Thoughts](tree-of-thoughts.md)
(search and prune *intermediate* thoughts): branch-solve-merge keeps full
trajectories isolated and reconciles only at the end.
