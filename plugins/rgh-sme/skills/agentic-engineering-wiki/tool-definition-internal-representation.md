---
type: concept
title: Tool Definition Internal Representation
description: >
  Native function calling is a fine-tuned chat model plus API-level syntactic
  sugar — tool defs render as TypeScript signatures, calls as ChatML-like tags.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

[Function calling](function-calling.md) is not a fundamentally different
mechanism from chat itself — like chat, it is a fine-tuned model plus
syntactic sugar at the API level. There is no official documentation of the
internal prompt format; it can be reconstructed by interrogating the model
(asking it to print text above the first message, wrapping interesting text in
custom tags and asking it to echo them back, or feeding partial hints as
assistant-voice text to encourage further disclosure).

For OpenAI's tool calling (as of the 2023 implementation), tool definitions
appear in the **system message** as **TypeScript function signatures**, not
JSON — e.g. a `set_room_temp` tool renders as a `namespace functions { type
set_room_temp = (_: { temp: number }) => any; }` block with comments carrying
the descriptions. The TypeScript framing is deliberate: it offers a richer
type vocabulary than JSON Schema, makes it easy to attach a description per
function and per argument, and forces the model to invoke with a JSON object
naming each argument (not positional), which improves call consistency and
reduces argument mix-ups — the model literally states the argument name right
before its value.

Tool invocation and response use special ChatML-like syntax internally, for
example an assistant turn addressed `to=functions.get_room_temp` followed by
the JSON arguments, and a `tool`-role turn carrying the return value back.
Tool-call IDs used to reassemble ordering exist only at the API layer, not in
this internal representation.

Token by token, the model is running a sequence of small classification
decisions: who speaks (forced by the harness), whether to call a tool versus
emit plain text, which tool, which argument to fill next, what value to give
it (looping over the last two for multiple arguments), then closing out. The
same underlying network implements several distinct, specialized inference
steps within a span of 10-20 tokens. This mechanistic view explains several
tool-definition guidelines: since tool defs are read as ordinary prompt text
by an otherwise-unmodified completion process, the same clarity and
[context engineering](context-engineering.md) principles that govern the rest
of the prompt govern tool definitions too.
