---
type: concept
title: Reflexion
description: >
  Separate an Actor, Evaluator, and Self-Reflection module so sparse outcome
  signals become verbal lessons that condition the next trial.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    resource: "Reflexion (Shinn et al.), pp. 1–19"
---

Reflexion (Shinn et al., 2023) formalizes
[reflection and error correction](reflection-and-error-correction.md) as
[verbal reinforcement learning](verbal-reinforcement-learning.md) with three
roles:

1. **Actor \(M_a\)** — generates text and actions from observations (often via
   [ReAct](react-loop.md) or [chain of thought](chain-of-thought-prompting.md)).
2. **Evaluator \(M_e\)** — scores a finished trajectory (exact match,
   heuristics for common failures, or LLM-as-judge / self-written unit tests).
3. **Self-Reflection \(M_{sr}\)** — turns sparse reward plus the trajectory
   into nuanced verbal feedback \(sr_t\) stored in
   [episodic reflection memory](episodic-reflection-memory.md).

Loop: generate \(\tau_t\), evaluate, reflect, append \(sr_t\) to memory, retry
until pass or trial budget. Scalar \(r_t\) tracks improvement; \(sr_t\) is the
amplified, actionable signal the Actor actually conditions on. Example: tests
fail on all-negative inputs; reflection names that edge case; the next Actor
trajectory covers it — the canonical case is writing software against a
unit-test suite: generate code, and if tests fail, feed the failure messages
back into the prompt so the model can retry while avoiding the same mistake.

This is a [multi-agent architecture](multi-agent-architecture.md) pattern even
when modules share a model family. Feed failure messages into the prompt so
retries avoid repeating mistakes — useless against irreversible side effects
(a sent email, an executed trade) unless paired with
[human approval gates](human-approval-gates.md) or sandboxes. Unlike
Self-Refine (single-generation iterate without lasting reflection memory) or
bare [self-critique prompting](self-critique-prompting.md), Reflexion persists
lessons across trials. Reflexion needs a do-over to be useful — it is the
inverse of [plan-and-solve prompting](plan-and-solve-prompting.md)'s upfront
planning, reviewing work *after the fact* instead, so it is valuable only
where retry is actually possible.

Like [ReAct](react-loop.md), it trades tokens and latency for higher success —
valuable when [compound mistake amplification](compound-mistake-amplification.md)
would otherwise silently accept a wrong "done" state (a
[planning failure mode](agent-planning-failure-modes.md)).

**When it helps:** On ALFWorld with a ReAct actor, heuristic or LLM binary
self-evaluation plus a 3-slot reflection buffer lifts completion near ceiling
across ~12 trials (ReAct-only plateaus early; hallucination about possessed
objects is largely eliminated by verbal "self-hints"). On HotPotQA, Reflexion
improves CoT/ReAct where temperature resampling alone never recovers first-
trial failures; an episodic-memory-only ablation (raw last trajectory without
verbal reflection) underperforms full self-reflection by ~8 absolute points.

**When it stalls:** WebShop-style tasks that need diverse exploration / escaping
local minima can yield unhelpful reflections with no improvement after a few
trials — terminate and redesign search affordances rather than stacking more
\(sr_t\). Self-correction also appears **emergent in stronger models**; weak
code models may show ~0 gain. Bound retries (for example stop after 3
consecutive failures on a task) and keep Evaluator heuristics cheap when the
environment only signals binary success.

**Programming grounding:** When the Actor writes code, prefer a
[self-generated test evaluator](self-generated-test-evaluator.md) so
pass/fail is executable rather than guessed. Ablations show test generation
and verbal self-reflection are **jointly** required — either alone fails to
beat the base sample. Watch [test suite fidelity](test-suite-fidelity.md)
(false-positive suites explain underperformance despite strong base models).
Run generated code in sandboxes; verbal reflections can also be monitored for
intent before tool use, improving interpretability relative to black-box RL.
