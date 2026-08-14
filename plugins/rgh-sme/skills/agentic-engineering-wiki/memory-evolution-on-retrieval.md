---
type: concept
title: Memory Evolution on Retrieval
description: >
  When a new memory links to existing neighbors, let those neighbors' own
  context, tags, and connections update in response, so the memory graph gets
  richer rather than merely bigger.
sources:
  - title: "A-Mem: Agentic Memory for LLM Agents"
    resource: "A-Mem (Xu et al.), §3.3"
---

**Where "agency" sits in a memory system is a design axis worth naming
explicitly.** [Active retrieval](active-retrieval-during-generation.md) and
similar agentic-RAG systems put agency in the *retrieval phase* — the model
autonomously decides when and what to fetch — while the underlying knowledge
base itself stays static once written. Memory evolution puts agency
somewhere else entirely: in *storage*, letting the memory structure itself
change shape as new experience arrives, independent of whether or how it's
later retrieved. A system can have either kind of agency without the other,
or both; they answer different questions ("what do I fetch right now?" vs.
"how should what I've already stored change in light of what just
happened?").

Most memory systems are write-once: a stored note stays exactly as written
until explicitly edited or evicted. **Memory evolution** breaks that
assumption for the notes touched by
[embedding-plus-LLM linking](embedding-plus-llm-memory-linking.md): after a
new memory's link set is computed, each neighbor note in that nearest-neighbor
set is itself passed back through an LLM — given the new note, its other
neighbors, and its own current content — to decide whether its context,
keywords, or tags should update, and the evolved version *replaces* the
original in the memory store.

The action space here is richer than a plain "update the summary": the
evolution step can choose to strengthen a connection, merge two notes, prune a
now-redundant one, and decide per neighbor whether to actually rewrite its
content or merely reinforce the new link without touching the text — not just
"leave unchanged" versus "overwrite."

The effect compounds over time: every new interaction can revise several
existing notes' framing, not just add one more note to the pile, so the
network's organization becomes progressively richer as new experience
interacts with old notes — closer to how encountering a new example can
sharpen how you remember several older, related examples, rather than simply
appending the new example to a list. Contrast this with
[episodic reflection memory](episodic-reflection-memory.md)'s fixed-size
buffer of self-contained lesson entries, which never rewrites earlier entries
in light of a later one — memory evolution is specifically the mechanism that
lets earlier notes change, not just the newest one get appended.
