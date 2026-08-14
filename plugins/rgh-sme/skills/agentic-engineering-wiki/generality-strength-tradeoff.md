---
type: concept
title: Generality–Strength Tradeoff
description: >
  Today's LLMs trade generality (working across any domain) against strength
  (reliably solving complex tasks); narrowing scope is how you buy the
  latter.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

Classic ML models were narrow specialists (sentiment analysis, fraud
detection, translation). GPT-style models perform an enormous variety of
tasks across domains, but this is not AGI (artificial general intelligence) —
AI meeting or exceeding human-level cognition, able to assimilate knowledge,
reason about it, solve novel and complex problems, and generate genuinely new
knowledge with humanlike creativity across any domain. Today's LLMs are
markedly deficient at reasoning and problem-solving (especially mathematics),
mostly recombine existing knowledge rather than introduce new knowledge, and
cannot learn new information outside of training.

A future AGI would possess both **strength** (solving complex problems) and
**generality** (solving problems in any domain). Current LLMs sit on a
tradeoff curve between the two:

- A pure chat app with an open system message sits at the general-but-weak
  end — it will discuss anything but won't reliably accomplish complex tasks,
  and is best suited to one- or two-step tasks where a human does the actual
  work.
- Narrowing an agent's domain — a custom system message plus domain-specific
  tools, i.e. [system prompt architecture](system-prompt-architecture.md) and
  a scoped [tool inventory](tool-inventory.md) — trades generality for
  strength.
- Pushing further along the strength axis,
  [LLM workflows](workflow-build-process.md) break a large task
  into small, well-defined tasks executed with high fidelity, coordinated by
  a supervisor process that may or may not itself be LLM-based. A workflow
  doesn't handle arbitrary requests — it's built for one specific task, and
  is therefore more capable at that task than a general-purpose
  conversational [LLM agent](llm-agent.md) asked to improvise the same
  multi-step plan.

Conversational agents fail complex workstreams for concrete reasons: they
lack natural work-item queues, grow distracted as system message and tools
bloat, and treat instructions as suggestions rather than enforceable
structure — failures seen when a single agent is asked to crawl, invent,
draft, and send marketing at once. This tradeoff is why a task's shape should
drive the architecture choice: a one-off, exploratory, or genuinely
open-domain request favors a conversational agent; a recurring,
well-understood, multi-step task favors narrowing scope, up to and including
a full workflow. See
[conversational agent structural limitations](conversational-agent-structural-limitations.md)
for the specific mechanics of why conversational agents break down on
complex multi-step work. Prefer modular workflows under
[progressive agent architecture](progressive-agent-architecture.md); reach
for [LLM-driven workflow routing](llm-driven-workflow-routing.md) only when
that strength still needs open-ended agency.
