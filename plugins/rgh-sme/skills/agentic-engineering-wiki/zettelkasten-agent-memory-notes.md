---
type: concept
title: Zettelkasten Agent Memory Notes
description: >
  Turn each interaction into an LLM-authored structured note — keywords, tags,
  a contextual description, and an embedding — instead of storing it under a
  developer-predefined schema.
sources:
  - title: "A-Mem: Agentic Memory for LLM Agents"
    resource: "A-Mem (Xu et al.), §3.1, §4.3"
---

Most agent memory systems (see [memory management](memory-management.md))
require a developer to predefine memory storage structure up front — which
fields exist, where each new fact is filed, when retrieval fires. That works
until the agent encounters something the schema didn't anticipate: a novel
solution the fixed categories can't file anywhere new, forcing it into
whichever existing bucket is closest rather than the connections it actually
has.

**Zettelkasten-style agent memory notes** avoid predefining that structure by
having an LLM construct each memory note at write time. Each note is a
structured tuple — original content, timestamp, plus three LLM-generated
fields (keywords capturing key concepts, tags for categorization, and a
contextual description giving richer semantic framing than the raw content
alone) — with an embedding computed over all of it for similarity search.
Generating the semantic fields with an LLM rather than a fixed schema lets the
memory system extract implicit structure the raw interaction didn't state
explicitly, and the multi-faceted representation (content + keywords + tags +
description, not just a single summary) supports more nuanced retrieval later
than a flat embedding of the raw text alone would.

This is a different bet from
[structured agent memory](structured-agent-memory.md)'s developer-defined
tables and queues, and from a plain
[memory stream](memory-stream.md)'s append-only natural-language log: the
structure lives in per-note LLM-generated attributes decided at write time,
not in a schema fixed at design time. The note itself is only half the
picture — how a new note gets connected to existing ones is
[embedding-plus-LLM memory linking](embedding-plus-llm-memory-linking.md), and
what happens to those existing notes once connected is
[memory evolution on retrieval](memory-evolution-on-retrieval.md).

**Organization quality is bounded by the authoring LLM's own capability.**
Because the keywords, tags, and contextual description attached to each note
are themselves LLM-generated rather than derived from a fixed procedure, a
weaker model produces weaker organization — different LLMs can generate
meaningfully different descriptions or draw different connections from the
same underlying interaction. This is the cost side of trading a fixed schema
for LLM-authored structure: the fixed schema had firm data at the cost of
inflexibility, and letting an LLM decide structure trades that firmness for
whatever quality ceiling the authoring model itself has.

**This structure pays for itself in retrieval cost, not just organization
quality.** Because retrieval pulls a handful of compact, purpose-built notes
(keywords, tags, and a short contextual description) instead of dumping
large stretches of raw interaction history into context, one system reporting
both architectures found the structured-note approach needed roughly an
order of magnitude fewer tokens per memory operation than baselines that
retrieve closer to full raw context — a large enough gap to change whether
large-scale deployment is economically viable, not just a marginal
efficiency win.
