---
type: concept
title: Domain-Capability Evaluation
description: >
  Measure whether a model understands the subject matter at all — usually
  via domain benchmarks — without mistaking multiple-choice discrimination
  for open-ended generation skill.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

[Application evaluation criteria](application-evaluation-criteria.md) put
**domain-specific capability** first: can the model handle the subject
(legal contracts, SQL, medicine, tool use) given its architecture, size, and
training data? A model never trained on Latin cannot understand Latin; no
amount of prompt craft invents missing domain knowledge. Evaluate via public
or private domain benchmarks (code generation/debugging, math, science,
legal knowledge, tool use, and thousands of others).

**Coding** usually scores on
[functional correctness](functional-testing-eval.md) (does the generated
program pass tests?), but efficiency (runtime, memory vs. a ground-truth
query — e.g. BIRD-SQL) and readability also matter. Readability has no
exact oracle and falls back to subjective or model-based
[graders](agent-grader-types.md).

**Non-coding domains** often use close-ended multiple-choice tasks because
they are easy to verify and reproduce — as of April 2024, roughly
three-quarters of EleutherAI lm-evaluation-harness tasks were MCQ (MMLU,
AGIEval, ARC-C); some authors deliberately exclude open-ended items to avoid
inconsistent assessment. Metrics are accuracy (and F1/precision/recall when
the choice set is a fixed classification label set). MCQs are popular
because they are cheap to create/verify and have a clear random baseline
(e.g. 25% for four options).

Two design traps when wiring domain benchmarks into a harness suite:

- **Presentation sensitivity.** MCQ scores move under trivial formatting
  changes — an extra space between question and answers, or adding the word
  `Choices:`, can flip model answers. Treat public leaderboard deltas as
  suspect unless prompting conditions match; this is the same hygiene
  [grader correctness](grader-correctness-as-eval-hygiene.md) demands for
  agent evals.
- **Discrimination vs generation.** MCQs test classifying good vs bad
  responses, not producing good ones. They suit knowledge/reasoning checks;
  they are a poor proxy for generation tasks like summarization, translation,
  or essay writing — those need
  [generation-capability evaluation](generation-capability-evaluation.md)
  instead.

Keep domain capability separate from
[instruction-following evaluation](instruction-following-evaluation.md): a
model can know the label space and still emit the wrong label strings when
asked.
