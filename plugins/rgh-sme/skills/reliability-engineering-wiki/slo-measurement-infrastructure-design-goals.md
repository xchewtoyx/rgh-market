---
type: concept
title: SLO Measurement Infrastructure Design Goals
description: >
  Six properties any SLO measurement implementation should be judged
  against — flexibility, testability, freshness, cost, reliability, and
  organizational constraints.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 7"
---

1. **Flexible targets** — operators must be able to adjust thresholds,
   percentiles, and aggregation windows without code changes or redeploys,
   and historical performance should remain visible across a target change
   so the evolution of the target itself stays traceable.
2. **Testable targets** — the ability to backtest a candidate
   SLI/SLO/threshold against historical data before committing to it; never
   set a target or alert threshold without a way to estimate the resulting
   alert frequency. See
   [choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md).
3. **Freshness** — how much lag exists between real production behavior and
   the SLO reflecting it. Required freshness varies: monthly management
   reporting can tolerate high lag, business-critical firefighting needs
   near-real-time data.
4. **Cost** — the data-engineering cost of flexible/testable/fresh SLOs at
   scale can be significant, across time-series data, structured logging
   data, and the easily-undervalued opportunity cost of engineers' own time.
5. **Reliability** — the measurement infrastructure itself needs its own
   reliability target; it's meta — the system tracking reliability must be
   among the most reliable systems run. Practical tip: when the SLO pipeline
   itself has an outage and can't reconstruct historical state, exclude that
   window from longer-term compliance math (adjust the denominator) rather
   than guessing at what happened.
6. **Organizational constraints** — non-technical policy constraints (data
   residency requirements, mandated vendor/database choices, data-silo
   consolidation mandates) often restrict the implementation design space in
   ways that only surface late if this isn't checked early.

These goals sit on the implementation side of
[SLI specification vs implementation](sli-specification-vs-implementation.md)
— they're a checklist for evaluating *how* an SLO gets measured, independent
of what it measures.
