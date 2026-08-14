---
type: concept
title: Error Budget
description: >
  The amount of unreliability a service is allowed over a measurement window,
  computed as one minus its SLO target, spent down by bad events and refilled
  as they roll out of the window.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3, ch. 1"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1, ch. 5"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

```
Error budget = 1 − SLO
```

A 99.9% SLO over a 30-day window yields a 0.1% budget — about 43.2 minutes
of allowed downtime, or 1,000 failed requests per 1,000,000. This is a direct
consequence of never [targeting 100%](hundred-percent-reliability-is-the-wrong-target.md):
some nonzero unreliability is expected and budgeted for in advance rather than
treated as an unplanned failure every time it occurs.

## Two calculation styles

- **Events-based**: `(bad events / total events)`, compared against `1 − SLO`.
  Subtracting gives budget remaining (positive = surplus, negative = deficit);
  dividing remaining by total budget gives % of budget left.
- **Time-based**: pick a base time unit, multiply out to the full window
  (adjusted for actual sample resolution) to get total possible data points,
  then multiply by `1 − SLO` to get the budget in units of time.

## Terminology

- **Surplus** — budget remaining.
- **Deficit** — budget exceeded (negative remaining).
- **Burn** — any consumption of budget; see [burn rate](burn-rate.md) for how
  fast that consumption happens relative to what's sustainable.
- **Recovery** — budget regained as old bad events age out of a rolling
  window.

## Excluding known non-reliability windows

Services with an accepted, communicated maintenance window (e.g. nightly
2–4am) should exclude that window from the error-budget calculation entirely,
rather than loosening the target to quietly absorb it — the target should
describe what's actually promised the rest of the time.

## What the budget is for

A surplus signals room to ship features, take risks, and experiment; a
deficit signals a shift toward reliability work. This basic framing is
useful as a starting heuristic but is deliberately naive — see
[error-budget-driven prioritization](error-budget-driven-prioritization.md)
for the more nuanced uses, and [error budget policy](error-budget-policy.md)
for how the response is formalized. Error budget is jointly owned between the
team building features and the team (or role) defending reliability, which
converts what used to be organizational friction into a shared, quantitative
contract.
