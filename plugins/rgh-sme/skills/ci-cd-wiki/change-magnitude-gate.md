---
type: concept
title: Change-Magnitude Gate
description: >
  An automated pre-check that blocks or escalates a change when its size or
  impact exceeds a threshold, catching accidental oversized or runaway
  changes regardless of whether the change itself is otherwise valid.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2, ch. 6"
---

# Change-Magnitude Gate

Correctness checks (tests, schema validation, linting) confirm a change is
*well-formed*; they say nothing about whether it's *plausible in size*. A
change-magnitude gate adds a second, independent check: compare the change's
size or impact against an expected range, and require elevated approval or
block outright when it falls outside that range — regardless of whether
every other check passed.

This catches a distinct failure class from functional testing: a script bug
that deletes every row instead of the intended few, a config generator that
emits a wildly different file because an upstream input changed unexpectedly,
or a bulk data import where a bad source batch replaces far more records than
normal churn would explain. None of these are necessarily *invalid* by
schema or syntax — they are correctly-formed changes that are implausibly
large.

## Where to apply it

- **Config changes**: gate on lines changed or percentage diff versus the
  previous version, not just whether the new file parses.
- **Bulk data imports**: gate on the percentage of records a scheduled import
  would add, modify, or remove versus the normal baseline churn rate (e.g.
  require manual approval if a weekly import would change 30%+ of records
  when normal churn is under 20%) — this is a targeted defense against a bad
  upstream source batch or a pipeline bug, independent of whatever
  per-record quality filtering (accept/reject lists) already exists for
  individual record correctness.
- **Any automated pipeline step that generates or transforms output at
  scale**, where the generator itself could have a bug that produces a
  technically-valid but far-too-large or far-too-small result.

## It is inherently reactive

Like most pre-checks, a change-magnitude gate is usually added only after a
specific incident exposes the gap it would have caught — there's no way to
enumerate every plausible threshold in advance. Treat the absence of a
magnitude gate on a given change path as a known gap rather than an oversight
to be embarrassed about, and add the gate as a concrete follow-up once a
runaway change actually gets through.

## Complementary to, not a replacement for, review

A change-magnitude gate is a mechanical backstop, not a substitute for
[mandatory code review](mandatory-code-review.md) — it exists specifically
for the cases a human reviewer or a correctness test wouldn't catch, because
the change looks fine in isolation and only its *scale* is the problem.
