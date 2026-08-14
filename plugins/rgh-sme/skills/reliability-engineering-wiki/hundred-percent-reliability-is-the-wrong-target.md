---
type: concept
title: 100% Reliability Is the Wrong Target
description: >
  A 100% SLO is always the wrong choice — it's unreachable, provides no
  perceptible benefit past what users can even notice, and forbids the
  change that services actually need to improve.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3, ch. 1"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1, ch. 2"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

Nothing is 100% reliable, and trying to be is prohibitively expensive — see
[cost of nines](cost-of-nines.md) for the quantitative reason why. But the
target is wrong even setting cost aside:

- **No marginal user value past a point.** A service's reliability only
  needs to match the user's perception of reliability. If a user's mobile
  network already fails 1–2% of the time, building 99.999% availability into
  the app behind it provides zero perceptible benefit — the user's own
  device/network is the binding constraint.
- **It forbids all change.** A literal 100% target treats every change as
  unacceptable risk, since change is empirically the largest cause of
  outages. A team held to 100% is forced into a purely reactive posture,
  unable to ship anything.
- **It doesn't survive contact with leadership incentives.** Demanding
  perfection from an organization creates incentives for people to misreport
  or fudge metrics to look like they're hitting an impossible goal, or to
  become overcautious and slow to ship out of fear — neither improves actual
  reliability.

The alternative is deliberately choosing a target below 100% and treating
the gap as an [error budget](error-budget.md) — an explicitly allowed amount
of unreliability, spent on necessary change, that converts "when can we
ship" from an anxious guess into arithmetic.

Non-nines targets (99.97%, 98.62%, 87%) are completely legitimate — fixating
on "the number of nines" as the only acceptable vocabulary is itself a
symptom of chasing an unnecessarily strict target. See
[nines vs time-budget framing](nines-vs-time-budget-framing.md).
