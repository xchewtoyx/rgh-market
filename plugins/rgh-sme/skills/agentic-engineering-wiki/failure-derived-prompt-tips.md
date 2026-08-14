---
type: concept
title: Failure-Derived Prompt Tips
description: >
  Encode recurring failed strategies seen in development trajectories as short
  imperative tips in the instance prompt to steer later episodes.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

Failure-derived prompt tips are manually iterated instructions distilled from
inspecting failed development trajectories — then pasted into the instance
layer of an [agent episode prompt stack](agent-episode-prompt-stack.md).
Examples from software-engineering agents: always reproduce the bug before
editing; never retry an identical failed command; jump with `goto` instead of
endless scrolling; verify the open file versus cwd after create/open; re-read
the file after edit.

Tips are surprisingly effective at killing the specific errant strategies they
name, even when full demos do not teach domain nuance. They do not scale as a
manual craft — treat them as a bridge toward automated
identify-failure → write-corrective-instruction loops, closer to
[Reflexion](reflexion.md) but baked into the static prompt rather than only
emitted mid-episode. Keep tips concrete and imperative; vague “be careful”
advice under [explicit instruction design](explicit-instruction-design.md)
rarely changes tool choice. For interactive [ReAct](react-loop.md) prompts,
prefer few-shot thoughts that **advance** subgoals over repeating the same
unfinished goal each turn — ReAct-IM-style loops are a failure mode you can
spot in development trajectories and ban explicitly.
