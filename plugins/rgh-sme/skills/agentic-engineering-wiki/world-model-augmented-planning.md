---
type: concept
title: World-Model-Augmented Planning
description: >
  Planning needs predicted action outcomes and backtracking, so bare
  chain-of-thought action lists often fail without state or search support.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    resource: "Tree of Thoughts (Yao et al.), pp. 1–14"
---

Whether autoregressive models can truly plan remains contested. Critics argue
that fluent-looking plans are often extracted general knowledge rather than
executable search over outcomes. Planning is fundamentally a search problem:
explore paths to a goal, predict rewards, pick a path — sometimes none exists —
and backtrack when a branch fails.

A bare action sequence from chain-of-thought does not supply each action's
**outcome state**. Knowing that turning right leads off a cliff is what lets a
planner rule that branch out. Approaches that treat language-model reasoning as
planning with a world model use the model's knowledge to predict outcomes and
guide coherent plans; alternatively, the model can be only *part* of a planner
augmented with search and explicit state tracking.
[Tree of Thoughts](tree-of-thoughts.md) is one concrete harness: thoughts as
states, an [LM search heuristic](lm-search-heuristic.md) for prune/expand, and
BFS or DFS with lookahead and backtracking.

For harness design, do not assume "think step by step" equals a reliable plan.
Prefer [plan-validate-execute](plan-validate-execute.md), explicit state,
[reflection](reflection-and-error-correction.md), and tools that reveal
environment feedback after each action.
