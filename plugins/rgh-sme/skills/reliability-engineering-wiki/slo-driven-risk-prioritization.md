---
type: concept
title: SLO-Driven Risk Prioritization
description: >
  Prioritizing reliability risk work by likelihood times impact against
  stated SLO commitments, rather than by intuition or anecdote, gives a
  bounded, defensible starting list rather than an exhaustive one.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 3"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 16, appendix A"
---

Risk management, in this framing, is the process of identifying, assessing,
and prioritizing threats to a service's [SLO](service-level-objective.md)
commitments, then applying resources to mitigate them — not an attempt to
eliminate all risk, since systems with zero stressors become brittle and
untested.

A four-stage bootstrapping cycle:

1. **Service risk evaluation** — for each service, ask: what are its SLOs?
   What does degraded or down look like at different affected-user
   percentages? What's the cost of downtime (revenue, customer retention,
   competitive alternatives)? Are there catastrophic risks (data loss,
   privacy breach)? Comparing services by peak dollar-loss-per-minute
   surfaces which deserves priority even when both "feel" important.
2. **Architectural inventory** — catalog the components, roles, interaction
   pathways, and background jobs that could threaten those SLOs.
3. **Risk prioritization** — `Risk = Probability × Impact`. To quantify risks
   for ranking, use a standardized risk assessment matrix:
   * **Probability of Occurrence within a Year**: Scale from Almost Never (0.0), Unlikely (0.2), Somewhat Unlikely (0.4), Likely (0.6), Highly Likely (0.8), to Inevitable (1.0).
   * **Impact to Organization**: Scale from Negligible (0.0), Minimal (0.2), Moderate (0.5), Severe (0.8), to Critical (1.0).
   * **Risk Ranking**: Calculated as `Probability × Impact` (ranging from 0.0 to 1.0). This quantitative rank orders the risk list from highest to lowest, serving as a guide for immediate remediation attention.
4. **Control and decision-making** — for each identified risk, choose
   avoidance (eliminate it), reduction (lessen its impact), or acceptance
   (tolerate it and plan for it).

This cycle is meant to run continuously, not once: periodic service delivery
reviews re-check risk tolerance against revenue/cost shifts, incident
postmortems feed newly discovered risks back into the prioritization list,
and new architecture gets risk-assessed as it's built — mirroring the same
continuous-iteration principle behind
[SLO evolution triggers](slo-evolution-triggers.md).
