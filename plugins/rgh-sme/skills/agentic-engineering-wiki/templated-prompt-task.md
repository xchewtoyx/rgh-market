---
type: concept
title: Templated Prompt Task
description: >
  Implement a workflow task as a prompt template that fills inputs, elicits a
  completion, and post-processes the text into the task's output schema.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

A templated prompt task hydrates a task-specific template with upstream inputs,
runs the model, and parses the completion into the fields
[task I/O schema design](task-io-schema-design.md) requires — the "link"
style many orchestration libraries encourage. Before reaching for this
pattern, confirm the task actually needs an LLM at all — see
[non-LLM task implementation](non-llm-task-implementation.md).

Gather, rank, and trim context under [context engineering](context-engineering.md),
then assemble a document whose natural completion *is* the task output. A useful
framing is **prefix/suffix completion**: open with role and context sections,
start the desired artifact (for example `Dear {owner_name},`), and close with a
fixed sign-off so the completion body is exactly the extractable field — nothing
more. Iterate by clarifying tone and labeling interpolated blocks so the model
knows what it is reading.

Every templated task must post-process the completion for downstream consumers.
When the needed output is a rigid multi-field structure rather than prose, prefer
[forced tool-choice extraction](forced-tool-choice-extraction.md).
