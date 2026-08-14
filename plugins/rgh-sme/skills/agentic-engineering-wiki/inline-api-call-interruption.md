---
type: concept
title: Inline API Call Interruption
description: >
  Decode until the model emits a call-result delimiter, pause generation,
  inject the tool response, then continue decoding in the same sequence.
sources:
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

Inline API call interruption is an inference harness pattern: represent a tool
invocation as text inside the generation stream (for example
`<API> name(args) → result </API>`, or vocabulary-safe stand-ins like
`[` / `]` / `->`), decode until the model emits the result delimiter, **pause**,
execute the named API, insert the textual response plus the closing token, and
resume decoding.

Unlike turn-based [function calling](function-calling.md) that appends separate
tool-role messages, interruption keeps call and result contiguous in one
left-to-right sequence — the shape
[self-supervised tool annotation](self-supervised-tool-annotation.md) finetunes
toward. Requirements: reliable parse of call spans, timeouts and error strings
that the model can continue from, and refusal to execute unknown APIs. Use when
tools must appear as ordinary next-token decisions inside free text; prefer
native function calling when the provider already guarantees structured call
messages and multi-tool batching.
