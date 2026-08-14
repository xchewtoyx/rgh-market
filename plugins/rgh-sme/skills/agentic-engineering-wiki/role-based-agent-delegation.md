---
type: concept
title: Role-Based Agent Delegation
description: >
  Assemble agents with distinct roles, goals, and tools and delegate work
  between them like a team, following the AutoGen and CrewAI frameworks.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

An emerging pattern for [multi-agent architecture](multi-agent-architecture.md):
define agents with specific roles and delegate work to them like a team
assigned to a goal, rather than one agent doing everything.

**AutoGen**'s simplest usage has two roles: an **Assistant** — a standard
conversational [LLM agent](llm-agent.md) with background tool use — and a
**UserProxy**, which stands in for the human user. The UserProxy is
system-messaged to work with the Assistant toward the human's stated goal,
acting as a corrective force (keeping the Assistant on track, offering
recommendations) and eventually declaring the goal accomplished. An
Assistant–UserProxy pair is itself a small LLM-based workflow. AutoGen also
offers a **group chat manager**: a workflow coordinator holding several
role-specific conversational agents (each with its own system message and
tools) that delegates incoming requests to whichever agent it judges
appropriate — a role-labeled instance of
[LLM-driven workflow routing](llm-driven-workflow-routing.md).

**CrewAI** fills a similar niche: assemble "crews" of agents, each with its own
role, goal, backstory, and tool subset from the shared
[tool inventory](tool-inventory.md), given tasks to resolve toward an overall
goal. Agents can be arranged into processes:

- **Sequential** — like a pipeline.
- **Hierarchical** — a director agent routes work, similar to AutoGen's group
  chat manager.
- **Consensual** — agents collaborate to determine how work gets done.

Both frameworks trade the predictability of a fixed pipeline for delegation
flexibility, so the same simpler-is-better guidance applies: prefer role
delegation only where a fixed [AI pipeline orchestration](ai-pipeline-orchestration.md)
genuinely cannot express the needed coordination.

The Assistant/UserProxy pair also shows up as the last resort on the
[task quality escalation ladder](task-quality-escalation-ladder.md): for a
complex, open-ended workflow task that resists being pinned down as a single
templated prompt, an expert conversational agent equipped with the needed
tools, paired with a user-proxy agent pushing it toward the goal, can succeed
where a single-shot prompt cannot — an expert agent alone often won't act
without a conversational partner. Treat this as experimental relative to the
more deterministic steps earlier on that ladder.
