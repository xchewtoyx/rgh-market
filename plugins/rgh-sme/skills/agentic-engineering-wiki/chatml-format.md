---
type: concept
title: ChatML Format
description: >
  A markup language tagging conversation turns with roles — system, user,
  assistant — that chat models are fine-tuned to complete unambiguously.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 3"
---

Before chat models, **instruct models** were trained to treat every prompt as
a request to answer rather than a document to continue — but a bare instruct
prompt still carries no explicit signal for *whose turn it is*, and mixing
completion-style samples back into training (to offset the alignment tax of
instruction tuning) directly undermined how reliably the model could
recognize instruct mode at all. ChatML solves this by making the turn
structure explicit in the document itself: a simple markup annotating a
conversation as alternating messages tagged with roles — `system`, `user`, or
`assistant`. Every message opens with a role marker and closes with a
matching end token; a typical transcript interleaves a system message with
alternating user and assistant turns.

The **system message** isn't part of the dialogue — it sets expectations for
the assistant's behavior and character, typically addressing the assistant in
the second person (e.g. "You are a software assistant who provides concise
answers to coding questions"). This is the concrete rendering underneath
[system prompt architecture](system-prompt-architecture.md)'s abstract
system/user split: chat models are RLHF finetuned specifically to complete
ChatML-annotated transcripts, which gives three benefits over a bare instruct
prompt:

1. **An unambiguous pattern of communication** — the closing token after a
   user's message signals their turn is over, and the harness injects the
   assistant's opening marker to force a response, removing any doubt about
   whether the model should answer or elaborate.
2. **Strict obedience to the system message** — the model is conditioned to
   follow system-message constraints (e.g. "answer in one sentence") closely;
   removing such a constraint noticeably changes verbosity. This is the
   mechanism [instruction hierarchy](instruction-hierarchy.md) formalizes as
   system-prompt privilege.
3. **Structural resistance to impersonating other roles** — see
   [ChatML injection resistance](chatml-injection-resistance.md).

Function/tool calling extends the same idea further: the transcript's "document" gains
special syntax for invoking tools and incorporating their results, but the
model is still just completing a document — now a transcript, possibly with
tool syntax, rather than a raw ChatML conversation alone. See
[tool definition internal representation](tool-definition-internal-representation.md).
