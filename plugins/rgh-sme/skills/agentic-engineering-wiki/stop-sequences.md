---
type: concept
title: Stop Sequences
description: >
  Halt generation at known end markers server-side (or cancel a stream) so
  postscripts never burn tokens after the extractable answer is complete.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

Once [completion boundary markers](completion-boundary-markers.md) define where
the useful answer ends, tell the API to stop there:

- **Stop sequences** — pass strings that terminate generation server-side when
  matched (OpenAI-style `stop`). No further tokens are billed. Prefer sequences
  that begin with a newline (e.g. `\n#`) so mid-line collisions (comments,
  phone numbers) do not false-trigger.
- **Streaming + cancel** — consume tokens until an end cue appears, then stop
  reading; cancellation saves some compute but lags the network, so it is
  weaker than true stop sequences. Use when the API lacks `stop` or ends are
  too varied for a fixed list.

Enhance either path with common continuation markers for the document type
(for a Python class: `\nclass`, `\ndef`, `\nif` at column 0 — indented
`\n\tdef` will not spuriously end the class). Pair with moving structural
boilerplate into the prompt under
[completion preamble types](completion-preamble-types.md) so generation starts
inside the extractable region.
