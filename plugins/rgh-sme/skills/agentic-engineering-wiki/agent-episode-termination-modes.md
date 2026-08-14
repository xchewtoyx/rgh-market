---
type: concept
title: Agent Episode Termination Modes
description: >
  Distinguish intentional submit, cost-limit submit, cost-limit with no edits,
  and early format-exit — only intentional submits resolve at useful rates.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

Software-engineering agent episodes end in a few harness-defined ways:

1. **Submit** — agent issues an explicit `submit` after edits.
2. **Exit cost (submit)** — budget hit; gather changes so far and submit.
3. **Exit cost (no submit)** — budget hit with no edits → unresolved.
4. **Early exit** — too many consecutive malformed actions; optional submit of
   whatever exists ([action format enforcement](action-format-enforcement.md)).

Resolved runs are overwhelmingly **intentional Submit** (e.g. GPT-4 Turbo full
SWE-bench: hundreds of resolved submits vs tens of cost-cutoff submits). Submit
endings also resolve far more often than cost cutoffs (~14% vs ~3% in that
setting). Design implication: raising the dollar/turn cap without improving
early localization and edit recovery mostly buys more
`exit_cost` tails under [agent trajectory phases](agent-trajectory-phases.md).
Well-shaped ACIs keep early-exit from format failure near zero — that is a
harness health metric next to resolve rate. Report pass@k / multi-run variance
separately when single pass@1 is noisy but expensive to resample.
