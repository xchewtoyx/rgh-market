---
type: concept
title: Agent Tool Failure Modes
description: >
  The right tool can still return wrong output, mistranslate an NL plan, or be
  missing entirely — failures that must be tested per tool, not only per plan.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    resource: "ReAct (Yao et al.), pp. 1–15"
---

Tool failures occur when the *correct* tool is chosen but its output is wrong —
a bad image caption, a wrong SQL query — or when a
[natural language action plan](natural-language-action-plans.md) translator
mistranslates a step into the wrong command.

A distinct case is **missing tool failure**: the agent lacks any tool that
could solve the task (needs live prices with no network access). Detecting
missing tools requires domain knowledge of what tools *should* exist; persistent
domain-specific failure is a signal to add inventory, not only to prompt
harder.

Always log each [function calling](function-calling.md) invocation and output.
Build dedicated checks for translator components. Distinguish these from
[planning failure modes](agent-planning-failure-modes.md), where the plan
itself is wrong before execution.

When tools fail at runtime, feed **definition-relative** error messages back
into the transcript so the model can self-correct on the next turn — not raw
internal exceptions that leak implementation detail or confuse retry. Pair with
[tool definition design](tool-definition-design.md) so the anticipated output
shape and error vocabulary match what the model saw in the schema.

**Non-informative retrieval** is a ReAct-specific tool failure: empty or
off-topic search hits derail subsequent reasoning and recovery even when the
API succeeds. Cap and format hits
([bounded search observations](bounded-search-observations.md)), teach
reformulation in few-shot thoughts, and fall back via
[internal–external knowledge routing](internal-external-knowledge-routing.md)
when the step budget is spent without a grounded answer.
