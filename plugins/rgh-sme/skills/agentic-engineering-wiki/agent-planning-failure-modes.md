---
type: concept
title: Agent Planning Failure Modes
description: >
  Plans fail via invalid tools, bad parameters, wrong values, unmet goals or
  constraints, or false success from broken reflection.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

Beyond general LLM failure modes, [LLM agents](llm-agent.md) fail in planning
in distinctive ways.

**Tool-use failures** (most common):

- **Invalid tool** — plan references something outside the
  [tool inventory](tool-inventory.md).
- **Valid tool, invalid parameters** — wrong arity or schema.
- **Valid tool, incorrect parameter values** — schema-valid but semantically
  wrong, including [argument hallucination](argument-hallucination.md) of
  placeholders never stated in conversation.

**Goal failure**: the plan does not solve the task, or violates constraints
(wrong destination, blown budget). Time is an often-overlooked constraint — a
late-but-correct grant proposal still fails. In long interactive episodes,
**Act-without-thought** trajectories often fail here by never decomposing the
goal into subgoals or by losing track of environment state — the failure mode
that sparse [ReAct](react-loop.md) thoughts are meant to cut. Knowledge-
intensive ReAct can still fail by **repeating** prior thoughts/actions without
choosing a new next step or exiting — a structural reasoning error that
greedy decoding exacerbates; treat loop detection and step-budget fallback
([internal–external knowledge routing](internal-external-knowledge-routing.md))
as harness guardrails. Trajectory audits also show **skipped prerequisites**
(Act cleaning without navigating to the sink; ReAct-IM believing an object is
already clean because the thought said “find a clean …”) and
**under-commitment** after retrieval (Finish NOT ENOUGH INFO when evidence
REFUTES). Wrong Thought scaffolds are as dangerous as missing Thoughts.

**Reflection-driven failure**: the agent wrongly believes it succeeded (assigns
40 of 50 people and insists it is done). Broken
[reflection](reflection-and-error-correction.md) stops retries early.

Mitigations are harness-level: clearer tool docs, simpler APIs, stronger
planners, [plan-validate-execute](plan-validate-execute.md), and datasets of
`(task, inventory)` pairs that measure valid-plan rate and per-flavor tool-call
error rates. Runtime tracing of these failures for production monitoring belongs
to observability practice; the design vocabulary above is what you build to
reduce them.
