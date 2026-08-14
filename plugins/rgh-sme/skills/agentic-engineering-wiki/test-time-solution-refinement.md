---
type: concept
title: Test-Time Solution Refinement
description: >
  At inference, treat the current answer as an optimizable variable and iterate
  self-supervised LLM critiques via textual gradient descent before committing.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), §3.2; Appendix D"
---

**Test-time solution refinement** is [instance vs prompt optimization](instance-vs-prompt-optimization.md)
at inference: the variable is the candidate solution, the loss is an LLM
critique of question + solution (no ground truth), and updates use
[textual gradient descent](textual-gradient-descent.md). Typical loop:
zero_grad → self-supervised loss → backward → step for a few iterations, then
optionally [majority vote / self-consistency](self-consistency-decoding.md)
across refined solutions. Budget roughly **three LM calls per iteration**
(loss, gradient, update) on top of the initial solve. For code with unit tests,
specialize to [test-time code refinement](test-time-code-refinement.md).

Objective prompts often ask for critical investigation, reasons the prediction
could be wrong, and a **Janusian process** — consider alternative answers — kin
to [self-critique prompting](self-critique-prompting.md) and
[Reflexion](reflexion.md), but graph-structured. Align answer format with the
eval oracle: e.g. require last line `Answer: $LETTER` via
[natural-language optimizer constraints](natural-language-optimizer-constraints.md)
when scoring is string-match on ABCD. On GPQA Diamond / MMLU ML / College
Physics subsets, TextGrad’s few test-time updates improved already-strong
gpt-4o CoT baselines. Trade inference compute for quality when
[when chain of thought helps](when-chain-of-thought-helps.md) alone plateaus;
keep [optimization variable role descriptions](optimization-variable-role-description.md)
so reasoning is retained when desired.
