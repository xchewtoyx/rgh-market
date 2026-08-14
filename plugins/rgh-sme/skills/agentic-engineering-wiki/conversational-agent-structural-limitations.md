---
type: concept
title: Conversational Agent Structural Limitations
description: >
  Conversational agents lack a built-in mechanism for processing discrete work
  units and no enforceable lever over how a task gets done, unlike a workflow.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

Simply adding tools and a narrower system message to a conversational
[LLM agent](llm-agent.md) does not, by itself, make it fit for a complicated
multi-step workstream (a case study: an agent tasked end-to-end with
generating and emailing marketing plug-in pitches to Shopify storefronts
produced a naive web search, terse pitches, and a form-letter email that
literally included the placeholder `[your_name]`). Two structural reasons this
keeps happening as you add more instructions and tools, rather than being
fixable purely by writing a better prompt:

- **No natural mechanism for processing units of work.** A conversational
  agent has no built-in notion of a discrete work item — feeding all the work
  in at once tends to produce disaster, and processing it one item at a time
  requires building a queue around the agent. At that point you are already
  building something more structured than a conversational agent — you have
  started building a [workflow](workflow-build-process.md).
- **No clean lever over *how* work gets done.** The agent has freedom in how
  it accomplishes each piece of work, so when something fails there is no
  precise place to intervene and fix it — the system message is, in practice,
  a strong suggestion and nothing more.

Growing the system message to address every observed failure mode also grows
the base prompt, leaving the agent distracted and confused as the task
lengthens — trading further
[generality for strength](generality-strength-tradeoff.md) has diminishing,
even negative, returns past a point. The fix is architectural, not prompt
tuning: isolate each step of the task into its own specialized, independently
verifiable task ([task I/O schema design](task-io-schema-design.md)), and
assemble the set of tasks into a workflow rather than one increasingly
overloaded conversational agent.
