---
type: concept
title: Grounding LLM Assessment in Human Evaluation
description: >
  Validate an LLM-as-judge pipeline by checking it doesn't widen disagreement
  beyond what a pool of human assessors already disagrees on among themselves.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

A well-structured assessment prompt — even one built with
[SOMA](soma-llm-assessment.md) — defines the grading task precisely
enough that the model "has no choice but to be objective," but that
precision alone doesn't validate the result. LLM self-assessment is
essentially a scalable replacement for human annotation (models scale, humans
don't), so it needs to be confirmed as not a substantial regression from the
human process it's replacing.

Comparing a single human's ratings to the model's only reveals *some*
disagreement, which is expected on its own — different humans disagree with
each other too, so any single comparison conflates "the model disagrees with
this person" with "people disagree with each other regardless of the model."
The correct method: use a *pool* of human assessors, measure their mutual
disagreement with a standard method (e.g. Kendall's Tau), and then confirm
that the measured disagreement stays roughly stable when the model — queried
once, at temperature 0 for reproducibility — is added into the pool as if it
were one more assessor. If adding the model doesn't meaningfully widen the
pool's disagreement, its judgments are about as trustworthy as another human
rater's would be; if it does, the assessment prompt needs more work before
it can be trusted as a replacement for human grading.
