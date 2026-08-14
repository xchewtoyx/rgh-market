---
type: concept
title: Generative Agent Architecture
description: >
  Condition long-horizon agent behavior on a memory stream, recursive
  reflection, and hierarchical plans rather than single-shot LM prompts.
sources:
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Generative agent architecture (Park et al.) extends an LLM with three
coupled loops so behavior stays coherent as experience grows: record
perceptions in a [memory stream](memory-stream.md), periodically synthesize
[reflection trees](reflection-tree.md), and maintain
[hierarchical plans](hierarchical-planning.md) that decompose into actionable
steps. Reflections and plans write back into the same stream and are retrieved
like observations.

Plain few-shot or [chain-of-thought](chain-of-thought-prompting.md) prompts
condition only on the current context window; they cannot hold days of
multi-agent social history. This architecture is for *believable simulacra*
under cascading interactions — not a claim of genuine agency — and remains the
spine even as base models improve. Failure modes to design for: retrieval
misses, embellished memories, and overly formal speech inherited from
instruction tuning.

For harness builders, treat it as an instance of
[OS-inspired agent memory](os-inspired-agent-memory.md) plus
[reflection and error correction](reflection-and-error-correction.md) at social
timescales, with a perceive → store → continue-or-react → (re)plan action loop
akin to [ReAct](react-loop.md) but driven by retrieved biography rather than
only the latest tool observation. Ground agents in an
[agent environment tree](agent-environment-tree.md) so location and object
state are partial and updatable. Expect
[emergent multi-agent coordination](emergent-multi-agent-coordination.md) when
many such agents share a sandbox — diffusion and parties are architecture
tests, not feature flags. Controlled interviews after simulation days show
**believability** rises with each memory/reflection/planning layer; ablations
without reflection fail to synthesize (e.g. gift suggestions from many
meetings). End-to-end metrics: information diffusion, relationship-graph
density, and coordination attendance. Design against
[memory hacking](memory-hacking.md), embellished recalls, and instruction-
tuning over-cooperativeness. For human steering, speaking as an agent’s **inner
voice** (directive persona) is more likely obeyed than an external interlocutor;
expose that as an [agent UX steering](agent-ux-steering-affordances.md) mode
alongside ordinary NL conversation.
