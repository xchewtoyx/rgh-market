---
type: concept
title: Task I/O Schema Design
description: >
  Define each workflow task's input/output shape explicitly, and separately
  keep a clear-enough idea of how the task should be accomplished.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

In a [workflow build process](workflow-build-process.md), one task's output
becomes the next task's input, so each task's interface must be well-defined
before implementation: what information does the task need, what does it
produce, and is that I/O structured (with an explicit schema) or free text?

Example (a Shopify plug-in email-generation task): the input schema names
typed fields such as plug-in `name`, `concept`, `rationale`, and a `store_id`
used to retrieve store details; the output schema is just `subject_line` and
`body`, both text. Writing the schema down this concretely, before
implementation, is what lets the task be
[implemented and verified in isolation](workflow-build-process.md).

Beyond the I/O interface, you also need a reasonably clear idea of *how* the
task should be accomplished — not just "generate content" but, for example,
"a fun presentation of the concept designed to appeal to the owner based on
values and themes demonstrated on the store's website," which implies pulling
content from the web page plus conditioning prompts around it. This *how*
need not be as rigidly fixed as the I/O schema — content is easier to change
than an interface — but it should be well-enough defined that you're
confident the task is reasonable as scoped; otherwise you end up back at the
drawing board rearranging tasks or redesigning interfaces once implementation
reveals the task was underspecified. Prefer a non-LLM implementation when
traditional software suffices; see
[non-LLM task implementation](non-llm-task-implementation.md).

When a first-draft task is not thoughtful enough, escalate: tighten the
prompt, add [forced reasoning before tools](forced-reasoning-before-tools.md)
or chain-of-thought, then [Reflexion](reflexion.md) with format checks, unit
tests, or LLM-as-judge analysis before retry. For open-ended tasks, an
[Assistant–UserProxy pair](assistant-userproxy-pair.md) can supply the
conversational partner an expert agent needs. Evaluate each task in isolation
with [per-task offline harness tests](per-task-offline-harness-tests.md)
before debugging the whole graph.
