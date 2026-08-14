---
type: concept
title: Agent Episode Prompt Stack
description: >
  Compose an agent episode as fixed system, optional demonstration, instance
  brief, then per-turn next-step templates around action and observation.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

An interactive agent episode is easier to reason about as a **prompt stack**
than as one growing blob. SWE-agent's default order:

1. **System** — fixed for every instance; never collapsed. Describes the
   environment, documents custom commands (usage + docstring each), and locks
   the response format (typically one thought plus one action per turn).
2. **Demonstration** — optional successful trajectory. Either inject each demo
   turn as separate history messages or wrap the whole demo in an explicit
   “this is a demonstration” frame; which representation helps is
   model-dependent. Demos mainly teach command *format* more than domain
   strategy when tasks are diverse.
3. **Instance** — the concrete task plus brief reinstruction, often with
   [failure-derived prompt tips](failure-derived-prompt-tips.md).
4. **Next step** — after each well-formed action, append observation (or an
   explicit silent-success message when stdout is empty) plus the shell/prompt
   cue for the next command.

The turn loop is LM inference → execute → next-step template, until submit,
budget exhaustion, or [action format enforcement](action-format-enforcement.md)
stops the episode. Keep system content instance-agnostic; put task text only in
the instance template so the stack stays reusable under
[system prompt architecture](system-prompt-architecture.md) and
[conversational agent context](conversational-agent-context.md).
