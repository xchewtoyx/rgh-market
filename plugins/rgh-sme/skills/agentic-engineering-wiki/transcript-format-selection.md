---
type: concept
title: Transcript Format Selection
description: >
  Choose how a completion model's conversation transcript is written on the
  page — freeform, script-style, markerless, or structured tags.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Writing an [advice conversation document](advice-conversation-document.md) for
a completion model requires choosing a transcript format — nothing enforces
one the way a chat API's template would. Four formats, each addressing a
weakness of the previous:

- **Freeform text** — flexible for inserting content between quotes, but hard
  to assemble dynamically and reliably once there are many elements to
  interleave.
- **Transcript/script format** (`Me: …` / `Assistant: …`) — easy to assemble
  programmatically, but weaker for long or formatted elements, such as
  indented source code, which doesn't sit naturally after a speaker label.
- **Markerless format** — works well with formatted text and long pasted
  content (e.g. emails), but the model can struggle to track who is speaking,
  and the application can struggle to detect where the model's response ends.
- **Structured format** (e.g. XML-tagged turns, see
  [structured document format](structured-document-format.md)) — clearly
  indicates who is speaking and when they finish, at the cost of more
  scaffolding tokens per turn.

Nothing prevents the prompt engineer from writing the assistant's lines too —
an application of the same
[inception technique](prompt-transition.md) used to transition into an
answer: writing from the assistant's perspective, as if it had already asked
a clarifying question, frames the next real user turn as responding to that
question, and ensures the actual completion opens with an answer rather than
another round of clarification.
