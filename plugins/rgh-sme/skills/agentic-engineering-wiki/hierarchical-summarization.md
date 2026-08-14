---
type: concept
title: Hierarchical Summarization
description: >
  Summarize a corpus too large for the context window by dividing it into
  window-sized units, summarizing each, then recursively summarizing the
  summaries along natural structure.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Summarization handles context that's too large to include directly by zooming
out to a short synopsis, the opposite move from
[retrieval](retrieval-augmented-generation.md)'s zoom-in on the most relevant
snippets. But the context window is a hard limit on summarization too — a
source too large to fit can't be summarized in one pass either, which is
exactly the situation hierarchical summarization solves.

Divide and conquer: split the corpus into semantic units no longer than the
context window, summarize each unit, then summarize the list of summaries.
For very long or deeply nested texts, apply this recursively — summarize
chapters, then summarize the chapter summaries at the book level, then
summarize the book summaries into one final synopsis. Any naturally
hierarchical structure works the same way, e.g. a large codebase: summarize
files, then summarize up the directory tree level by level, echoing the same
recursive-split shape as [chunking strategy](chunking-strategy.md)'s
"section → paragraph → sentence" splits, just applied bottom-up instead of
top-down. Prefer natural groupings (chapters, sections, topics, authors,
projects): split along those borders and summarize exactly one group per
pass. If forced to split on an unnatural boundary, avoid unbalanced passes
where most of the text being summarized together comes from one section and
only a little from another — that imbalance degrades the resulting summary's
coverage of the smaller section.

**Cost rule of thumb**: as long as each summary is on average less than about
one-tenth the size of the text it summarizes, the total cost of
summarization — regardless of how many hierarchy levels deep it goes — stays
bounded by the total token count of the original text.

**The rumor problem**: each additional level of "summary of a summary of a
summary" carries its own chance of the model misunderstanding something, and
that misunderstanding compounds at later levels, like a game of telephone —
one chance of error at level 1, three chances by level 3. In practice this
chain usually isn't deep enough to matter much, as long as summarization
length isn't stinted at any one level.

Choose [task-specific summarization](task-specific-summarization.md) when the
downstream question is fixed; keep general summaries when the resulting
artifacts must be reused across tasks. Hierarchical summarization complements
[memory summarization](memory-summarization.md), which fights chat FIFO
pressure, but targets bulk corpora ahead of the
[feedforward pass](llm-application-feedforward-pass.md) rather than an ongoing conversation.
