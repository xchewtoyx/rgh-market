---
type: concept
title: ReAct Thought Editing
description: >
  Let humans correct a few reasoning traces mid-episode so later actions
  realign — cheaper than retyping action sequences or retraining the policy.
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

Because [ReAct](react-loop.md) thoughts are readable language in the same
transcript as acts, humans can **inspect and edit** them on the fly: delete a
hallucinated belief, insert a subgoal hint, or change reasoning style. Later
actions often realign after only a couple of thought edits — far less effort
than typing tens of corrective actions, and unlike Act-only or classical RL
where changing a few past actions rarely reshapes the policy.

This is stronger than dialogue-only goal updates: edits can rewrite internal
beliefs the flexible thought space supports. Expose it as an
[agent UX steering](agent-ux-steering-affordances.md) affordance (editable
thoughts + regenerate forward) and pair with
[human approval gates](human-approval-gates.md) when acts have real side
effects. Coupling LLMs to web or physical action spaces still risks harmful
lookups or irreversible acts — keep blast-radius limits in the harness even
when thoughts look aligned.
