---
type: concept
title: Harness Self-Attribution's Regression Blindness
description: >
  An evolve loop's self-declared fix predictions land far above chance, but
  its regression predictions barely beat chance — it can justify why an edit
  helps but not reliably foresee what it will break.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §4.4.2"
---

An [evidence-driven change manifest](evidence-driven-change-manifest.md) makes
every edit's predicted impact checkable against the next round's real
outcomes — which lets its two halves be scored separately, and they turn out
to be reliable in very different degrees. Measured across evaluation rounds of
one evolve loop, comparing predicted task-level deltas against observed ones:

- **Fix predictions are evidence-driven and roughly 5x above a random
  baseline** on both precision and recall — when the loop names a task it
  expects an edit to fix, that expectation is grounded in something real, not
  noise dressed up as reasoning.
- **Regression predictions are barely above random** — only about 2x —
  meaning most regressions the loop is about to cause go unforeseen in its own
  manifest.

The asymmetry has a plain explanation: an editing agent reasons forward from a
diagnosed failure to a targeted fix, which is exactly the kind of causal chain
a model can construct and check against evidence. Predicting what a fix will
*break* requires reasoning about interactions the diagnosis never surfaced —
tasks the edit never touched directly, side effects on components the current
failure pattern says nothing about — which is a fundamentally harder
inference the same evidence trail doesn't support as well.

**Practical consequence:** treat a manifest's `predicted_fixes` field as a
genuinely useful targeting signal, but treat its `risk_tasks` / predicted-
regression field as, at best, a partial early warning — not a substitute for
actually re-running the full task panel after every edit. This asymmetry is
also what produces the non-monotone step pattern typical of an evolution
curve (score dips between otherwise-improving rounds): an edit lands its
predicted fixes reliably, then costs unpredicted regressions the manifest
never flagged, and the net can go either way per round even while the
best-so-far trend improves over the full run. Regression foresight — closing
this specific gap — is the most direct lever for making self-attributed
harness evolution safer to run with less human oversight per round.
