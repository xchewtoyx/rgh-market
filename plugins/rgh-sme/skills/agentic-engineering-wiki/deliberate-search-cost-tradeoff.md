---
type: concept
title: Deliberate Search Cost Tradeoff
description: >
  Pay for tree search over thoughts only when CoT already fails — knobs like
  beam size, votes, and mixed generate/evaluate models buy performance at
  5–100× token cost.
sources:
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    resource: "Tree of Thoughts (Yao et al.), pp. 1–14"
---

[Tree of Thoughts](tree-of-thoughts.md) multiplies generation versus IO or
[chain of thought](chain-of-thought-prompting.md) — typically ~5–100× more
completion tokens depending on beam width, depth, and passage length. Empirically
ToT can beat best-of-100 CoT at similar token volume on hard puzzles (Game of
24), but on GSM8K / StrategyQA with GPT-4 the lift over CoT is tiny because the
base path already works or the bottleneck is knowledge, not search.

Design rule: use deliberate search where early irreversible choices and CoT
fragility dominate; skip it for tasks the base model already solves. Tune
performance vs cost via beam size \(b\), vote count, few- vs zero-shot
proposers, early-stop BFS, and trimming “impossible” thoughts from the
[LM search heuristic](lm-search-heuristic.md). Mixed models help: stronger
generators with cheaper evaluators retain most accuracy (generation is the
bottleneck; weak generate + strong evaluate collapses). Prefer open or smaller
LMs for the expensive frontier when quality allows, and treat finetuning for
high-level thought propose/evaluate as a longer-term alternative to forever
paying search at inference.
