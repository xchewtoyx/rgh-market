---
type: concept
title: Component-Level Harness Ablation
description: >
  Isolate one evolved harness component at a time to see where an evolution
  loop's gain actually lives — components own different failure surfaces and
  interact non-additively, capping the aggregate improvement.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §4.4.1"
---

When a [harness evolution outer loop](harness-evolution-outer-loop.md) jointly
edits system prompt, tools, middleware, and long-term memory, the headline
aggregate gain hides *where* that gain actually comes from. The diagnostic:
hold three of the four evolved components at their seed defaults, keep only
one evolved, and measure. Findings from one such study (Terminal-Bench 2, four
components isolated in turn against a 69.7% seed and a 77.0% full-evolution
result):

- **Three of four single-component variants beat the seed on their own**
  (memory-only, tool-only, middleware-only); the **system-prompt-only**
  variant is the sole regression against the seed. Prompt-only self-evolution
  — the surface most automated agent-improvement methods restrict themselves
  to, see
  [automated agent optimization taxonomy](automated-agent-optimization-taxonomy.md)
  — captures none of the gain that tools, middleware, and memory carry on
  their own, and can even cost ground relative to not touching the prompt at
  all.
- **Each component owns a different failure surface, visible in per-difficulty
  breakdowns.** Memory-only lifts hard tasks *above* the full joint-evolution
  result, while regressing easy tasks (added boundary-case lessons become
  superfluous re-verification once the task was already simple). Tool-only
  tracks close to full evolution on medium tasks but a built-in publish guard
  closes the loop too early on hard tasks. Middleware-only clears every easy
  task but inflates turn count on hard ones.
- **Components interact non-additively, which caps the aggregate gain.** The
  three positive single-component gains sum to more than the full joint-
  evolution gain, and on the hardest tier the memory-only variant *exceeds*
  the full result — memory, middleware, and prompt all independently push
  toward the same closure-style re-verification behavior, so stacking all of
  them spends turns on redundant re-checks rather than compounding benefit.
  Because the loop optimizes an aggregate score dominated by the largest
  difficulty tier, it converges on a trade-off tuned to that tier and only
  partially recovers the gain any single component shows on a different tier.

Design implication: a harness-evolution loop's own aggregate score is not
evidence that every component is being evolved efficiently — component-level
ablation is the only way to see that the joint result is leaving gains on the
table through interaction effects, something no amount of staring at the
aggregate curve alone would surface. Treat interaction-aware evolution (making
components *complement* rather than duplicate each other's fix) as an open
problem, not something the loop already solves by construction.
