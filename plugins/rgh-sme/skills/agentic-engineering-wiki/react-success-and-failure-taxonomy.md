---
type: concept
title: ReAct Success and Failure Taxonomy
description: >
  Audit interleaved reason–act trajectories as true/false positives plus
  reasoning, search, hallucination, and label-ambiguity failures — not only EM.
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 31–33 (Appendix E.1); §3.3"
---

When evaluating [ReAct](react-loop.md) versus
[chain of thought](chain-of-thought-prompting.md) on multi-hop QA, end-task
accuracy hides qualitatively different episodes. Tag trajectories with:

| Bucket | What it looks like |
| --- | --- |
| **True positive** | Correct answer with grounded hops (ReAct) or sound internal steps (CoT). |
| **False positive** | EM-correct answer via wrong entities, invented years, or broken comparisons. |
| **Reasoning error** | Bloated/inefficient plans (search every cast member) or inverted inequalities. |
| **Search error** | Bad query → empty/off-topic hits; recovery is reformulating the query. |
| **Hallucination** | CoT-style fabricated fact with no evidence (e.g. wrong journal year). |
| **Label ambiguity** | Reasonable answer mismatches a longer or dual-citizenship gold string. |

Design implications: score with this taxonomy in
[offline prompt evaluation](offline-prompt-evaluation.md), not only exact
match. Prefer ReAct when external grounding must cut CoT hallucination;
prefer CoT when retrieval noise creates
[tool failure](agent-tool-failure-modes.md) cascades. Teach few-shots to
**target** the right entity/ensemble rather than enumerate every named
mention, and to reformulate after failed Search. Treat false positives as
harness bugs — they inflate resolve rate while teaching bad grounding habits
under [agent planning failure modes](agent-planning-failure-modes.md).
