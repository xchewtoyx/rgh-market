---
type: concept
title: Least-to-Most Prompting
description: >
  Decompose a hard problem into simpler subproblems and solve them in order,
  feeding each answer into the next prompt for easy-to-hard generalization.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 1–15"
---

Least-to-most prompting (Zhou et al.) targets a failure of
[chain of thought](chain-of-thought-prompting.md): easy-to-hard generalization
when test problems are harder than few-shot exemplars. Two few-shot stages, no
finetuning:

1. **Decomposition** — exemplars of how to split problems, then the new
   question to decompose.
2. **Subproblem solving** — exemplars of solving, plus previously answered
   subquestions and their solutions, then the next subquestion.

Append the **original problem as the final subproblem**. Solve sequentially:
after each answer, append it before prompting the next. Later subproblems are
literally facilitated by earlier answers in context — stronger than a flat
rationale that must invent all intermediates in one continuous generation.

Optional: merge both stages into one pass, or combine with CoT and
[self-consistency decoding](self-consistency-decoding.md). Related to
[task decomposition prompting](task-decomposition-prompting.md) and
[hierarchical planning](hierarchical-planning.md), but the distinctive claim is
*progressive* dependency: each solve step consumes prior solutions as working
memory, not only a static outline.

**Compositional generalization check:** With a single 2-step demonstration,
1-shot L2M and CoT look similar overall on GSM8K, but L2M’s relative edge
grows on items needing **more steps than the demo illustrated** (largest
gain on 5+ step items). When both methods get rich multi-example engineered
prompts whose demos already cover typical test complexity, overall L2M may
**not** beat CoT — use L2M when easy→hard step-count generalization is the
failure mode, not as a default accuracy booster. Keep separate decomposition
vs solving contexts when engineering; a merged one-pass 1-shot is fine for
simplicity ablations under
[offline prompt evaluation](offline-prompt-evaluation.md). Treat decomposition
exemplars as [domain-specific](domain-specific-decomposition-prompts.md) —
they rarely transfer across problem families.

**Symbolic / SCAN pattern:** Last-letter concatenation shows CoT collapsing
faster than L2M as list length exceeds exemplars; solution exemplars must
teach a **base case + recursive step that consumes the prior answer**, not
independent from-scratch rationales. SCAN length-split jumps to ~99.7% with
code-davinci-002 under L2M vs ~16% CoT — cover command semantics in mapping
exemplars and use compact intermediate IRs (for example Python `*`/`+`
expressions) when expanding action lists would blow the window. Write those
mapping demos as [compositional mapping exemplars](compositional-mapping-exemplars.md)
(name components → restate outputs → compose), not flat command→action pairs.
Expand compact IRs with [prompted IR expansion](prompted-ir-expansion.md) when
a dedicated executor is unavailable. DROP-style reading+arithmetic often gains
because questions are trivially decomposable; almost every GSM8K L2M failure is
solvable given a **correct manual decomposition** — invest in the decompose
stage first. See
[decomposition-before-composition failures](decomposition-before-composition-failures.md)
for CoT vs L2M error taxonomies on DROP, and
[compositional translation failure modes](compositional-translation-failure-modes.md)
for SCAN decompose-vs-translate buckets.

**Token-efficiency claim:** on last-letter concatenation, 2-shot L2M (~123
GPT-3 tokens of prompt) beats 8-shot CoT (~573 tokens) in accuracy, and the
gap widens with list length (L=12: 74.0% vs 38.4%) — L2M's per-token
data-efficiency, not only its final accuracy ceiling, is the case for
preferring it when prompt budget is scarce. A controlled check isolates *why*:
CoT run on the same two examples but presented **independently** (as flat,
unlinked rationales) outperforms CoT run on those same two examples in their
original **L2M-style dependent** form — so L2M's edge over CoT survives even
when both methods see identical demonstration content, meaning the gain comes
from the recursive step-consumes-prior-answer *structure*, not from the demos
containing extra information CoT's demos lacked.

**Error propagation in the solve chain:** L2M failures on last-letter
concatenation are dominated by **concatenation slips** (dropping, duplicating,
or reordering a letter mid-chain) rather than losing the recursive structure
itself — the base case + extension template stays intact even in wrong
answers. Because each step's prompt consumes the *literal prior output* rather
than re-deriving it, a slip at step *k* propagates unexamined into every later
step's context: the chain has no mechanism to notice or revisit an earlier
answer once it is fed forward, unlike a single flat CoT rationale where later
tokens can still attend back over the whole derivation. This is a structural
version of [compound mistake amplification](compound-mistake-amplification.md)
specific to incremental/recursive prompting methods — pair long solve chains
with [self-consistency decoding](self-consistency-decoding.md) across full
chains (not per-step) or a
[reflection](reflection-and-error-correction.md) pass that can revisit and
correct an earlier subanswer, since the decomposition step alone provides no
such self-correction.
