---
type: concept
title: Compositional Mapping Exemplars
description: >
  Teach solve-stage few-shots to name component outputs and how they concatenate
  or repeat, so composition reuses simpler meanings instead of flat I/O pairs.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 16–30"
---

Under [least-to-most prompting](least-to-most-prompting.md), the **mapping /
solving** context is not the same as standard few-shot I/O. Standard SCAN-style
demos pair a command with a finished action string. Compositional mapping
demos instead:

1. Name which simpler commands’ outputs are concatenated or repeated.
2. Restate each component’s output.
3. Conclude the composed action (or other IR).

That framing trains reuse of previously demonstrated (or already-solved)
meanings — primitives, directional actions, repetition, conjunction, “after”,
opposite/around — rather than memorizing flat input→output rows. It is the
exemplar counterpart of feeding prior sub-answers into the next prompt: both
make intermediate results **explicit working memory** for composition.

When engineering L2M for symbolic or instruction-following domains, invest in
this solve-stage rhetoric separately from the decomposition context; compact
IRs (`+`, `*`, small expressions) keep composed answers short enough for
[context engineering](context-engineering.md) as nesting grows.
