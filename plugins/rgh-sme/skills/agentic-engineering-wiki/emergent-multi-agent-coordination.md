---
type: concept
title: Emergent Multi-Agent Coordination
description: >
  Believable group behaviors — information diffusion, relationship continuity,
  and event coordination — arise from per-agent memory and planning, not
  hard-coded scripts.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Under [generative agent architecture](generative-agent-architecture.md), social
outcomes can emerge from independent perceive–retrieve–plan loops rather than
from authored scripts. Smallville-style examples:

- **Information diffusion** — one agent announces a candidacy; later pairwise
  chats spread it town-wide.
- **Relationship memory** — agents reopen prior topics (photography project)
  across sessions because retrieval surfaces those observations.
- **Coordination** — a single user seed (host a party) cascades into invites,
  decorating help, and attendance without a central coordinator.

Design implication: invest in [memory stream](memory-stream.md) retrieval,
[reflection trees](reflection-tree.md), and an
[agent environment tree](agent-environment-tree.md) so agents share a world
they can partially observe — do not expect emergence from chat prompts alone.
Failure modes that break chains (forgotten invites, no-shows) still happen;
evaluate end-to-end community metrics, not only single-agent coherence.
Seed each agent with a short identity paragraph split into initial memories so
occupations and relationships exist before the first timestep.
