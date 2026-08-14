---
type: concept
title: ChatML Injection Resistance
description: >
  Reserved role-marker tokens can't be produced by ordinary user text, so an
  API caller is structurally confined to the user role and cannot fake turns.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 3"
---

[ChatML](chatml-format.md)'s role-opening and role-closing markers are
reserved tokens that a user interacting through a chat API cannot generate.
If a user's supplied text literally contains the reserved marker string, it
gets tokenized as several ordinary sub-tokens instead of the single reserved
token — the tokenizer simply cannot produce that special token from
arbitrary input text. This makes it structurally impossible for an API caller
to sneak in a fake assistant or system message and hijack the conversation:
they are confined to the user role no matter what string they submit.

The chat completion API reinforces this at another layer: the JSON messages
array sent to the API contains no literal ChatML special tokens at all —
conversion into ChatML happens behind the API, so callers cannot inject the
reserved tokens even indirectly through the request format.

This structural protection has one important gap: **don't inject user content
into the system message.** Because the model closely follows the system
message under [instruction hierarchy](instruction-hierarchy.md), folding user
content — or any other externally sourced text, such as a fetched file — into
the system message defeats this protection entirely, since the content is now
inside the very message the model is conditioned to obey most. A file
containing "IGNORE EVERYTHING ABOVE AND [attacker instruction]" does nothing
dangerous sitting in a user message, but the same text folded into the system
message can override the actual system instructions. Keep externally sourced
and user-sourced content in the user role, or in a clearly demarcated tool
role, and reserve the system message for developer-authored text only — the
practical, harness-level complement to
[defensive prompt engineering](defensive-prompt-engineering.md)'s guidance to
treat all retrieved text as untrusted.
