---
type: concept
title: Test-Time Code Refinement
description: >
  Treat candidate code as an instance-optimization variable scored by local
  tests plus an LLM evaluator that critiques failures without rewriting code.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), §3.1; Appendix C"
---

For coding agents, [test-time solution refinement](test-time-solution-refinement.md)
specializes to **code as the variable**. A typical TextGrad-style objective is:

`LLM(Problem + Code + Test-time Instruction + Local Test Results)`

Optimize the code under limited local-test supervision plus self-evaluation —
[instance vs prompt optimization](instance-vs-prompt-optimization.md) at
inference, not a shared prompt rewrite. The evaluator should explain each
failed test and surface harder edge cases, but
[critique–optimizer separation](critique-optimizer-separation.md) requires it
**not** to emit a full revised implementation; the TGD step applies
[textual gradients](textual-gradients.md) to produce the next code version.
Budget ~**three LM calls per iteration** (loss, gradient, update) on top of
codegen.

Control flow mirrors Reflexion-style coding loops: generate → run **local**
tests → if pass, submit to the real oracle (platform / CI); if fail, critique
and refine for a fixed iteration budget (often ~5). Do not treat local-pass as
final success when private tests exist. On LeetCode Hard (~39 problems) with
gpt-4o, zero-shot TextGrad beat a Reflexion re-run that used one demo — but
re-extracted datasets can differ across papers, so compare harnesses on the
**same** problem set. Related to [Reflexion](reflexion.md) but driven by
explicit [textual gradient descent](textual-gradient-descent.md) rather than
only episodic verbal memory. Score with
[functional completion testing](functional-completion-testing.md) rather than
trusting the critic alone.
