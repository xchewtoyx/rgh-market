---
type: concept
title: Reflection and Error Correction
description: >
  Reflection evaluates feasibility, plans, and outcomes; error correction acts
  on that insight by regenerating plans or retries until the goal is met.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

Reflection is not mandatory for an [LLM agent](llm-agent.md) to run, but it is
often required for it to succeed. It can fire after receiving a query (is this
feasible?), after plan generation (does the plan make sense?), after each step
(are we on track?), and after full execution (is the goal met?).

Reflection generates insight; **error correction** acts on it — regenerate a
plan, retry a tool call, or stop. They are paired but distinct. The same agent
can self-critique via prompting, or a separate scorer can evaluate. Patterns
such as [ReAct](react-loop.md) interleave reasoning and action — thoughts are
internal context updates that do not touch the environment, while acts do —
and [Reflexion](reflexion.md) splits evaluation and self-reflection into modules
under [verbal reinforcement learning](verbal-reinforcement-learning.md),
persisting lessons in [episodic reflection memory](episodic-reflection-memory.md).

Tradeoff: reflection is relatively easy to implement and can yield large gains,
but thoughts, observations, and retries consume tokens and raise latency —
especially on long trajectories already vulnerable to
[compound mistake amplification](compound-mistake-amplification.md). Few-shot
format examples for structured reflection further tax the context budget.
