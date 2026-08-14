---
type: concept
title: Prompt Anatomy
description: >
  A working prompt usually combines a task description, optional examples, and
  the concrete task, with placement tuned per model.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 6"
---

Most effective prompts combine three parts:

1. **Task description** — what to do, including persona/role and output format
   (usually [static content](static-vs-dynamic-prompt-content.md)).
2. **Example(s)** — few-shot demonstrations of the desired behaviour
   ([in-context learning](in-context-learning.md)).
3. **The task** — the concrete question or request, plus
   [dynamic](static-vs-dynamic-prompt-content.md) instance context.

Many APIs map the description to a [system prompt](system-prompt-architecture.md)
and the task to a user prompt. Placement of the description matters: some models
prefer it at the start, others at the end — experiment per model. Structure the
three parts for clarity rather than stuffing everything into one undifferentiated
blob; that is the scaffold [prompt engineering](prompt-engineering.md) builds on.

Berryman's document-oriented framing adds placement roles along the same spine:
an **introduction** that names the document type and early focus (models have a
fixed per-token thought budget — guide attention early), a middle parade of
context elements (concise; avoid drowning in the [Valley of Meh](valley-of-meh.md)),
a [sandwich technique](sandwich-technique.md) **refocus**, and a
[prompt transition](prompt-transition.md) into the completion. Prefer crisp
elements; end elements on newlines when natural to simplify assembly and length
math under [context engineering](context-engineering.md).
