---
type: concept
title: The Efficiency–Thoroughness Trade-Off (ETTO)
description: >
  Hollnagel's principle that being maximally efficient and maximally thorough
  at the same time is not a solvable problem, so every operator and manager
  is continuously trading one against the other, usually invisibly.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 2"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 12"
---

Hollnagel's efficiency–thoroughness trade-off (ETTO) principle: "If anything
is unreasonable, it is the requirement to be both efficient and thorough at
the same time — or rather to be thorough when with hindsight it was wrong to
be efficient." No fixed procedure or "best practice" resolves this in
advance; operators and managers continuously adjust how much time and
checking a task gets to match immediate conditions, and that adjustment *is*
the trade-off, made afresh each time rather than settled once. This is the
mechanism underneath [goal conflicts and production
pressure](goal-conflicts-and-production-pressure.md): what later reads as a
shortcut is usually an ETTO that was reasonable given the information and
time actually available in the moment ([local
rationality](local-rationality-principle.md)).

**Why "best practices" and silver bullets don't dissolve it.** Decision-makers
routinely search for a mechanism that advances efficiency and thoroughness
simultaneously, without trade-offs — a silver bullet. None exists, because
the two pull in the same organisation on different timescales:

- **Acute goals** (timely, efficient, cheap): short-term, easily measured by
  counting discrete elements — throughput, delay, cost.
- **Chronic goals** (safety, quality, equity): long-term, emergent properties
  of how components, software, and people interact over time, not reducible
  to a single count.

Acute goals are structurally easier to demonstrate progress on, so they
dominate unless chronic goals are protected as explicit cultural
commitments rather than left to compete as ordinary metric targets — a metric
target erodes under efficiency pressure the same way any other acute goal
does, which is a form of [goal displacement in safety
metrics](goal-displacement-in-safety-metrics.md).

**The measurement asymmetry that keeps ETTOs invisible.** Production signals
are clear, immediate, and backed by established historical baselines — a
missed deadline is obvious the day it happens. Safety signals are weak,
indirect, and lack robust leading indicators — the return on a safety
investment is a non-event that never shows up as a number until [rare
outcomes stop confirming the trade-off was
safe](rasmussen-boundary-model.md). Layering multiple unintegrated "best
practice" standards onto operations does not resolve this asymmetry; it adds
competing goal structures that increase brittleness rather than resolving
the underlying trade-off.

Because ETTOs cannot be eliminated, the organisational lever is not to demand
"safety first" but to make the trade-off visible and occasionally reverse it
on purpose — see [sacrifice judgements](sacrifice-judgements.md). Punishing
an ETTO after the fact, once an accident reveals it was the wrong call in
hindsight, is the [authority–responsibility
mismatch](authority-responsibility-mismatch.md): the organisation is
condemning the same daily trade-off it commissioned.
