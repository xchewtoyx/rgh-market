---
type: concept
title: Static vs Dynamic Prompt Content
description: >
  Split always-on task clarification from per-instance context so instructions
  stay consistent while dynamic material can change every call.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Prompt material is either **static** — the same every call: task framing,
precise instructions, format rules — or **dynamic** — different every time:
user facts, retrieved docs, conversation state. The boundary follows how the
app is built: hardcoded clarification is static; strings from variable
sources are dynamic context. LLMs assimilate messy text well, but only if
the harness **supplies** it.

The line between them isn't always clean, and which category a piece of text
falls into depends on how the application is built, not on its content alone:
"I want a proper book, not a self-help book" could plausibly be either, but a
sentence hardcoded into the app for every user is static clarification, while
the same sentence pulled from a variable source (the user's own words, a
database lookup) is dynamic context. If a rule applies to everyone using the
app, it's clarification; if it's ascertained about one particular user or
request, it's context.

Static clarification matters more in programmatic loops than chat: there is
no quick human repair turn, and consistent criteria enable optimization and
user trust. Prefer **positive** dos over bare don’ts, bolster commands with
a reason, and avoid brittle absolutes. Put explicit rules in the
[system prompt](system-prompt-architecture.md) for chat APIs trained to obey
it; use [explicit instruction design](explicit-instruction-design.md) and
[in-context learning](in-context-learning.md) — labeled explicitly or via
[few-shot example formatting](few-shot-example-formatting.md) — as implicit
clarification when rules are hard to enumerate.

Both kinds of content need sourcing before they can be filtered and
prioritized: for dynamic content specifically, favor gathering broadly first
("no bad ideas" at the gathering stage) and narrowing down later during
[scoring and prioritization](llm-application-feedforward-pass.md), rather
than pre-filtering too aggressively while collecting it.

Under [prompt element importance](prompt-element-importance.md), score
static instructions high-importance and place them at the edges
([sandwich technique](sandwich-technique.md)); treat dynamic blocks as
budget-flexible under [context engineering](context-engineering.md) and
[prompt assembly algorithms](prompt-assembly-algorithms.md). Designing
*what* to fetch and under which latency/preparability limits is
[dynamic context gathering](dynamic-context-gathering.md).
