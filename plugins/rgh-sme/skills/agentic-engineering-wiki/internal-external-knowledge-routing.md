---
type: concept
title: Internal External Knowledge Routing
description: >
  Fall back between retrieval-grounded acting and sample-and-vote CoT when
  step budget or answer confidence shows one path is stuck.
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

Knowledge-intensive agents often need both **parametric** internal knowledge
and **non-parametric** retrieval. Pure
[chain of thought](chain-of-thought-prompting.md) structures reasoning well but
hallucinates facts; pure [ReAct](react-loop.md) stays grounded via tools but
can waste the step budget on non-informative searches or repetitive
thought/action loops. Yao et al. treat the two as complementary and route
between them with simple harness heuristics:

- **ReAct → CoT-SC:** if the agent never finishes within a fixed step budget
  (for example 7 HotpotQA / 5 FEVER Wikipedia turns), stop tool use and answer
  with [self-consistency decoding](self-consistency-decoding.md) over internal
  knowledge.
- **CoT-SC → ReAct:** if majority vote among \(n\) CoT samples occurs fewer
  than \(n/2\) times (low internal confidence), hand the question to a
  retrieval-acting loop instead.

On HotpotQA / FEVER with PaLM-540B, either hybrid beat standalone CoT-SC across
sample counts — matching CoT-SC@21 with only a handful of samples — while
keeping answers more inspectable when ReAct succeeds. For harness design, log
which branch produced the answer (provenance for
[context grounding](context-grounding.md)), keep Act-only and CoT-only
ablations in [offline prompt evaluation](offline-prompt-evaluation.md), and
treat weak search APIs as intentional
[agent-computer interface](agent-computer-interface.md) pressure that forces
explicit reformulation rather than opaque dense retrieval.
