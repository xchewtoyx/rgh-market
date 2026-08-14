---
type: concept
title: Reflection Tree
description: >
  Periodically synthesize recent memories into higher-level insights that cite
  evidence, forming trees from raw observations up to abstract self-models.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

A reflection tree grows when an agent only has raw observations and fails to
generalize (picking the frequently seen neighbor over the collaborator who
shares a research passion). Trigger reflection when accumulated importance of
recent events crosses a threshold; then: take recent records, ask the LM for
salient high-level questions, use those questions as
[memory stream](memory-stream.md) retrieval queries, extract insights that
**cite evidence** record IDs, and store each reflection with pointers to
citations. Reflections may cite other reflections — leaves are observations;
higher nodes are more abstract.

This differs from [Reflexion](reflexion.md)'s trial-failure verbal RL: the goal
is ongoing self-modeling and social inference inside a
[generative agent architecture](generative-agent-architecture.md), not only
fixing a failed task trajectory. Still pair with
[episodic reflection memory](episodic-reflection-memory.md) discipline — bound
how many abstract nodes enter any one prompt — so reflection does not crowd out
the observations that grounded it.
