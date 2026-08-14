---
type: concept
title: Memory Stream
description: >
  Store natural-language experience records scored by recency, importance, and
  relevance so retrieval packs the most useful memories into context.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

A memory stream is a database of natural-language experience records — each
with creation time, last-access time, and text — that feeds a
[generative agent architecture](generative-agent-architecture.md). Base
records are **observations** (self-behavior, other agents, object states);
[reflections](reflection-tree.md) and plans are written back as the same kind
of object so one retriever serves all tiers.

Full streams overflow any window. Score candidates after min–max normalizing
each factor:

`score = α_recency · recency + α_importance · importance + α_relevance · relevance`

Recency decays exponentially with time since last retrieval; importance is an
LM “poignancy” rating at creation (mundane vs life events); relevance is
embedding similarity to a query describing the current situation. Pack
top-ranked memories that fit the budget into the prompt under
[context engineering](context-engineering.md). Unlike dumping a running
summary alone, selective retrieval keeps *specific* facts available —
[hybrid retrieval](hybrid-retrieval.md) ideas applied to an agent's own life
log rather than an external corpus.
