---
type: concept
title: A Few Reliable Tests Beat Many Unreliable Ones
description: >
  A small suite of tests the team genuinely trusts produces better outcomes
  than a large suite riddled with flaky, unreliable tests — because unreliable
  tests get ignored or disabled, silently erasing whatever value they had.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# A Few Reliable Tests Beat Many Unreliable Ones

An unreliable test — one that fails intermittently for reasons unrelated to
an actual defect (timing, shared environment state, uncontrolled starting
conditions) — costs more than it's worth: someone has to re-run it to check
whether the failure was real, interpret an ambiguous result, and eventually,
under enough repeated false alarms, the team starts ignoring or disabling it.
At that point it provides zero defect-catching value while still costing
review time on every run.

At scale, per-test flake rates compound: even **0.1% failure per test** across
10,000 daily runs implies investigating ~10 flakes per day. Automatic reruns
trade CPU for engineering time but only delay fixing root cause. As flakiness
approaches **~1%**, suites lose value — teams stop reacting to failures and
the suite stops catching defects. Google reported a ~**0.15%** flake rate
(still thousands of flakes daily) requiring active engineering investment.
Most flakes come from nondeterminism inside tests themselves — clock time,
thread scheduling, network latency, hardware interrupts, browser rendering —
not from the product under test. See [test size constraints](test-size-constraints.md)
for why small, constrained tests reduce these sources.

The corrective is to automate deliberately rather than exhaustively: a small
number of tests the team fully trusts is worth more than a large number that
include unreliable ones, because trust is what determines whether a failure
actually gets acted on. One documented case: a large e-commerce retailer
replaced 1,300 manual tests run every ten days with just 10 automated tests
run on every commit — and grew that trusted suite to hundreds of thousands of
tests over time, rather than starting from an untrustworthy large suite and
hoping to fix it later.

This is the strategic framing behind
[commit test suite design principles](commit-test-suite-design.md)'s
determinism requirement and
[developer-owned test suite maintenance](developer-owned-test-maintenance.md)'s
ownership argument: both exist to keep the suite in the "trusted" category
rather than letting it decay into the "ignored" one. See also
[automated test suite qualities](automated-test-suite-qualities.md) for the
fuller checklist this principle is part of.
