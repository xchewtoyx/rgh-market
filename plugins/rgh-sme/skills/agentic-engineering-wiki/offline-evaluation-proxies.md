---
type: concept
title: Offline Evaluation Proxies
description: >
  Test new prompt or harness ideas against a simulated success signal before
  exposing them to real users, since there is no live feedback signal offline.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

See [agent grader types](agent-grader-types.md) for a third category — human
graders — alongside the two proxy strategies below, and how multiple graders'
outputs combine into one task result.

Offline evaluation tests new ideas before exposing real users to them. It is
harder than evaluating a shipped system in some ways, because there's no live
customer feedback signal to lean on — you need a simulated proxy for success
instead. Decide the success dimensions first with
[application evaluation criteria](application-evaluation-criteria.md); the
proxy strategy below is *how* you score each dimension, not a substitute for
naming them. Two proxy strategies, chosen by how mechanically checkable the
task is:

- **Functional-completeness proxy** — for tasks with an objectively checkable
  output, like code, use that objective check directly: grab a sample of real
  repositories, confirm their tests run, surgically delete and regenerate
  code fragments, and check whether the tests still pass. This is the lucky
  case — it needs no judgment call about quality, only a pass/fail signal
  that's cheap to compute at scale.
- **LLM-as-judge** — for open-ended applications (a scheduling assistant,
  general chat) with no mechanical check available, have a separate LLM
  review transcripts or output variants the way a human judge would: either a
  basic "which version is better?" comparison, or scoring against a supplied
  checklist of criteria for more nuanced evaluation. This trades an
  objective check for a learned one, so its own reliability needs
  establishing before it can be trusted as a proxy — see
  [LLM self-assessment grading bias](llm-self-assessment-grading-bias.md),
  the [SOMA LLM assessment](soma-llm-assessment.md), and
  [grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md).
  Where a gold-standard reference solution exists instead, prefer
  [gold-standard matching](gold-standard-matching.md); where neither a
  reference nor a judge is available, fall back to
  [functional completion testing](functional-completion-testing.md).

Both proxy strategies need example inputs to run against in the first place —
see [example suite](example-suite.md) for the simplest way to start collecting
them and [eval sample sourcing](eval-sample-sourcing.md) for scaling past what
a human can hand-pick, and [eval test granularity](eval-test-granularity.md)
for deciding whether to test one model pass or the whole application loop.

General guidance either way: engage as much of the real application as
possible in the evaluation, not just the final generation step. It may be
easier — sometimes unavoidable — to mock the context-gathering step and test
only prompt assembly and boilerplate, but context-gathering quality is often
decisive for overall application quality, so sidestepping it in evaluation
risks a nasty surprise once the feature reaches production. This offline
testing is part of the same discipline
[prompt optimization tooling](prompt-optimization-tooling.md) leans on for its
own I/O example data.
