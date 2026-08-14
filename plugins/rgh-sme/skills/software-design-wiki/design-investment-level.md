---
type: concept
title: How Much to Invest in Design
description: >
  A concrete guideline for strategic programming's investment mindset — spend
  roughly 10-20% of total development time on design, enough to compound into
  real benefit without badly hurting near-term schedules.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 3"
---

Neither extreme works: designing everything up front (the waterfall failure
mode — see [design is a continuous activity](continuous-design.md)) is known
not to work for software, but zero design investment is
[tactical programming](strategic-vs-tactical-programming.md), which decays
over time. The practical middle ground is to spend about 10-20% of total
development time on design investment — small enough not to badly hurt
schedules, large enough to compound into a real benefit — and to expect
initial projects to run 10-20% longer than a purely tactical approach would.

The payoff has a timeline, not an instant return: benefits start appearing
within a few months, and the investment effectively becomes "free" once the
time saved from earlier investments covers the ongoing cost of new ones — at
which point strategic development is running faster than the tactical
baseline it's compared against (roughly 10-20% faster, by the same estimate).
The mirror-image failure mode is tactical programming's fast start followed by
a decay in development speed as complexity accumulates, eventually landing at
least 20% below what strategic development would have achieved for the rest
of the system's life.
