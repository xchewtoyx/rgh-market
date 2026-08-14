---
type: concept
title: Task Quality Escalation Ladder
description: >
  When a task's first-draft results aren't good enough, escalate through a
  fixed sequence of fixes rather than reaching for the most complex one first.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

When a [workflow task](task-io-schema-design.md)'s first-draft results aren't
good enough, escalate through these techniques in order rather than jumping
straight to the most expensive one:

1. **Add a reasoning nudge.** If the task isn't thoughtful enough, prepending
   something like "let's think step-by-step" before demanding the refined
   answer can considerably improve results
   ([chain-of-thought prompting](chain-of-thought-prompting.md)). If the model
   jumps to a tool call before it has reasoned about the task, use
   [forced reasoning before tools](forced-reasoning-before-tools.md) to
   require the reasoning step explicitly.
2. **Tighten the prompt.** A common failure mode is the task confidently
   ending with a wrong answer — bad formatting, not actually answering the
   question, or (for code) bugs and syntax errors. Before reaching for a
   heavier fix, check the prompt's clarity as a human reading it would: could
   you tell exactly what to do from this wording alone?
3. **Apply Reflexion.** If failures persist, attempt the task with whichever
   prompting method fits, then have the application layer analyze the output
   against requirements — a format check, running unit tests for code output,
   or an LLM review of the output. If requirements aren't met, craft a new
   prompt containing the task requirements, the model's previous attempt, and
   the analysis report, and ask the model to learn from the mistake and retry.
   See [Reflexion](reflexion.md) for the general pattern; applying it one or
   more times improves the odds of success but costs significantly more
   compute each time.
4. **Pair a conversational agent with a user-proxy agent**, for complex,
   open-ended tasks that resist being pinned down as a single templated
   prompt. See
   [role-based agent delegation](role-based-agent-delegation.md)'s
   Assistant/UserProxy pattern — an expert agent alone often won't act without
   a conversational partner pushing it toward the goal, and this step is
   still experimental relative to the more deterministic steps above it.

Prefer the earliest step in this ladder that actually fixes the problem: each
step down the list trades more compute and more architectural complexity for
higher odds of success, so treat escalation as a cost, not a default.
