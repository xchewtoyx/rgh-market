---
type: concept
title: Prompt Engineer as Playwright
description: >
  Treat the model-facing transcript as a script you author — roles, injected
  turns, and tools — distinct from the human’s visible conversation.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 3"
---

In chat apps, the human↔assistant dialogue is **not** identical to the
application↔model transcript. The harness may fabricate supporting user or
assistant turns (highlighted code the user never typed, retrieved docs) before
the model replies. Berryman’s metaphor:

- **Characters** — ChatML roles (`system`, `user`, `assistant`, `tool`).
- **Script** — the assembled prompt working the user’s problem.
- **Playwrights** — prompt engineer (structure/boilerplate), human user
  (theme), LLM (assistant lines), and external APIs (injected content).

The prompt engineer is lead playwright / showrunner: shape tone and
information flow so the model sees a coherent document under
[system prompt architecture](system-prompt-architecture.md) and
[conversational agent context](conversational-agent-context.md). Never confuse
“what the user said” with “what the model must see.”
