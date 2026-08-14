---
type: concept
title: Agent Trajectory Phases
description: >
  Expect early localization/reproduction, then mid-episode edit–evaluate
  cycles, then submit — and redesign recovery when the first approach fails.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

Software-engineering agent trajectories under an
[agent-computer interface](agent-computer-interface.md) show recurring phases
(Yang et al. on SWE-bench):

1. **Early (turns ~1–4)** — **reproduction** and **localization**. Dominant
   patterns create a scratch file, edit a snippet, and run it; alternatives
   start with directory/file search then open/scroll.
2. **Mid/late (≈turn 5+)** — **edit then evaluate** (`edit` paired with
   `python`/`pytest`). First edits rarely fully resolve; repeated
   execution feedback drives better patches. Interleaved navigation
   (`scroll_*`, `open`, search) handles long functions and callers that
   break after an edit.
3. **Submission** — intentional `submit` clusters ~turns 10–20; rarer later.

Most resolved runs finish well within budget (GPT-4 SWE-agent mean ~15 turns
on full SWE-bench). Critical failure mode: if the first ~10–20 turns’ approach
fails, agents **underuse remaining budget** — greedy local editing and
context overload instead of re-exploration. Prefer
[collapsed observations](collapsed-observations.md) (e.g. last-five history)
and temperature/window settings validated by ACI ablations; invest in
recovery prompts and tools that force re-localization after repeated eval
failures rather than only raising the cost/turn cap. Classify how episodes
end with
[agent episode termination modes](agent-episode-termination-modes.md) —
resolved work almost always intentional-submits within budget. Use phases and
termination modes as the evaluation grain for harness changes under
[episode-scale evaluation vs request APM](episode-scale-evaluation-vs-request-apm.md). Editing-only
subtasks (HumanEvalFix-style single-file bugs) finish even earlier (often
≤10 turns) when localization is removed from the problem.
