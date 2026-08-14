---
type: concept
title: Agent UX Steering Affordances
description: >
  UI controls that expose tool activity, let users edit or authorize calls, and
  regenerate from a corrected point so humans steer the agent mid-trajectory.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
---

Conversational agents are assisted agency: the human stays in the loop to
correct drift. Beyond a chat transcript, the harness should expose:

- **Processing and tool-use indicators** — show that work is in flight and that
  background tools ran.
- **Tool-call detail** — name, arguments, and results so users can inspect why
  a reply happened.
- **Editable tool arguments** — let users correct a bad call and resubmit.
- **Regeneration from a corrected point** — after a corrected tool call or
  message, regenerate the trajectory forward so steering sticks.
- **Authorization prompts** for any tool that might modify real-world assets —
  application-layer interception, not prompt-level pleading
  ([human approval gates](human-approval-gates.md)).
- **Artifact visibility** — show which [conversation artifacts](conversation-artifacts.md)
  the agent currently sees, and allow dismiss when focus is wrong.

These affordances are harness design for [LLM agents](llm-agent.md): they make
tool traces and context selections inspectable and reversible. Chat turn-taking
alone does not give users enough leverage when tool side effects or wrong
attachments derail the task. In multi-agent simulacra
([generative agent architecture](generative-agent-architecture.md)), also
offer an **inner-voice** channel — the user speaks as the agent’s conscience
so directives stick more reliably than as an outside character — and let users
rewrite nearby object state in natural language for the
[agent environment tree](agent-environment-tree.md) to notice.
