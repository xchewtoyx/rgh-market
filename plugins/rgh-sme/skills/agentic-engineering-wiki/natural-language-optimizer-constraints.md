---
type: concept
title: Natural-Language Optimizer Constraints
description: >
  Append hard format or domain rules as natural-language constraint blocks to
  the textual optimizer so updates must satisfy them.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), §2 spillover; Appendix B"
---

When running [textual gradient descent](textual-gradient-descent.md), soft
critiques alone may break output contracts. TextGrad injects **constraints** as
natural-language postfixes inside `<CONSTRAINTS>…</CONSTRAINTS>` on the
optimizer prompt (e.g. force a final line `Answer: $LETTER` with
LETTER ∈ {A,B,C,D}). The API attaches constraint strings to the optimizer
alongside parameters.

Use this for harness invariants — answer formats, schema tags, safety
refusals — that [optimization variable role descriptions](optimization-variable-role-description.md)
alone do not enforce. Instruction-tuned models follow **simple** constraints
reliably; stacking too many drops compliance — prefer a short hard set over a
laundry list. Still verify with
[offline prompt evaluation](offline-prompt-evaluation.md); LLM optimizers can
ignore constraints under pressure. Pair with
[critique–optimizer separation](critique-optimizer-separation.md) so
constraints live on the rewrite step, not the critique engine.
