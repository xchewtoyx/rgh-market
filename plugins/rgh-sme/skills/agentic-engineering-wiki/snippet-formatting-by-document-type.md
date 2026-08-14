---
type: concept
title: Snippet Formatting by Document Type
description: >
  Format a retrieved data snippet to match the prompt's document type —
  conversation turn, report section, or serialized structure.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

How a snippet should be formatted depends on what kind of document the prompt
is impersonating:

- **Conversational transcript** — package retrieved data as a back-and-forth
  turn. A `weather = {"description": "sunny", "temperature": 75}` API result
  becomes something like "User: What's the weather like? Assistant: It's
  going to be sunny with a temperature of 75 degrees."
- **Analytic report** — state the knowledge in natural language, often as
  individual sections per API call or data source, e.g. a `#### Weather
  Forecast` heading followed by a sentence built from the returned fields.
- **Structured document** — usually simplest: serialize the object's relevant
  fields directly, e.g. as XML or JSON tags matching the surrounding
  document's format.

Across all document types, an explicit **side remark or aside** ("As an
aside, …") is a useful way to communicate background context without forcing
the model to use it in a particular way, or at all. Example from code
completion (where the document template is a source file): quoting a snippet
from another file inside a code comment explicitly labeled as included "for
comparison reasons," rather than pasted in as if it belonged to the file being
completed.

This is one input to [prompt assembly](prompt-assembly-algorithms.md); see
also [snippet formatting goals](snippet-formatting-goals.md) for the
properties a well-formatted snippet should have regardless of document type.
