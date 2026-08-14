---
type: concept
title: Offline Example Suites
description: >
  Run 5–20 representative inputs through prompt assembly, save prompts and
  completions, and eyeball diffs — the first offline harness before automated
  scoring.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 10"
---

An **example suite** is the smallest useful
[offline prompt evaluation](offline-prompt-evaluation.md) setup:

1. 5–20 inputs spanning expected scenarios (whole app or one critical step).
2. A script that builds the real prompt and records prompt + completion files.
3. Human eyeballing — often via git diffs — to judge improve / regress / noop.

**How many inputs are enough scales with the effect size being detected, not
with a fixed rule of thumb.** Early in an agent's development, most changes
produce large, obvious effects — a fix either clearly helps or clearly
doesn't — so a small suite (dozens, not hundreds, of tasks) reliably shows
the difference. As an agent matures, the changes worth making shrink toward
narrower edge cases, and a small suite starts missing effects a larger one
would catch; the suite needs to grow specifically to keep pace with how
small an effect it's expected to detect. This also argues for starting the
suite early rather than waiting to accumulate "enough" examples first — eval
suites get *harder* to build the longer a team waits, since early on
product requirements translate directly into test cases, while a live
system with established behavior requires reverse-engineering success
criteria from what's already shipped.

It is not automated pass/fail; familiarity with the set reveals recurring
completion flaws you can target in prompts. Prefer whole-loop coverage first
(“testing should mirror reality”), then add unit-like suites for critical
passes. For multi-turn apps use **canned conversations** (force next turns to
assume scripted answers) or a **model-mocked user** guided by a profile
(tests the loop but bakes in model biases).

Grow samples by mining historical non-AI solutions, shipping telemetry
(consent-aware; better for online eval when gold labels are missing), or LLM-
generated situations (combinatorial topics; avoid incestuous sample generation
from the same model under test). Record latency and token stats on every run.
Graduate to automatic assessment and larger sets once eyeballing saturates —
[gold-standard matching](gold-standard-matching.md),
[functional completion testing](functional-completion-testing.md), or
[SOMA LLM assessment](soma-llm-assessment.md).
