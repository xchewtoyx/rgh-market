---
type: concept
title: SOMA LLM Assessment
description: >
  Grade free-form completions with Specific questions, Ordinal scales, and
  Multi-Aspect criteria — as a third-party judge, validated against humans.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 10"
---

SOMA is a structured technique for getting more reliable results out of
LLM-as-judge assessment (see
[LLM self-assessment grading bias](llm-self-assessment-grading-bias.md) for
the framing issue this technique doesn't by itself solve): **S**pecific
questions, **O**rdinal scaled answers, **M**ulti-**A**spect coverage.

- **Specific questions** — some tasks are easier to verify than to solve
  (confirming a poem is a valid limerick, versus writing one), and for those a
  generic "Is this right?" can work fine. But for most tasks — a smart-home
  tool call setting a specific temperature, say — answering "is the
  completion right?" is nearly as hard as generating the completion in the
  first place, and an underspecified assessment question can produce an
  answer worse than the original generation due to its own ambiguity.
- **Ordinal scaled answers** — ditch yes/no. Standards for "right" vary by
  model caprice, or worse, by systematic bias (holding higher-accuracy
  attempts to stricter standards, or accepting a barely-over-50%-correct
  answer while rejecting a near-perfect one under a binary frame). Ask for a
  rating on an ordinal scale instead — a 1-5 scale is a reasonable default —
  with a description or worked example anchoring each level, so "3" means the
  same thing across runs.
- **Multi-aspect coverage** — a single "how good is this?" question invites
  inconsistent implicit criteria from one evaluation to the next (sometimes
  judging correctness, sometimes judging whether the model asked before
  acting, sometimes judging tool choice). Predefine explicit categories
  instead, and ask the model to rate each separately, then combine the
  scores. For a smart-home example: did the completion correctly implement
  the intended action (right tool, right syntax); did that action actually
  remedy the user's problem; was the model sufficiently restrained from
  acting without asking, yet sufficiently assertive to avoid excessive
  hand-holding.

State that an assessment is happening, and which aspects to grade, *before*
showing the example to be graded — the model reads once and can't backtrack,
so front-loading the evaluation frame lets it focus on the right aspects
while it reads rather than needing to re-derive them afterward.

A common, reusable choice of aspects splits **intent** (did the model have
the right idea — is the chosen fix actually correct?) from **execution** (did
it correctly carry out that intent — right tools, right syntax?). This
intent/execution split underlies the
**relevance-truth-completeness (RTC)** system used for scoring chat
conversations: relevance (did it address the right thing), completeness (did
it cover the topic fully, not just part of it), and truth (was the content
actually correct). Break apart any "Goldilocks" question asking whether a
completion was "just right" into its two component aspects (enough, and not
too much) and ask them separately — conflating them produces noisier results
than either question would alone.

**Validate the judge itself**, not just the questions it's asked: add
temperature-0 model scores to a **pool** of human raters and check that
disagreement (e.g. Kendall's Tau) stays stable, rather than comparing the
model's scores against a single human rater alone — a lone comparison point
can't distinguish the model drifting from ordinary inter-rater disagreement.
Links to [offline prompt evaluation](offline-prompt-evaluation.md) and
[gold-standard matching](gold-standard-matching.md) when labels exist.
