---
type: concept
title: Last-Minute Context Trimming
description: >
  When assembled context still doesn't fit the token budget, shrink what's
  already selected — elide less-relevant lines or summarize — rather than
  dropping snippets outright.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

During [prompt assembly](llm-application-feedforward-pass.md), a document can
still be over budget even after only relevant snippets were selected. Two
last-minute space-saving techniques handle this without discarding an
otherwise-relevant source entirely:

- **Eliding** — remove less relevant lines from within an otherwise-relevant
  document, e.g. cutting unrelated functions out of a code file while keeping
  the ones that matter.
- **Summarization** — condense a long document down to its essential content
  for long sources that can't be trimmed line by line without losing
  coherence.

This is the assembly-time counterpart to
[memory summarization](memory-summarization.md), which applies the same
compress-rather-than-discard idea specifically to conversational short-term
memory; here it applies to any oversized piece of selected context, such as a
retrieved document or code file. Either technique should preserve the
document's plausibility as a whole, per the
[Little Red Riding Hood principle](little-red-riding-hood-principle.md) —
elided or summarized text should still read as a coherent document, not as
visibly mangled input. This readability requirement is a deliberate choice,
not a technical necessity: when the compressed text will only ever be read
by the LLM itself, not a human,
[perplexity-based prompt compression](perplexity-based-prompt-compression.md)
trades that readability away for a much higher compression ratio.
