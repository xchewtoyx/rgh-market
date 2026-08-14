---
type: concept
title: Plan-and-Solve Prompting
description: >
  Prompt the model to form an overarching plan before working the problem
  step by step, without any tool use or think-act-observe loop.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

Rather than jumping straight into a
[ReAct](react-loop.md)-style think-act-observe loop, plan-and-solve prompting
asks the model to first form an overarching plan before executing it: "Let's
first understand the problem and devise a plan to solve the problem. Then,
let's carry out the plan and solve the problem step-by-step." No tool usage is
involved — it is purely a reasoning-quality technique, closer in spirit to
zero-shot [chain of thought prompting](chain-of-thought-prompting.md) than to
ReAct's tool-using loop, decomposing the problem before committing to any
intermediate answers.

Because it produces a plan without any tool interaction, it is the
prompt-level cousin of [hierarchical planning](hierarchical-planning.md),
addressing the same generate-a-roadmap-first idea as a single-turn reasoning
prompt rather than an agent architecture. Combining preplanning with ReAct's
loop — plan first, then think-act-observe against that plan — is a natural
harness pattern worth trying when goals need both structure and external
actions, or when neither technique alone is enough.
