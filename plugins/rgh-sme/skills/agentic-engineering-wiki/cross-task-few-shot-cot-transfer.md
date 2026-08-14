---
type: concept
title: Cross-Task Few-Shot CoT Transfer
description: >
  Few-shot CoT exemplars from another domain help mainly when answer format
  matches; mismatched formats collapse gains — often worse than zero-shot CoT.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §3 Table 5"
---

Few-shot [chain-of-thought prompting](chain-of-thought-prompting.md) is
sensitive to how well exemplars match the **task and answer format**. Cross-
domain exemplars that keep the same multiple-choice framing can still lift
accuracy substantially over plain zero-shot, but transferring to a different
answer type (e.g. CommonsenseQA → MultiArith) helps far less. In Kojima et al.,
both cross-task Few-shot-CoT variants still underperformed
[zero-shot chain of thought](zero-shot-chain-of-thought.md) on MultiArith —
underscoring the engineering cost of curated exemplars.

This aligns with the broader [in-context learning](in-context-learning.md)
pitfall that models often latch onto repeated **format** more than task
semantics. When building exemplar packs, match output schema first; if you
cannot maintain task-matched demos, prefer a robust
[reasoning trigger](reasoning-trigger-sensitivity.md) over mismatched CoT
shots, and verify with [offline prompt evaluation](offline-prompt-evaluation.md).
