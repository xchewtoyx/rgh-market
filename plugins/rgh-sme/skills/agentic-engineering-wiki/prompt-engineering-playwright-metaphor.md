---
type: concept
title: Prompt Engineering Playwright Metaphor
description: >
  The visible user-assistant conversation and the actual model transcript
  differ — the transcript is a script with several collaborating authors.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 3"
---

A key source of confusion when building chat applications: the human user's
visible conversation with "the assistant" is not the same thing as the
application-to-model [ChatML](chatml-format.md) transcript actually sent as
the prompt. The transcript can contain information the human user never sees
— for example, when a user asks "How should I test this code?", the
application must infer what "this code" refers to and fabricate supporting
user or assistant turns containing the relevant code snippet before sending
the transcript onward.

A useful metaphor: a theatrical play, with characters, a script, and multiple
collaborating playwrights.

- **Characters** are the ChatML roles — user, assistant, system, tool (names
  vary by provider).
- **Script** is the prompt: the transcript of character interactions working
  toward solving the user's problem.
- **Playwrights**, plural, jointly write that script:
  1. *The prompt engineer* determines the overall prompt structure and
     boilerplate text — [system prompt architecture](system-prompt-architecture.md)
     and [prompt anatomy](prompt-anatomy.md).
  2. *The human user* introduces the focal problem or theme.
  3. *The model itself* fills in the assistant's speaking parts, though the
     prompt engineer may also pre-write portions of assistant dialogue via
     [inception](prompt-transition.md).
  4. *External APIs* supply additional injected content — a documentation
     search tool contributing retrieved passages, for instance, via
     [function calling](function-calling.md).

Extending the metaphor: the prompt engineer is the lead playwright and
showrunner, responsible for the overall shape and tone of the interaction —
not writing every line, but directing what kind of play gets performed and
keeping the other playwrights' contributions coherent with each other.
