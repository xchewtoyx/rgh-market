---
type: concept
title: Episodic Reflection Memory
description: >
  Store a small buffer of self-reflection texts across trials so later
  trajectories see distilled lessons, not only the latest raw trace.
sources:
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
---

Episodic reflection memory is the long-term half of
[Reflexion](reflexion.md)'s memory design: short-term memory is the current
trajectory history; long-term memory is the Self-Reflection module's verbal
outputs \(sr_t\). Bound the buffer to a small \(\Omega\) (often 1–3
experiences — Shinn et al. truncate to the last **3** self-reflections) so
[context engineering](context-engineering.md) stays feasible while still
carrying lessons across trials.

This is distinct from [memory summarization](memory-summarization.md) of chat
history: entries are *diagnoses and proposed fixes*, not compressed dialogue.
Keeping only the raw last trajectory (**episodic memory without verbal
reflection**) is weaker than storing first-person self-hints — refinement
alone underperforms reflection-guided refinement on HotPotQA. It also differs
from [OS-inspired agent memory](os-inspired-agent-memory.md) archival stores
meant for arbitrary facts — reflection memory is specifically the durable
side of [verbal reinforcement learning](verbal-reinforcement-learning.md).
When \(\Omega\) is exceeded, drop or merge oldest reflections deliberately
rather than silently FIFO-evicting the lesson that explained the last failure.
Programming loops often use \(\Omega = 1\); sliding-window capacity is a known
limit — vector or structured stores are natural upgrades when lessons must
persist beyond a few trials under [memory management](memory-management.md).
