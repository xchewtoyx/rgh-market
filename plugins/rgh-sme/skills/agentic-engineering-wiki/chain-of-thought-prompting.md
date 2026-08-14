---
type: concept
title: Chain-of-Thought Prompting
description: >
  Eliciting step-by-step natural-language reasoning before the final answer
  measurably improves multi-step task accuracy, because emitting the
  reasoning as visible text is the only way a model can build on its own
  intermediate insight.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 2"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    resource: "Tree of Thoughts (Yao et al.), pp. 1–14"
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 1–15"
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    resource: "Chain-of-Thought Prompting (Wei et al.), §1–§3; Appendix A"
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §2–§3"
---

Chain-of-thought (CoT) prompting (Wei et al., 2022) asks the model to think step
by step, nudging systematic problem solving. A **chain of thought** is a
coherent series of intermediate natural-language reasoning steps that lead to
the final output. The underlying problem it addresses: token-by-token
generation has no internal monologue, so a model asked for a direct yes/no
answer produces an intuitive guess first and only rationalizes it afterward.
This isn't just an emergent quirk — it follows from
[autoregressive generation](autoregressive-generation.md)'s architecture: a
model's reasoning depth within a single token is bounded by how many layers it
has, and the only way for a higher-layer insight to feed back into further
processing is for the model to emit it as an actual token first, which then
becomes input to the very next token's first layer. Thinking out loud into the
visible text is, mechanically, the *only* way the model gets to build on its
own intermediate insight. Few-shot CoT supplies exemplars as ⟨input, chain of
thought, output⟩ triples so later responses follow reason-then-answer order —
combining the strengths of NL rationales (without a large rationale
finetuning corpus) and [in-context learning](in-context-learning.md).
Conditioning the model this way shifts it into producing the reasoning first,
which in turn shifts the final answer. Reported gains: StrategyQA commonsense
accuracy rose from 69.4% to 75.6%, and GSM8K math word-problem solve rate rose
from roughly 20% to 60% (PaLM 540B).

The simplest form appends "think step by step" or "explain your rationale."
Zero-shot CoT (Kojima et al., 2022) drops CoT's curated few-shot examples
entirely and prefixes with a cue such as **"Let's think step-by-step"** — see
[zero-shot chain of thought](zero-shot-chain-of-thought.md) and
[two-stage reasoning–answer extraction](two-stage-reasoning-answer-extraction.md).
Stronger forms prescribe exact steps or give a one-shot worked example. Which
variant wins is application-dependent — see
[when chain of thought helps](when-chain-of-thought-helps.md) and
[scale-dependent chain of thought](scale-dependent-chain-of-thought.md). A
prompting-only approach matters for harnesses: one checkpoint can serve many
reasoning tasks without finetuning or losing generality, at the cost of
exemplar or trigger maintenance. Treat CoT as
[output-side reasoning augmentation](output-side-reasoning-augmentation.md) —
orthogonal to input-side instructions and few-shots.

CoT improves math and multi-step benchmarks and can reduce hallucinations, but
it raises perceived latency because intermediate reasoning precedes the
user-visible answer — and that pre-answer
[natural-language intermediate reasoning](natural-language-intermediate-reasoning.md)
is load-bearing, not decorative. Sampling several CoT chains and aggregating
finals is [self-consistency decoding](self-consistency-decoding.md); searching
alternative intermediate steps with lookahead and backtracking is
[Tree of Thoughts](tree-of-thoughts.md); decomposing into ordered subproblems
whose answers feed the next prompt is
[least-to-most prompting](least-to-most-prompting.md). Correct CoT traces also
give an interpretable debugging window into wrong paths (full characterization
of supporting computations remains open). In agents, "think step by step" is
task decomposition; it is not by itself a validated plan —
[world-model-augmented planning](world-model-augmented-planning.md) and
[plan-validate-execute](plan-validate-execute.md) still apply. For an explicit
plan-before-execute cue, see
[plan-and-solve prompting](plan-and-solve-prompting.md). Pair with
[self-critique prompting](self-critique-prompting.md) when the model should
verify after reasoning, or with [pause tokens](pause-tokens.md) for a
non-prompted way to buy the model extra computation before it answers.

Few-shot CoT is somewhat robust to annotator style, exemplar set, and count,
and exemplars need not match the test distribution — but large variance
remains (especially class-biased exemplar order on classification-like
tasks), and some tasks still need careful prompt engineering. Advantage over
standard prompting holds across small exemplar counts (Wei et al.: roughly
**1–8** shots on GSM8K, MultiArith, Sports, letter concat, coin flip) — start
lean, then add shots only if
[offline prompt evaluation](offline-prompt-evaluation.md) shows a gap. Gains
do not transfer perfectly across model families; always re-check. For
[CoT failure modes](cot-failure-modes.md) dominated by arithmetic slips,
prefer an [external calculator for CoT](external-calculator-for-cot.md) over
more exemplars alone.
