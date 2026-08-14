---
type: concept
title: Verbal Reinforcement Learning
description: >
  Improve an agent across trials with linguistic self-reflection stored in
  memory instead of weight updates or scalar reward fine-tuning.
sources:
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
---

Verbal reinforcement learning treats natural-language feedback as a
**semantic gradient**: after a trial, the agent reflects on sparse task
signals, writes actionable lessons, and conditions later trials on that text.
No LLM fine-tuning is required — the policy is effectively
\(\{M_a, \textit{mem}\}\), the actor plus an episodic memory of reflections.

Compared with scalar or vector rewards, verbal feedback can name *which*
action to change and *how*, which helps credit assignment in long
trajectories. Tradeoffs: it depends on the quality of self-evaluation or
heuristics, and it offers no formal success guarantee. Use it when few-shot
in-context examples are not enough to learn from environment feedback but
updating weights is too expensive — the usual regime for
[LLM agents](llm-agent.md) in production harnesses.

[Reflexion](reflexion.md) is the canonical modular instantiation (Actor,
Evaluator, Self-Reflection). Pair reflections with bounded
[episodic reflection memory](episodic-reflection-memory.md) so lessons persist
across trials without blowing the context budget. Evaluators need not be
learned judges: for sparse-reward text games, a hand-written heuristic
(repeat action+response >3 times, or steps >30) can trigger reflection as
effectively as an LLM binary classifier; for code, a
[self-generated test evaluator](self-generated-test-evaluator.md) supplies
executable pass/fail — choose the cheapest reliable signal under
[offline prompt evaluation](offline-prompt-evaluation.md). Verbal policy
optimization can still trap in non-optimal local minima when exploration is
weak; terminate rather than inventing more reflections.
