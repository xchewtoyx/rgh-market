---
type: concept
title: Research Agent Eval Groundedness
description: >
  Score a research agent's output on groundedness, coverage, and source
  quality together, since no single check like unit tests exists for
  open-ended synthesis.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Research agents gather, synthesize, and analyze information into an answer or
report — a task with no equivalent of a coding agent's unit-test pass/fail
signal. What counts as "comprehensive," "well-sourced," or even "correct"
depends on the specific task (a quick market scan needs a different bar than
acquisition due diligence), experts can genuinely disagree on whether a given
synthesis is comprehensive enough, ground truth shifts as the underlying
sources it draws from keep changing, and longer, more open-ended outputs
simply create more surface area for mistakes to hide in. One named benchmark
in this space (BrowseComp) targets questions that are deliberately easy to
verify but hard to solve — needles in an open-web haystack.

Given no single check suffices, combine several grader types aimed at
different failure modes:

- **Groundedness checks** — verify each claim in the output is actually
  supported by the sources the agent retrieved, not asserted without backing.
- **Coverage checks** — a predefined set of key facts a genuinely good answer
  must include, checked for presence.
- **Source quality checks** — confirm the sources the agent actually consulted
  are authoritative, not merely whatever came back first in a search — a
  citation-backed answer built on weak sources is a different failure from an
  uncited one.

For sub-questions with an objectively correct answer (a specific reported
figure, say), exact match still works and should be used where it applies —
see [gold-standard matching](gold-standard-matching.md). Beyond that, an LLM
grader can flag unsupported claims and coverage gaps, and separately assess
open-ended synthesis for coherence and completeness. Because research quality
judgments are inherently more subjective than a coding agent's test suite,
these LLM-based rubrics need frequent recalibration against expert human
judgment — see
[grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md)
— more so than for domains with a firmer objective ground truth.
