---
type: concept
title: Conversational Agent Context
description: >
  Assemble preamble, prior conversation, and the current exchange — including
  tool call/response traces — into the transcript the agent sees each turn.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.1"
---

A conversational [LLM agent](llm-agent.md)'s prompt is usually a
transcript with three layers:

1. **Preamble** (system message) — behavior, available tools, optional few-shot
   tool-use examples ([system prompt architecture](system-prompt-architecture.md)).
2. **Prior conversation** — earlier user/assistant turns and any attached
   [conversation artifacts](conversation-artifacts.md); this is the working
   short-term memory the model needs beyond the latest request.
3. **Current exchange** — the new user message (plus artifacts), then zero or
   more application-inserted tool call and tool-response messages, ending when
   the assistant returns a user-visible reply. That reply is not part of *this*
   prompt; it becomes prior conversation for the next turn.

Worked example (travel assistant): a system preamble sets persona and date and
defines `get_flights`/`get_ticket_info` tools; prior conversation holds an
earlier flight query and a reply with an attached artifact listing two
flights; the current exchange has the user asking about ticket availability, a
`get_ticket_info` call/response, and a final summary reply.

The outer conversational loop appends user input, then repeatedly runs the
inner tool-resolution loop ([ReAct loop](react-loop.md) /
[function calling](function-calling.md)) until the last message is a genuine
assistant response without pending tool calls. Prior conversation is what lets
agents resolve references like "put it back where it started" without
re-asking for facts already observed.

Selection pressure: drop tools irrelevant to the current phase, truncate or
summarize prior turns after topic shifts
([memory management](memory-management.md)), and prefer elastic slices of large
artifacts over stuffing whole documents. Too much context confuses and burns
budget; too little starves the task — [context engineering](context-engineering.md)
discipline is evaluate against the domain, not a fixed recipe. For long-lived
personas and facts that must survive FIFO churn, adopt
[main-context sections](main-context-sections.md) so working context is not
just another transcript turn.
