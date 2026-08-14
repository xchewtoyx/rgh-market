---
type: concept
title: Dynamic Context Gathering
description: >
  Runtime collection of per-instance background under latency, preparability,
  and comparability constraints — usually the bulk of context-design work.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 5"
---

Once [static vs dynamic prompt content](static-vs-dynamic-prompt-content.md)
has framed the task, the model still lacks subject-specific background
(user, document, session). Gathering that material is typically where most
context-design and coding time goes: unlike static clarification, it runs
while the program is live inside the
[feedforward pass](llm-application-feedforward-pass.md).

Three constraints shape what is feasible:

- **Latency / urgency** — non-user or fire-and-forget triggers tolerate slow
  retrieval; on-demand actions tolerate moderate wait but rarely multi-pass
  LLM pipelines; in-the-moment completions (typing) make every millisecond of
  lookup risk the request going stale, so complex non-precomputed retrieval
  is usually out.
- **Preparability** — rarely changing facts can be precomputed; under extreme
  latency pressure, *speculatively* prepare candidates you might need because
  there will be no time to fetch them on demand.
- **Comparability** — gather more than you can pack, then triage. Every item
  needs a usefulness score (and awareness of
  [dependency](prompt-element-dependency.md) / invalidation) so
  [prompt element importance](prompt-element-importance.md) and
  [prompt assembly algorithms](prompt-assembly-algorithms.md) can drop the
  weak ones. Static clarification often earns the highest score because
  misunderstanding the question dominates; all context is optional in
  principle — quantify how optional.

Discover candidate sources with
[dynamic context source discovery](dynamic-context-source-discovery.md), then
implement the obvious near sources first and grow outward as the product
matures.
