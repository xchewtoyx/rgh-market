---
type: concept
title: Grader Score Combination
description: >
  Decide up front whether a task passes when every grader agrees or when a
  weighted blend clears a threshold — the combination rule changes what
  "passing" actually means as much as the graders themselves do.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Once a task is scored by more than one [grader](agent-grader-types.md) —
typical for anything beyond a single mechanical check — the individual
grader outputs need a combination rule to become one task-level result:

- **Binary** — every grader must pass; any single failing grader fails the
  task. Right when each grader checks something independently
  non-negotiable (e.g. a code fix must both resolve the reported bug and not
  break existing tests — see
  [patch outcome taxonomy](patch-outcome-taxonomy.md) for why collapsing that
  into one binary pass/fail already loses information a full taxonomy
  preserves).
- **Weighted** — combined grader scores must clear a threshold, letting a
  strong result on one dimension offset a weaker result on another.
  Appropriate when the graders measure genuinely tradeable qualities (tone
  versus resolution speed, say) rather than independent hard requirements.
- **Hybrid** — some graders gate (must pass, binary) while others contribute
  to a weighted score on top of that gate — e.g. a task must pass its
  deterministic tests to even be scored, and rubric quality then determines
  how well it scored among passing attempts.

Picking the wrong rule silently changes what the eval is actually measuring:
a weighted combination can let a task "pass" despite failing a check that
should have been non-negotiable, while an all-binary combination can hide
a continuum of partial progress a weighted score would have shown. Decide the
combination rule from what each grader is actually checking — hard
requirement versus a dimension worth trading off — rather than defaulting to
whichever is simplest to implement.
