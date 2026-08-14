---
type: concept
title: Seven Rules for Technical Documentation
description: >
  A compact checklist for any technical document — write for the reader,
  avoid repetition and ambiguity, use a standard organization, record
  rationale, keep it current without being exhaustive, and review it for
  fitness of purpose.
sources:
  - title: "Documenting Software Architectures: Views and Beyond"
    resource: "Documenting Software Architectures (Clements, Bachmann, Bass, Garlan), Prologue"
---

A short, general-purpose checklist for technical documentation, stated independently of any particular document type: **[write from the reader's point of view, not the author's](write-for-the-reader-not-the-writer.md)** — a document exists to be used, and its structure should follow what a reader needs to extract, not the order the writer discovered the material (see [the curse of knowledge and audience research](curse-of-knowledge-and-audience-research.md)). **Avoid unnecessary repetition** — the same fact stated in two places tends to drift out of sync as one copy gets updated and the other doesn't, creating a document that contradicts itself. **Avoid ambiguity** — explain notation, symbols, and conventions explicitly rather than assuming a reader will infer them the way the writer intends; an arrow, an icon, or a term that seems self-evident to the author is a common, entirely avoidable source of misreading.

**Use a standard organization** — a reader who has seen one document from a set (or one document of a given kind) should be able to predict where to find a given piece of information in the next one, which only works if the organization is consistent rather than reinvented per document. **Record rationale**, not just the resulting decision — a document that states what was decided without why is much harder to trust, extend, or safely revise later, because a future reader can't tell which parts of the decision are load-bearing and which were arbitrary. **Keep documentation current, but not necessarily exhaustive** — a shorter document that accurately reflects the current state is more valuable than a longer one that has drifted out of date in places, and completeness is not a virtue when it comes at the cost of currency (see [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md)). **Review documentation for fitness of purpose** before treating it as finished — see [reviewing documentation for fitness of purpose](reviewing-documentation-for-fitness-of-purpose.md) — checking not just that it's accurate but that it actually serves the tasks its intended readers need to do with it.
