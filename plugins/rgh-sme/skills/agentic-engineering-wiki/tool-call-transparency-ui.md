---
type: concept
title: Tool-Call Transparency UI
description: >
  Surface an agent's background tool activity in the chat UI itself so users
  can inspect the rationale behind an unexpected response.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

The turn-taking chat UI has stayed essentially unchanged for decades; the
affordances that need to be added on top are specific to
[function calling](function-calling.md) agents:

1. **Processing spinner** — indicates the agent is working and a response is
   forthcoming.
2. **Tool-use indicator** — a small marker inside the agent's message (e.g. a
   pill button) signaling background tool activity is occurring or occurred.
3. **Tool-call detail view** — a "Tool calls" control revealing full details
   (tool name, arguments as a webform, results) so the user can inspect the
   rationale behind a response, especially when it's unexpected.

Detail-view visibility matters beyond UX polish: it is what makes
[editable tool-call correction](editable-tool-call-correction.md) possible,
and it gives users the same parameter-level view that
[human approval gates](human-approval-gates.md) recommend logging for
reviewers.
