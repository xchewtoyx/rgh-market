---
type: concept
title: Self-Consistency Decoding
description: >
  Sample multiple independent CoT reasoning paths and marginalize to the most
  consistent final answer — a self-ensemble without a trained verifier.
sources:
  - title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    resource: "Self-Consistency (Wang et al.), pp. 1–24"
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    resource: "Tree of Thoughts (Yao et al.), pp. 1–14"
---

Self-consistency (Wang et al., 2023) replaces greedy decode on a single
[chain-of-thought](chain-of-thought-prompting.md) path with
**sample-and-marginalize**: prompt with CoT exemplars, sample \(m\) diverse
reasoning paths (temperature, top-\(k\), or nucleus), parse each into a path
\(r_i\) and final answer \(a_i\), then choose
\(\arg\max_a \sum_i \mathbf{1}(a_i = a)\) — unweighted majority vote over the
answer set. The intuition: complex problems admit many correct thinking
routes to one answer, so agreement across diverse paths raises confidence;
incorrect paths are less likely to converge on the same wrong \(a\).

**Aggregation choice:** majority vote ≈ length-normalized weighted sum of
generation probabilities; unnormalized path probability and per-answer
weighted averages do worse. Near-parity of majority and normalized weights
suggests the LM treats sampled solutions as similarly likely and is **poorly
calibrated** to rank correct over incorrect — which is why trained verifiers
and re-rankers exist, and why a label-free vote is attractive as a harness
knob.

**Scope:** works when finals come from a **fixed answer set** (math number,
commonsense string after “The answer is”). Open-text needs a separate
consistency metric. Unlike multi-model ensembles, it is a **self-ensemble** on
one frozen LM: no extra annotation, finetuning, or verifier — at the cost of
\(m\) generations.

Each chain still has no local exploration of alternative *steps* within a
trajectory. When intermediate decisions need lookahead or backtracking,
prefer [Tree of Thoughts](tree-of-thoughts.md) or another search harness over
flat CoT-SC. Cost scales with \(m\); start with **5–10 paths** — gains often
saturate quickly — and treat larger \(m\) as a quality–latency tradeoff
next to [branch-solve-merge](branch-solve-merge.md), which fans out candidates
but merges with a dedicated agent rather than voting finals.

**When it helps beyond greedy CoT:** Self-consistency can **recover** cases
where CoT alone *hurts* versus standard few-shot prompting on NLP tasks, and
it remains useful under imperfect or zero-shot CoT prompts. On PaLM 540B,
Zero-shot-CoT + SC (40 paths) closes much of the gap to Few-shot-CoT + SC on
GSM8K (70.1 vs 74.4) and lifts MultiArith to ~89 — so SC is a strong harness
knob when you want to avoid maintaining exemplar packs. Diversity of
reasoning paths is the active ingredient: sample-and-rank by log-prob, beam
search (which collapses diversity), prompt-order ensembles, and multi-model
majority votes all underperform same-budget SC on a single strong model
(weaker models drag stronger ones down). Robust across common \(T\) / top-\(k\)
/ nucleus settings; smaller models still improve but with smaller absolute
gains when skills have not emerged. Use agreement rate as a
[consistency-as-uncertainty signal](consistency-as-uncertainty-signal.md).
Use as an [offline prompt evaluation](offline-prompt-evaluation.md) lever when
comparing prompt variants under the same sampling budget.

**Scale and path-count evidence (Wang et al.):** Absolute gains over greedy CoT
grow with model scale (roughly +3–7 points on UL2-20B arithmetic vs +9–24 on
LaMDA-137B / GPT-3 code-davinci-001; PaLM-540B and code-davinci-002 still add
~+12–18 on hard math like GSM8K/AQuA despite already-strong CoT). Commonsense
and OOD symbolic tasks also rise, with smaller but reliable lifts at sufficient
scale. Accuracy rises as sampled paths go 1→5→10→20→40; more diverse paths
consistently help, and multi-path majority often recovers items where greedy
CoT alone fails via a different correct rationale. Prefer this knob on capable
models when the answer set is discrete — budget \(m\) under
[LLM model selection criteria](llm-model-selection-criteria.md) rather than
assuming a weak base will close the same gap.
