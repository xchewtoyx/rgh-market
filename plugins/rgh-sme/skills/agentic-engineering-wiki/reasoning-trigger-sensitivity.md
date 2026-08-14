---
type: concept
title: Reasoning Trigger Sensitivity
description: >
  Zero-shot CoT accuracy swings widely with the exact reasoning cue — instructive
  triggers help; misleading or irrelevant ones collapse to baseline or worse.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), §3 Table 4"
---

[Zero-shot chain of thought](zero-shot-chain-of-thought.md) is not
trigger-invariant. On MultiArith with text-davinci-002, Kojima et al. find
instructive cues that invite stepwise reasoning (best: “Let’s think step by
step,” ~79%) far outperform misleading (“Don’t think. Just feel.”) and
irrelevant (“Abrakadabra!”) strings that sit near or below plain zero-shot
(~18%). Even among instructive prompts, wording still moves accuracy by tens
of points (“First,” / “logically” / “splitting it into steps” span ~45–77%).

Treat the trigger as a first-class prompt artifact in the
[prompt catalog](prompt-catalog.md). Sweep a small set of instructive variants
under [offline prompt evaluation](offline-prompt-evaluation.md) rather than
assuming any “think step by step” paraphrase is equivalent. Prefer automatic
template discovery only when you already have a metric and a validation split
([prompt optimization tooling](prompt-optimization-tooling.md)).
