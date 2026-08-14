---
type: concept
title: Cost of Nines
description: >
  The cost of each additional nine of reliability rises non-linearly, so
  moving from 99.9% to 99.99% requires roughly ten times the rigor of the
  step before it, not merely twice as much.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 2"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3"
---

Going from 99.9% to 99.95% is a 2x reduction in allowed unreliability;
99.95% to 99.99% is a further 5x reduction. So the jump from 99.9% straight
to 99.99% requires roughly 10x the engineering rigor, not the ~2x that
"one more nine" intuitively suggests. Financial costs (redundancy, testing,
staging/canary infrastructure) and human costs (on-call burden, follow-the-
sun staffing) both scale steeply as targets approach 100%, while marginal
user-perceived benefit falls toward zero.

This is the quantitative backbone of why
[100% reliability is the wrong target](hundred-percent-reliability-is-the-wrong-target.md):
extreme reliability increases system complexity and cost exponentially while
delivering diminishing, then zero, perceptible value to users.

Practical consequence for target-setting: it's often more useful to start
from a *time budget* you find acceptable (e.g. "about two hours of
unreliability a month is fine") and reverse-derive the percentage, rather
than picking a percentage first and discovering later what it actually
costs — see
[nines vs time-budget framing](nines-vs-time-budget-framing.md) and the
[availability table](availability-table.md) for exact time limits.

The same non-linearity shows up in composed dependencies: see
[dependency reliability composition](dependency-reliability-composition.md)
for how stacking several "reasonable" per-component targets erodes an
end-to-end guarantee faster than intuition suggests, and
[independent failover reliability composition](independent-failover-reliability-composition.md)
for how adding an independent failure domain buys back nines far more
cheaply than hardening a single component. The same non-linear cost also
shows up inside a single replicated, coordinated dependency — see the
[quorum replica-count reliability tradeoff](quorum-replica-count-reliability-tradeoff.md)
for why tolerating one more failure in a quorum system costs two more
replicas and a disproportionate amount of write throughput, not a smooth
incremental cost.
