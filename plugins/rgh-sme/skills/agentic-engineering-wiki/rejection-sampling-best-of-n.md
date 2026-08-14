---
type: concept
title: Rejection Sampling Best-of-N
description: >
  Sample n candidate completions from a base policy and pick the highest-scoring
  one under a reward or judge model — more inference compute, no extra training.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §3.2"
---

**Best-of-n** (rejection sampling) draws a fixed *n* answers from a behavior-
cloned or RL policy and keeps the one ranked highest by a scorer (WebGPT: a
preference reward model; harnesses may use an LLM judge or task metric). It
optimizes against the scorer **without further training**, trading inference
compute for quality — a sibling of
[self-consistency decoding](self-consistency-decoding.md) that ranks with an
external score rather than majority vote.

Use when you already have a reliable offline scorer and can afford *n* full
episodes or answers. Watch for reward overoptimization as *n* grows; keep
[offline prompt evaluation](offline-prompt-evaluation.md) on held-out labels.
This is harness inference design, not the RLHF manufacturing pipeline that
trained the reward model.
