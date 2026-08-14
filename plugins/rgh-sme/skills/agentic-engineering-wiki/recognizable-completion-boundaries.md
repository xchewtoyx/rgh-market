---
type: concept
title: Recognizable Completion Boundaries
description: >
  Reliably extracting the answer from a completion needs a known start marker
  and a known end marker specific to the document format being generated.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

To reliably extract the main answer out of a completion — past any
[preamble](completion-preamble-types.md) and before any trailing fluff — the
harness needs recognizable start and end boundaries specific to the document
format in use:

| Document structure | Start | End | End test = substring test? |
|---|---|---|---|
| Markdown document | expected section header | any other section header | Yes |
| YAML document | expected keyword after a newline | line with lower indentation | No |
| JSON document | expected keyword in quotes, colon, quote | any unescaped quotation mark | No |
| Triple-ticked code listing | ` ```[language]\n` | ` ```\n` | Yes |
| Numbered list, first item | `1.` | `2.` | Yes |
| Function/class, bracketed language (e.g. Java) | opening bracket | matching closing bracket | No |
| Function/class, indent language (e.g. Python) | expected function/class header | lower indentation level (except an occasional terrible string literal) | No |

A well-crafted prompt can sharpen these boundaries further. For example, in
YAML, if the next expected keyword is known ahead of time, look for lower
indentation *followed by that keyword* rather than any lower indentation —
turning an otherwise unreliable structural check into a reliable substring
test.

Recognizing the start lets the harness filter out an irrelevant introduction;
recognizing the end lets it filter a fluffy postscript and, more importantly,
[stop generation early](completion-stop-condition-design.md) — every
generated token past the answer costs time and compute for nothing.
