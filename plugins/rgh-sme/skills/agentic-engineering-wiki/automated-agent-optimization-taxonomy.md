---
type: concept
title: Automated Agent Optimization Taxonomy
description: >
  Classify automated agent-improvement methods by what evidence the optimizer
  observes and what surface it is allowed to edit, to see where full-harness
  evolution sits relative to single-surface methods.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §2"
---

Automated methods for improving an LLM agent without retraining the base model
form a spectrum, organized by two axes: **what evidence the optimizer
observes**, and **what surface it is allowed to edit**. Placing a method on
this map clarifies what kind of gain to expect from it and what it will miss:

- **Episodic critique / reflection** — observes the agent's own recent output
  or trajectory; edits nothing durable, only the next attempt's in-context
  state. [Reflexion](reflexion.md) and Self-Refine-style
  [self-critique prompting](self-critique-prompting.md) live here: fast,
  cheap, but the lesson does not automatically persist past the episode unless
  paired with [episodic reflection memory](episodic-reflection-memory.md).
- **Prompt / instruction optimization** — observes a batch of trajectories or
  labeled examples across many episodes; edits a single prompt-level surface
  (instructions, a natural-language playbook, or few-shot demonstrations).
  [TextGrad](textual-gradients.md)-style
  [prompt optimization tooling](prompt-optimization-tooling.md) and
  [DSPy](dspy-signature-abstraction.md) teleprompters live here, along with
  reflective playbook distillation and trajectory-feedback RL variants that
  reinforce successful tool sequences without touching tools or middleware
  themselves.
- **Program-structure editing** — observes trajectories the same way, but
  edits the *shape* of the system: a growing skill library, a scored archive
  of program variants under mutation, or a searched workflow graph. This is
  where a multi-component harness-evolution loop belongs — it jointly edits
  system prompt, tools, middleware, and long-term memory as a combinatorial
  whole, rather than one editable surface, so cross-component trade-offs
  become legible to the optimizer instead of hidden inside whichever surface
  happens to be editable.

The practical payoff of placing a method correctly: a method confined to the
prompt-optimization tier cannot fix a failure that only a tool-implementation
or middleware-level guard can close (see
[harness component-level selection](harness-component-level-selection.md)) —
no amount of instruction rewriting substitutes for an execution-time
intercept. Conversely, a full harness-evolution loop pays for that reach with
a larger, more heterogeneous action space and a harder attribution problem
(see [evidence-driven change manifest](evidence-driven-change-manifest.md)),
which is exactly the coordination cost prompt-only methods avoid by staying on
one surface.
