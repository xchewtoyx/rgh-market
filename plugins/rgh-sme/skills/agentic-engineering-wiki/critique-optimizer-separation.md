---
type: concept
title: Critique–Optimizer Separation
description: >
  Keep the feedback engine to criticism only; let a separate optimizer step
  propose the next variable value — do not conflate diagnose and rewrite.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix A.3–A.4"
---

TextGrad’s LLMCall **backward** prompt instructs the model to act as a gradient
(feedback) engine: give intelligent criticism, **do not** invent a new variable
version, and skip feedback when the current value already works. The **TGD**
step then incorporates (possibly noisy) criticisms and must emit an improved
value inside explicit tags (e.g. `<IMPROVED_VARIABLE>…</IMPROVED_VARIABLE>`)
that replace the variable. The same rule appears in code evaluators: explain
each failed local test and harder edge cases, but **do not** provide a revised
implementation — leave rewriting to
[test-time code refinement](test-time-code-refinement.md)’s optimizer step.

This separation is a harness pattern for any
[textual gradients](textual-gradients.md) /
[reflection and error correction](reflection-and-error-correction.md) loop:
mixing “what’s wrong” and “here is the full rewrite” in one call conflates
diagnosis with proposal and makes failures harder to ablate. Keep critique
prompts stable across applications; specialize
[optimization variable role descriptions](optimization-variable-role-description.md)
and the optimizer prompt instead. Parse optimizer tags strictly — the same
discipline as [action format enforcement](action-format-enforcement.md).
