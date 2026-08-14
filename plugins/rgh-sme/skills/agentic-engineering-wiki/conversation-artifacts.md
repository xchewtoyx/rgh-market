---
type: concept
title: Conversation Artifacts
description: >
  Structured data attached to transcript messages — UI selections, documents,
  or tool-derived lists — so the agent sees task context without copy/paste.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

An artifact is any relevant data block attached to a conversational turn — for
example, a list of available flights with dates/times/airports for an airline
assistant, the on-screen document a user is viewing, or a highlighted table.
The application should attach artifacts automatically from UI state (a user
highlighting or clicking something, or a prior
[function calling](function-calling.md) response) rather than forcing users to
paste them into chat.

Presentation choices under [conversational agent context](conversational-agent-context.md):

- **Which artifacts to present** — include all of them (best information, but
  risks confusing the model with irrelevant content) or have the model itself
  select relevant artifacts (more accurate, but needs an extra side-request
  and added complexity).
- **How to present artifacts** — embed in message content via a tagged block
  (for example `<artifact>`) or a markdown section (`## Attached Data`);
  format (JSON vs plain text) is secondary to clarity — test for the model
  and domain. If every artifact already came from a function call, don't
  treat it specially at all: keep the original tool call/response messages in
  prior conversation instead of re-attaching — those traces also serve as
  extra few-shot tool-use examples.
- **How much content per artifact** — for oversized sources, do not dump the
  full text: extract an [elastic snippet](elastic-snippets.md), offer a
  bulleted outline with on-demand detail tools, or expose a retrieval tool
  over the artifact ([RAG](retrieval-augmented-generation.md)).

At the UX layer, give users visibility into which artifacts the agent
currently has in view (especially implicitly-attached ones, like the
on-screen document a user is viewing) and a way to dismiss one if the agent
is focused on the wrong thing — this helps users ask more pointed questions
and keeps the conversation on track, and harness and product share this
control surface with [human approval gates](human-approval-gates.md) for
dangerous tools.
