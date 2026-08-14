---
type: concept
title: Context Grounding
description: >
  Supply the information the model needs in-prompt, and when required restrict
  answers to that context so parametric knowledge cannot leak through.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    resource: "RAG (Lewis et al.), §1"
---

Sufficient context helps models the way reference texts help students. Including
the source material for a question improves answers and reduces
[hallucination](hallucination.md): without needed facts, the model falls back
on unreliable parametric knowledge. Context may be supplied directly or
gathered via tools (retrieval, search) — [agent tool categories](agent-tool-categories.md)
call this knowledge augmentation. Hybrid
[retrieval-augmented generation](retrieval-augmented-generation.md) makes that
non-parametric memory **inspectable**: retrieved passages are provenance for
what the generator used, and the index can be swapped when facts change —
neither is available when knowledge lives only in weights.

Restricting a model to *only* provided context is harder. Clear instructions
("answer using only the provided context"), examples of unanswerable questions,
and asking the model to quote its source help — but prompting alone gives no
guarantee. Finetuning and exclusive training on the permitted corpus are stronger
and often infeasible. Place critical grounding material with
[lost in the middle](lost-in-the-middle.md) in mind.
