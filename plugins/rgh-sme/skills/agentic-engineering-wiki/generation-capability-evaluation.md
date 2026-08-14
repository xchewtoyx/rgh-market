---
type: concept
title: Generation-Capability Evaluation
description: >
  For strong models, de-emphasize fluency and coherence checks and invest
  evaluation budget in factual consistency and safety — the generation
  failures that still ship as user-visible harm.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

The **generation** bucket of
[application evaluation criteria](application-evaluation-criteria.md) asks
whether the model produces usable natural-language output, not whether it
knows the domain or obeys format instructions.

Classic NLG metrics — **fluency** (grammatical, natural-sounding) and
**coherence** (logical structure), plus task-specific axes like faithfulness
for translation and relevance for summarization — mattered when models
routinely produced broken prose. For strong foundation models those axes are
usually near-saturated: they remain useful for weak models, creative
writing, and low-resource languages, and they can still be scored with
model-based judges or perplexity, but they rarely decide a modern shipping
decision.

What does decide it:

- **[Factual consistency](factual-consistency-evaluation.md)** — undesired
  [hallucination](hallucination.md); local (against provided context) vs
  global (against world knowledge). Critical for RAG and any grounded
  answer product.
- **Safety** — whether outputs contain disallowed content. Treat safety as
  an offline eval criterion with an explicit taxonomy and detectors, not as
  an afterthought filter: inappropriate language; harmful advice or
  tutorials; hate speech; violence; stereotypes; political/religious
  ideological skew. Detection options range from prompted general-purpose
  judges, through provider moderation endpoints, to specialized
  cheaper toxicity classifiers transferable from human to model text.
  Benchmarks such as RealToxicityPrompts and BOLD exercise open-ended
  toxicity and bias. In the harness, pair these evals with
  [input/output guardrails](input-output-guardrails.md) so failures caught
  offline also have a runtime policy — but keep the offline suite as the
  contract you regress against under
  [eval-driven development](eval-driven-development.md).

Teams may add product-specific generation axes (controversiality for a
writing assistant; friendliness, positivity, creativity, conciseness) —
encode those as named graders in the same bucket rather than folding them
into a single "quality" score. Keep generation checks distinct from
[domain-capability evaluation](domain-capability-evaluation.md) and
[instruction-following evaluation](instruction-following-evaluation.md) so a
fluent, on-topic answer that violates format or invents facts still fails
the right criterion.
