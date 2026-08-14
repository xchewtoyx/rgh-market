---
type: concept
title: ACI Design Principles
description: >
  Keep agent actions simple and efficient, feedback informative but concise,
  and add guardrails that catch common errors before they compound.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–15"
---

Four principles for shaping an [agent-computer interface](agent-computer-interface.md)
around a **fixed LM** (weights unchanged; actions, docs, and feedback adapt):

1. **Simple actions** — few options, concise docs; avoid bash-style option
   explosions that demand demos or finetuning.
2. **Compact, efficient actions** — important operations (navigate, edit)
   should finish in as few turns as possible; do not force composing many
   micro-actions for one higher-order intent.
3. **Informative but concise feedback** — show substantive state/effects (for
   example the revised file window after edit) without dumping irrelevant
   detail that burns tokens under [lost in the middle](lost-in-the-middle.md).
4. **Guardrails** — catch common mistakes early (syntax checks, result caps)
   so recovery is fast rather than letting
   [compound mistake amplification](compound-mistake-amplification.md) run.

Concrete SWE-agent instantiations:
[stateful file viewer](stateful-file-viewer.md),
[guardrailed edit tool](guardrailed-edit-tool.md),
[bounded search observations](bounded-search-observations.md),
[collapsed observations](collapsed-observations.md), and
[action format enforcement](action-format-enforcement.md). For browser agents,
see [lm-oriented web observations](lm-oriented-web-observations.md) and
[token-efficient quote observations](token-efficient-quote-observations.md).
Iterate by inspecting failed trajectories on a development set, then grid-search
ACI knobs — the same spirit as
[failure-derived prompt tips](failure-derived-prompt-tips.md). Aim toward
[automated ACI iteration](automated-aci-iteration.md) so those inspections
become a closed loop rather than only craft. Quantify each change with
[ACI component ablation](aci-component-ablation.md): human-UI patterns
(iterative search, full-file views, silent whole-file overwrites) often
regress resolve rate even when they feel natural.
