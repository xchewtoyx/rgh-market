---
type: concept
title: Decomposition Before Composition Failures
description: >
  Least-to-most fails when subquestions are nonsensical or when a sub-answer is
  wrong; CoT often fails earlier by picking the wrong fact or operator.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 46–60 (§9)"
---

When comparing [least-to-most prompting](least-to-most-prompting.md) to
[chain of thought](chain-of-thought-prompting.md) on reading+arithmetic
(DROP), CoT-only failures often come from **wrong operators**, latching onto
**irrelevant passage facts**, or **mis-extracting** entities — L2M’s explicit
subquestions force the needed lookups before composition. L2M’s own error
mass is different: sampled failures are mostly **wrong solving of a
subproblem**, then fewer **bad or absent decompositions** (rephrasing the
same question is not a split), with occasional **label noise**.

Design implication: invest first in decomposition exemplars that name
prerequisite facts; then audit solving exemplars that consume prior
sub-answers. If almost every failure becomes solvable under a manual correct
decomposition, the decompose stage is the bottleneck — not the final
arithmetic. Keep CoT ablations to measure whether composition alone would
have chosen the wrong intermediate. Use these categories in
[offline prompt evaluation](offline-prompt-evaluation.md) rather than only
end accuracy. For symbolic composition (SCAN), residual errors often shift to
operator algebra after decompose is solved — see
[compositional translation failure modes](compositional-translation-failure-modes.md).
