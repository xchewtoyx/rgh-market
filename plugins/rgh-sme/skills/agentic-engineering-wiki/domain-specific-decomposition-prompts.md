---
type: concept
title: Domain-Specific Decomposition Prompts
description: >
  Decomposition few-shots rarely transfer across domains — invest in
  within-domain demos because a correct split usually decides success.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 1–15"
---

[Least-to-most prompting](least-to-most-prompting.md) needs a **decomposition
context** tuned to the domain. A math-word decomposition demo does not teach
the model to break down common-sense questions like “Did Aristotle use a
laptop?” — a new decomposition prompt is required for optimal performance.
Even **within** a domain, decomposition generalization is hard: nearly all
GSM8K L2M failures become solvable given a correct manual split.

Implication for harness design: treat decompose-stage exemplars as first-class
artifacts under [offline prompt evaluation](offline-prompt-evaluation.md), not
as one universal “how to split problems” preamble. Symbolic wins (SCAN,
last-letter) partly reflect *easy* decomposition; do not assume those rates
transfer to domains where inventing subproblems is the hard part. Pair with
[compositional mapping exemplars](compositional-mapping-exemplars.md) for the
solve stage once the split is reliable.
