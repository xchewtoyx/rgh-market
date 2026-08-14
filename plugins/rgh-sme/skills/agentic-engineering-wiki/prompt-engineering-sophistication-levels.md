---
type: concept
title: Prompt Engineering Sophistication Levels
description: >
  Rank LLM apps from thin wrappers through context injection and tools up to
  goal-directed agency — each level adds harness obligations, not just wording.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 1"
---

[Prompt engineering](prompt-engineering.md) is broader than single-prompt
wording: it is the practice of structuring the whole
[LLM application loop](llm-application-loop.md) so user problems become
completable documents and completions become user-domain results. Sophistication
climbs in four levels:

1. **Thin wrapper** — nearly direct prompting (chat thread packaging, naive
   file-as-completion). Minimal transform beyond format glue.
2. **Modify and augment** — modality transcription; external
   [context injection](dynamic-context-gathering.md) (neighboring tabs, docs,
   search hits for post-cutoff facts, past support transcripts — the seed of
   [retrieval-augmented generation](retrieval-augmented-generation.md)); and
   **statefulness** across turns with deliberate truncation/summarization
   under [memory management](memory-management.md) so history does not
   distract.
3. **Tool use** — the model reaches real systems via APIs. Design questions
   [tool definition design](tool-definition-design.md) and
   [agent tool categories](agent-tool-categories.md) answer: which tool,
   correct arguments, how results re-enter the prompt, and how tool errors
   are communicated ([function calling](function-calling.md),
   [ReAct](react-loop.md)).
4. **Agency** — the app decides toward broad user goals (multi-step gather and
   act). Frontier and failure-prone unless goals are tightly constrained;
   treat as [progressive agent architecture](progressive-agent-architecture.md)
   with guardrails, motivating the
   [generality-strength tradeoff](generality-strength-tradeoff.md) that later
   narrows scope back down via workflows and tool inventories, not a
   free-form AutoGPT default.

Each level is a strict increase in capability and design surface — moving up
a level doesn't obsolete the concerns from the level below, it adds new ones
on top. Climb only when a lower level cannot meet the product need — each
step adds failure modes the harness must own under
[offline prompt evaluation](offline-prompt-evaluation.md).
