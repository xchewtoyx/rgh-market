---
type: concept
title: Valley of Meh
description: >
  The early-to-middle prompt region where in-context recency and lost-in-the-
  middle effects combine so context is used less effectively than at the edges.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 6"
---

Two placement effects stack in long prompts:

- **In-context learning recency** — information nearer the end of the prompt
  has more impact on the next tokens ([in-context learning](in-context-learning.md)).
- **[Lost in the middle](lost-in-the-middle.md)** — beginning and end are
  recalled more reliably than the stuffed middle.

Together they create a **Valley of Meh**: an early-to-middle band where context
is under-used. Depth and location vary by model, but every long prompt has one.
Mitigate by placing key, high-quality elements outside the valley, filtering for
conciseness under [context engineering](context-engineering.md), and using the
[sandwich technique](sandwich-technique.md) so the task is restated after the
context parade. There is no perfect fix — keep prompts short enough that the
valley cannot swallow the payload.
