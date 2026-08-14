---
type: concept
title: Completion Boundary Markers
description: >
  Choose start and end cues so the harness can extract the main answer — prefer
  formats whose end-test is a simple substring when possible.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

Reliable extraction needs recognizable **start** and **end** markers around the
main answer (after any [completion preamble](completion-preamble-types.md)).
Common patterns:

| Structure | Start cue | End cue | Substring end-test? |
| --- | --- | --- | --- |
| Markdown sections | expected header | next header | Yes |
| Fenced code | ` ```lang\n` | ` ```\n` | Yes |
| Numbered list item 1 | `1.` | `2.` | Yes |
| YAML / JSON fields | expected key | indent or unescaped quote | Often no |
| Bracketed code blocks | opening `{` | matching `}` | No |
| Indent-based defs | header line | lower indent | No |

Sharpen weak ends in the prompt: for YAML, require lower indentation *plus*
the known next keyword so the end-check becomes a substring test. Start cues
filter introductions; end cues filter postscripts and enable early stop via
[stop sequences](stop-sequences.md) or stream cancellation — every extra token
costs latency and money.
