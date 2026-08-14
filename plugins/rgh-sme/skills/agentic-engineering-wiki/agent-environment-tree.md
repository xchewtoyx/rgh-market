---
type: concept
title: Agent Environment Tree
description: >
  Represent places and objects as a containment tree rendered to natural
  language, with each agent holding only a personal subgraph that can go stale.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Long-horizon sandbox agents need a world model richer than the latest
observation string. An **environment tree** stores areas and objects with
containment edges (“stove in the kitchen”), rendered to NL for prompting.
Each agent keeps a **personal subgraph** of what it has seen (home, workplace,
common shops), updated on navigation — not an omniscient shared map. Subtrees
can go stale until re-entry.

Action location selection walks the agent’s tree from root to a leaf via
recursive LM prompts (prefer staying put when the activity fits the current
area), then pathfinding animates movement. Object state updates similarly:
query the LM to map an NL action onto status changes (espresso → machine
brewing). Users or other agents can rewrite object status in NL (“stove is
burning”) so the next perceive → store cycle notices and reacts — a concrete
affordance for [generative agent architecture](generative-agent-architecture.md)
and [world-model-augmented planning](world-model-augmented-planning.md).
