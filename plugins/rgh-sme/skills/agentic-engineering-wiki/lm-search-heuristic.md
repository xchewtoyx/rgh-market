---
type: concept
title: LM Search Heuristic
description: >
  Use the language model itself to score or vote on frontier states so search
  can prune, look ahead, or backtrack without a hand-coded heuristic.
sources:
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    resource: "Tree of Thoughts (Yao et al.), pp. 1–14"
---

Classical planners use programmed rules or learned value models as search
heuristics. An LM search heuristic instead asks the same (or a sibling) model to
deliberately reason about whether a partial state is promising — more flexible
than fixed rules and often more sample-efficient than training a separate
evaluator when the base model already encodes task knowledge.

Two common forms from [Tree of Thoughts](tree-of-thoughts.md): **value
independently** — rate each state (scalar or sure/likely/impossible), optionally
with short lookahead simulations or commonsense elimination; and **vote across
states** — cast “which frontier state to expand” as multi-choice selection when
absolute scores are hard (for example passage coherence). Aggregate multiple LM
samples when a more robust heuristic is worth the cost. Heuristics need only be
approximately helpful; over-trusting them recreates
[planning failure modes](agent-planning-failure-modes.md) such as false success.

This pattern sits between prompt-only [self-critique](self-critique-prompting.md)
and a full [Reflexion](reflexion.md) evaluator module: it steers *search over
partial solutions*, not only post-hoc critique of a finished answer. Pair with
explicit state and [world-model-augmented planning](world-model-augmented-planning.md)
so prune-and-backtrack decisions have something concrete to evaluate. When
cutting cost under [deliberate search cost tradeoff](deliberate-search-cost-tradeoff.md),
prefer a strong generator with a cheaper sibling as evaluator — cross-model
ablations show thought *generation* quality dominates evaluation quality.
