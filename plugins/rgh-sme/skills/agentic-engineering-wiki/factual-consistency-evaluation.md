---
type: concept
title: Factual Consistency Evaluation
description: >
  Check whether generated claims are supported by a scoped context (local) or
  by world knowledge (global), using judges, self-consistency, search
  augmentation, or textual entailment — not fluency alone.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

[Hallucination](hallucination.md) is a generation property;
**factual-consistency evaluation** is the offline check that catches it.
Split the check by what the output is allowed to depend on:

- **Local factual consistency** — every claim must be supported by a given
  context (source document, company policy, retrieved passages, tabular
  data). Natural for summarization, support chatbots, and
  [retrieval-augmented generation](retrieval-augmented-generation.md): the
  context is explicit, so verification is tractable.
- **Global factual consistency** — claims are checked against open-world
  knowledge. Natural for general chat, fact-checking, and market research.
  Harder: you must first establish what the facts are, and contested claims
  have no single oracle. Absence of evidence is not disproof — search
  judges that overweight page *relevance* while ignoring human stylistic
  cues (citations, neutral tone) will mis-score.

Prefer local checks whenever the application has a scoped context; reserve
global checks for products that genuinely answer open-world questions.
Focus benchmarks on *where* the model hallucinates: niche knowledge
(under-referenced entities) and queries about things that do not exist
("What did X say about Y?" when X never addressed Y) are especially
prone.

Verification methods when context is available (user-supplied or retrieved):

- **AI-as-judge** — a separate model scores whether the output invents
  unsupported facts. Structured judge prompts beat prior heuristics on
  factual consistency; fine-tuned judges (e.g. TruthfulQA's GPT-judge) can
  approach human truthfulness labels. Build the judge under
  [SOMA](soma-assessment-technique.md) /
  [agent grader types](agent-grader-types.md) and calibrate it with
  [grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md).
  TruthfulQA (817 misconception-prone questions across 38 categories) is a
  reusable global-consistency suite with that judge attached.
- **Self-verification (SelfCheckGPT-style)** — sample N fresh responses; if
  they disagree with the original response R, treat R as likely
  hallucinated. Effective but expensive (many extra model calls per eval
  item). Related to
  [consistency as uncertainty signal](consistency-as-uncertainty-signal.md).
- **Knowledge-augmented verification (SAFE-style)** — decompose the response
  into self-contained statements, propose search queries per statement, and
  judge each against retrieved evidence. Stronger for long-form global
  checks; still depends on search quality.
- **Textual entailment (NLI)** — given premise (context) and hypothesis
  (claim), classify Entailment / Contradiction / Neutral. Entailment means
  consistent, contradiction inconsistent, neutral undetermined. Specialized
  entailment scorers can run cheaper than frontier judges when the premise
  is short and explicit.

Wire local factual consistency into RAG and grounded-answer suites alongside
[research agent eval groundedness](research-agent-eval-groundedness.md) and
[citation-backed agent answers](citation-backed-agent-answers.md). It is the
generation-bucket check under
[application evaluation criteria](application-evaluation-criteria.md) that
most often decides whether a retrieval-heavy harness is actually safe to
ship.
