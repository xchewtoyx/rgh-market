---
type: concept
title: Conversational Agent Eval Simulation
description: >
  Grading a conversational agent needs a second LLM playing the user, because
  the quality of the interaction itself — not just the end state — is part of
  what's being measured.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Conversational agents (support, sales, coaching) differ from coding or
research agents in what makes the eval hard: the interaction itself — tone,
pacing, whether the agent asked before acting — is part of what's under test,
not only whether the right end state was reached. That means most
conversational-agent evals need a second LLM to **simulate the user**,
stress-testing the agent across extended, sometimes adversarial multi-turn
exchanges rather than grading a single static input. Named benchmarks in this
space simulate multi-turn interactions across domains like retail support and
airline booking, with one model playing a user persona while the agent under
test navigates the scenario.

A worked eval for a refund-handling task shows what multidimensional scoring
looks like in practice: a model-based rubric grades interaction quality
directly (did the agent show empathy, was the resolution clearly explained,
was the response actually grounded in a tool's returned data rather than
invented) alongside a **state check** (was the ticket marked resolved, was the
refund actually processed), a **tool-call check** (was identity verified
before refunding, was the refund amount within policy), and a **transcript
constraint** (did it finish within a reasonable number of turns). Because many
conversational tasks (answering an open-ended question, for instance) have
several equally valid correct responses, this domain leans on model-based
graders more than coding evals do, using them to assess both communication
quality and goal completion together rather than either alone.

This is the multi-turn-simulation instance of the general pattern
[canned conversations and model-mocked users](canned-conversations-and-model-mocked-user.md)
already covers for building conversational test fixtures — the eval-design
framing here is what to *score* once that simulated conversation exists, not
how to generate it.
