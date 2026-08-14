---
type: concept
title: Eval Environment Isolation
description: >
  Start every eval trial from a clean environment — shared state between
  trials creates correlated failures that look like agent performance and can
  let an agent cheat on leftovers from a previous run.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), Going from zero to one: a roadmap to great evals for agents"
---

An eval harness's environment needs to be as controlled as the grading itself.
Two distinct failure modes come from letting state leak between trials that
are supposed to be independent:

- **Correlated failures masquerading as agent performance.** If several
  trials fail because of the same environmental limitation — limited CPU
  memory, a resource that wasn't reset, a leftover file from a prior run — those
  trials are not independent measurements; they share a confound. Aggregating
  them as if they were independent samples of agent capability overstates how
  much a real capability gap explains the failures.
- **Unfair advantage from leftover state.** An agent can exploit artifacts a
  previous trial left behind that it shouldn't have access to — one observed
  case: an agent gained an advantage on a task by inspecting git history left
  over from an earlier trial in the same environment, effectively reading
  information the task was not supposed to make available.

The fix is structural, not a grading adjustment after the fact: each trial
must run in a genuinely fresh environment, with the agent under test
configured to match production as closely as the eval harness will support.
This is a different failure mode from
[eval observation anti-leakage](eval-observation-anti-leakage.md), which
censors gold-adjacent text *within* a single observation the agent can see —
environment isolation is about state leaking *across* trials that are
supposed to be independent of each other, not about a single observation
revealing too much. Both need to be designed for; neither substitutes for the
other. Build isolation into the same harness that
[per-task offline harness tests](per-task-offline-harness-tests.md) run
against, not as a one-off fix applied after a suspicious result surfaces.
