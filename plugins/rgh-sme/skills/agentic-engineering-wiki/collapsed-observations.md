---
type: concept
title: Collapsed Observations
description: >
  Preserve history structure while replacing old tool or command outputs with
  short placeholders to cut tokens and drop stale duplicate state.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

Collapsed observations keep the shape of an agent trajectory — which actions
ran, in what order — while replacing bulky old observation bodies with a
one-line stub such as “Old output omitted (N lines).” Dual purpose: shrink
tokens per step, and remove outdated duplicates (directory listings, file
views, prior command dumps) that compete with current state under
[context engineering](context-engineering.md).

Prefer collapsing *bodies*, not erasing turns: the model still sees that a
command happened. Do not collapse the system template or the latest
observation the agent must react to. Keeping only the last few observations
(SWE-agent default: last 5) beats full-history retention on resolve rate —
full history costs ~3 absolute points under
[ACI component ablation](aci-component-ablation.md). Expect
[agent trajectory phases](agent-trajectory-phases.md) (localize/reproduce →
edit–eval → submit) when reading collapsed histories — early failures need
recovery affordances, not only a longer turn budget. Pair with
[agent episode prompt stack](agent-episode-prompt-stack.md) next-step templates
and [memory summarization](memory-summarization.md) when even placeholders
accumulate past budget. Unlike blind
[FIFO context eviction](fifo-context-eviction.md), collapse targets redundant
environment feedback first.
