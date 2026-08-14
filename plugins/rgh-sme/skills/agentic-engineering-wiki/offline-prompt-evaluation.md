---
type: concept
title: Offline Prompt Evaluation
description: >
  Prototype and score prompt or task changes against proxies or LLM judges
  before shipping, exercising as much of the real feedforward path as possible.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 4"
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix E"
---

Because models are probabilistic, evaluate new prompts and harness changes
offline before users see them. Under
[eval-driven development](eval-driven-development.md), decide *what* to
measure with
[application evaluation criteria](application-evaluation-criteria.md)
(domain, generation, instruction-following, cost/latency) before wiring
proxies. Easy proxies exist when correctness is measurable (for example
regenerate deleted code fragments and check tests). Open-ended apps often
need **LLM-as-judge** — structure it with
[SOMA LLM assessment](soma-llm-assessment.md) rather than a bare “is this
correct?”. Prefer [gold-standard matching](gold-standard-matching.md) or
[functional completion testing](functional-completion-testing.md) when those
oracles exist. When a binary LLM judge is unavoidable (sorted lists,
paraphrase-heavy labels), constrain the judge to emit only `1`/`0` inside
fixed tags so scoring stays parseable for
[prompt optimization tooling](prompt-optimization-tooling.md) loops. Re-run
suites when prompts or providers move — GenAI exhibits
[radical fragility](genai-radical-fragility.md). A running suite also turns
model migration from a multi-week manual re-review into a fast, legible
decision: rerun it against the new release and read the pass-rate deltas,
rather than rebuilding that judgment from scratch by hand every time a model
ships.

Engage as much of the real [feedforward pass](llm-application-feedforward-pass.md) as
possible: mocking context gathering is sometimes necessary but risks missing
retrieval failures that dominate production quality. Start with an
[offline example suite](offline-example-suites.md) (eyeball diffs on 5–20
cases) before investing in automatic judges. Prefer
[per-task offline harness tests](per-task-offline-harness-tests.md) with I/O
examples once workflow tasks exist. Match test granularity to the change:
model swaps → broad regression; prompt/API knobs → single-pass units;
architecture/loop shape → whole-loop regression. Online telemetry and product
metrics for live drift belong to observability practice; the design obligation
here is having evalable contracts and harnesses you can run before release under
[harness drift awareness](harness-drift-awareness.md). Keep primary offline
metrics
[episode-shaped rather than request-APM](episode-scale-evaluation-vs-request-apm.md)
(resolve, phase failure, budget tails — not per-tool p99 alone).
