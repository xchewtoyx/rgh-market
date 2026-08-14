---
type: concept
title: Output Medium Transformation
description: >
  A completion is text by default, but transforming it into the right output
  medium — speech, a UI event, a diff — is part of closing the application loop.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

A model's completion is a blob of text. Sometimes that's the end product
directly (a simple chat reply), but closing the
[LLM application loop](llm-application-loop.md) — transforming the completion
back into the user's domain — often needs further work:

- **Structured extraction** — asking for output in a specific format (tabular
  data, a fixed schema) and parsing it out of the raw completion text.
- **Function calling** — the generated text represents a function call rather
  than a user-facing answer; the application executes the real action (look
  up flights, or something with real-world effect like purchasing tickets)
  and returns the result to the user in their domain. See
  [function calling](function-calling.md) for the mechanics.
- **Medium changes** — text-to-speech for phone-based assistants; UI events
  for applications with a complex interface; or even a presentation change
  within text itself, such as showing a code completion as a grayed-out
  inline suggestion accepted with a keystroke versus showing a code change as
  a colored diff.

Which transformation is right depends on where in the user's actual workflow
the output needs to land — text is the model's native output, but it is
rarely the application's actual deliverable.
