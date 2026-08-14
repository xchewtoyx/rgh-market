---
type: concept
title: Elastic Snippets
description: >
  Represent one piece of retrieved content at several sizes so prompt
  assembly can fit the largest version the remaining budget allows.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 6"
---

Normally one piece of content maps to one snippet, but content can sometimes
be split into multiple snippets or represented in multiple forms of varying
size. For example, a literary-analysis question about a specific scene needs
the relevant passages [retrieved](retrieval-augmented-generation.md) and
snippetized — but given two key retrieved moments, you could present them as
two bare snippets with no surrounding context (shortest), two snippets each
with some surrounding context (middle ground), or one combined snippet with
context linking the parts together (conveys the most, including how the two
moments relate).

Two general approaches to handling this variable-size situation:

1. **Elastic prompt elements** — a single element with multiple versions
   ranging from short to long (e.g. longest = the whole chapter, progressively
   shorter versions replace paragraphs with "…", down to just the two quoted
   snippets separated by "…"). At assembly time the question shifts from "do
   we have space for this snippet?" to "what's the biggest version of this
   snippet we have space for?"
2. **Multiple overlapping prompt elements** — separate elements (the passage
   alone; the passage plus some context; the passage plus more context) of
   which only one may actually be included. This requires the
   [prompt assembly](prompt-assembly-algorithms.md) method to support
   declaring elements as pairwise incompatible under
   [prompt element dependency](prompt-element-dependency.md); include
   the longest that fits, else fall back.

See [prompt compression budget allocation](prompt-compression-budget-allocation.md)
for a different level of the same problem: instead of choosing which whole
size of one item fits, it decides how much compression each prompt *role*
(instructions, question, demonstrations) is allowed before individual item
sizes are even considered — the two can be combined.

This is the same slice-the-large-source-down problem
[conversational agent context](conversational-agent-context.md)
names for attached [artifacts](conversation-artifacts.md) — a large source that
won't fit in full needs a strategy for choosing how much of it to include,
rather than an all-or-nothing decision. It is the general form of elastic
[conversation artifacts](conversation-artifacts.md) and progressive
disclosure for large sources: spend tokens on the best
[snippet formatting](snippet-formatting-goals.md) the budget allows without
dumping the whole document into the [Valley of Meh](valley-of-meh.md).
