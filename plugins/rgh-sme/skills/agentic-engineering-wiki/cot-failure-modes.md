---
type: concept
title: CoT Failure Modes
description: >
  Categorize wrong chain-of-thought traces — logical mistakes, calculator
  errors, unnecessary steps, prior-knowledge gaps, or never starting to reason.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), Appendix B–C"
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), Appendix D.2"
---

When [offline prompt evaluation](offline-prompt-evaluation.md) shows CoT
regressions, classify traces before rewriting the whole prompt. Sample studies
(Kojima et al.; Wei et al. on GSM8K) yield a practical taxonomy:

- **Logical / plan mistakes** — wrong plan, extra unnecessary step,
  overcomplicated procedure (dominant on MultiArith for both zero-shot and
  few-shot CoT).
- **Calculator / arithmetic errors** — plan roughly right, numeric slip
  (some fixed by an
  [external calculator for CoT](external-calculator-for-cot.md); many co-occur
  with other errors).
- **Symbol mapping error** — correct structure, wrong number/symbol binding;
  often fixable by editing equations alone.
- **One step missing** — otherwise coherent chain skips a required hop.
- **Commonsense / semantic misunderstanding** — coherent logic that misses
  priors or misparses the ask (dominant on CommonsenseQA incorrects; large
  share of “needs substantial edit” GSM8K failures).
- **Never starts reasoning** — rephrases or answers without a step chain
  (especially under weak
  [reasoning triggers](reasoning-trigger-sensitivity.md)).
- **Indecision / multi-answer** — lists options; first listed may luckily match
  gold ([CoT path correctness gap](cot-path-correctness-gap.md)).

Outcome slices vs plain zero-shot also matter: on PaLM 540B GSM8K, CoT helps
where zero-shot fails often, but a non-trivial slice **hurts** (sometimes from
fragile formatting after the trigger). Prefer fixing the matching failure mode —
format cues and [answer cleansing](answer-cleansing.md) for extraction issues;
[self-consistency decoding](self-consistency-decoding.md) for calculator noise;
stronger models or retrieval for prior-knowledge gaps — rather than always
adding more exemplars. Compare Zero-shot-CoT vs Few-shot-CoT error mixes before
assuming demos will fix logical-plan failures.
