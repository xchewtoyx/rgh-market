---
type: concept
title: Automated ACI Iteration
description: >
  Turn recurring failed trajectory patterns into ACI changes automatically —
  tips, command docs, guardrails — instead of only hand-editing the interface.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 106–118 (Appendix E)"
---

Most [ACI design](aci-design-principles.md) today is **manual**: inspect failed
episodes, write [failure-derived prompt tips](failure-derived-prompt-tips.md),
tweak command docs, then measure with
[ACI component ablation](aci-component-ablation.md). That works but does not
scale as toolkits and domains grow.

**Automated ACI iteration** means the harness (or a meta-loop) scrutinizes its
own interface the way automated prompting improves seq2seq templates:
identify recurring bad strategies → propose corrective tip/command/guardrail
edits → keep only changes that raise
[offline harness](per-task-offline-harness-tests.md) / resolve metrics over a
horizon. Keep the [configurable ACI harness](configurable-aci-harness.md) as the
mutable artifact so iteration is config diff, not agent-loop rewrite.

Open design questions: how to credit incremental gains without overfitting a
dev set; how to decide when to add a tool versus ban a strategy; how principles
transfer when the same ACI vocabulary moves beyond programmatic SE (search UIs
for shopping or knowledge-base onboarding). Prefer a **small effective toolkit**
first — extend with browsing, static analysis, or fault localization only when
ablation shows signal — rather than growing the inventory before iteration
loops exist.

A fuller answer to "how" is the
[harness evolution outer loop](harness-evolution-outer-loop.md): expose every
harness piece as an addressable component under
[component observability](component-observability.md), distill trajectories
into evidence an editing agent can act on, and bind each edit to an
[evidence-driven change manifest](evidence-driven-change-manifest.md) so
credit and regression risk are checked against the next round's outcomes
rather than assumed.
