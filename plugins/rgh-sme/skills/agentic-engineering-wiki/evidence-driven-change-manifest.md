---
type: concept
title: Evidence-Driven Change Manifest
description: >
  Attach every harness edit to a self-declared, falsifiable prediction of what
  it will fix and what it might break, then verify that prediction against the
  next round's real outcomes.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.3, App. B.2"
---

Letting an agent edit its own harness invites rationale-driven
self-justification — an edit that sounds principled but was never actually
checked against evidence. The **evidence-driven change manifest** pattern
forces every edit through a fixed evidence contract before it can be made, and
a fixed verification step before it can survive:

**Before writing an edit**, the editing agent must have, sourced from
[trajectory distillation](agent-debugger-trajectory-distillation.md) reports
rather than intuition or "best practices":

1. **Failure evidence** — which tasks failed, and specifically what went
   wrong.
2. **Root cause** — *why* it failed, not just what failed.
3. **Targeted fix** — a change that addresses the root cause directly.
4. **Predicted impact** — which tasks this should fix, and which tasks it puts
   at risk of regressing.

**After the edit ships and the next round evaluates**, the loop intersects the
manifest's predicted-fix and predicted-regression sets with the observed
task-level deltas (fail→pass, pass→fail) to produce a per-edit verdict:
**KEEP** (working, leave as-is), **IMPROVE** (directionally correct, refine),
or **ROLLBACK + PIVOT** (not working at this component level — revert, then
re-approach the same failure pattern at a
[different component level](harness-component-level-selection.md), rather
than iterating harder at the level that already failed twice).

The manifest is what turns "the agent believes this edit helps" into "the next
round can prove or disprove it" — "each edit thereby becomes falsifiable by
the next evaluation, which replaces rationale-driven self-justification with a
measurable contract between rounds." Empirically this targeting is real but
asymmetric: an evolve loop's fix predictions land roughly 5x above a random
baseline, but its regression predictions land only about 2x above random —
see
[harness self-attribution's regression blindness](harness-self-attribution-regression-blindness.md)
for why that asymmetry matters for how much you should trust the manifest's
risk column.

One prompt-engineering trap worth naming explicitly for whatever agent writes
the manifest: get the **iteration numbering off-by-one framing right**. When
the query reports "iteration N evaluation completed," that describes the
harness produced by iteration N−1 — the agent is now writing edits that will
be *labeled* iteration N and evaluated *next* round. Manifests that silently
advance the iteration counter by one corrupt the attribution step's ability to
match predictions to the round they actually describe.
