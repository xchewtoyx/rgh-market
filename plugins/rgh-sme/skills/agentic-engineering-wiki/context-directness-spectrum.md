---
type: concept
title: Context Directness Spectrum
description: >
  Classify context by how directly it comes from the user — their own words,
  indirect nearby sources, or boilerplate that only shapes the response.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

Context gathered during
[context retrieval](llm-application-feedforward-pass.md) varies in how
directly it comes from the user:

- **Most direct** — straight from the user: typed text in a help box, or the
  code block a user is currently editing.
- **Indirect** — from relevant nearby sources: searched documentation excerpts
  for a support request, or other open files/tabs that often contain relevant
  snippets for a coding assistant.
- **Least direct** — boilerplate text that shapes the response without coming
  from the user's specific situation at all, e.g. a top-of-prompt statement
  like "This is an IT support request. We do whatever it takes to help users
  solve their problems." Boilerplate introduces the general problem up front
  and later acts as glue connecting the more direct context fragments into a
  coherent document.

This directness axis is orthogonal to
[prompt element importance](prompt-element-importance.md) — the least direct
boilerplate is often also the highest-priority element, since it frames how
everything else should be read even though it says nothing specific about the
user's actual request.
