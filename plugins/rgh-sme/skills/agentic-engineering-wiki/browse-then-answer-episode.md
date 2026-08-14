---
type: concept
title: Browse-Then-Answer Episode
description: >
  Separate a browsing phase that gathers quoted references from a later answer
  phase that composes only from those references and the question.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §2"
---

WebGPT episodes have two phases. While browsing, `Quote` stores title, domain,
and extract as references; browsing ends when the model issues `End: Answer`,
hits a max-action limit, or exceeds max total reference length. If at least one
reference exists, a **new answering prompt** (question + numbered references)
asks for the final answer — no further browser tools.

This [agent control flow](agent-control-flow.md) topology keeps evidence
gathering distinct from synthesis, pairs with
[token-efficient quote observations](token-efficient-quote-observations.md),
and makes citation support checkable offline under
[citation-backed agent answers](citation-backed-agent-answers.md). Prefer
explicit phase transitions over letting the model answer mid-browse when you
need grounded QA; expose early-exit labels (nonsense / controversial) as
first-class
[agent episode termination modes](agent-episode-termination-modes.md).
