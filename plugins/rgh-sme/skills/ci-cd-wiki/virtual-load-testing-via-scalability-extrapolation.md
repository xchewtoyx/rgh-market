---
type: concept
title: Virtual Load Testing via Scalability Extrapolation
description: >
  Fitting a small number of real load-test measurements to a simple
  contention-and-coherency scalability model to project throughput at loads
  beyond what the test environment or software licensing can physically
  generate, instead of building out full-scale capacity infrastructure.
sources:
  - title: Guerrilla Capacity Planning
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 6, appendix F"
---

# Virtual Load Testing via Scalability Extrapolation

A [nonfunctional test gate](nonfunctional-test-gate.md) is normally limited by
whatever load the test environment or load-generation tooling can actually
produce — full-fidelity capacity infrastructure (see
[capacity test environment fidelity](capacity-test-environment-fidelity.md))
is expensive, and licensed load-generation tools often cap the number of
virtual users a team can afford to simulate. Virtual load testing sidesteps
this: take a handful of real measurements at loads the environment *can*
reach (a statistical minimum of about four data points, spanning as wide a
load range as practical), fit them to a two-parameter scalability curve, and
use the fitted curve to project throughput at loads well beyond what was
physically tested.

The model has exactly two free parameters, deliberately kept minimal so the
fit is falsifiable rather than curve-fitted to noise:

- **Contention** — serialization overhead from shared resources (lock waits,
  a single execute queue) that grows with load even without any caching
  effects.
- **Coherency delay** — overhead from keeping shared, mutable state
  consistent across concurrent workers (cache-line invalidation, cross-node
  synchronization) that grows *faster* than contention as load increases,
  and is what eventually makes throughput curve back down as load keeps
  rising ("retrograde" scalability) rather than merely flattening out.

Fitting only two parameters to at least four points makes the result a
genuine falsifiable model, not an interpolation that is guaranteed to pass
through every point — the residual error between fitted and measured points
is itself useful evidence: a small residual across the measured range gives
real confidence in the extrapolated (unmeasured) region, while a poor fit is
a signal to investigate the measurement process before trusting any
projection at all.

## When it earns its keep

- Load levels of genuine interest exceed what the test lab, licensing, or
  hardware budget can generate directly.
- A team needs to decide, ahead of a capacity-driven procurement or
  architecture decision, whether a design will keep scaling or hit a wall —
  without first building the expensive environment that would prove it
  empirically.
- Distinguishing whether a plateau visible in the tested range is a genuine
  ceiling or an artifact of the specific configuration tested: recomputing
  the same two parameters across configurations (e.g. 4-way vs. 6-way vs.
  8-way) can reveal that an apparent saturation point in one configuration is
  actually a false alarm caused by unusually high coherency overhead specific
  to that configuration, not a fundamental limit of the workload.

## Limits

The projection is not a substitute for testing at the loads that matter most
to the release decision — it is a way to prioritize *which* loads are worth
testing directly, and to sanity-check a procurement or architecture decision
under time or budget pressure. It also has no diagnostic power beyond
flagging that contention or coherency dominates: once the model shows a
problem exists, root-causing *which* subsystem is responsible still requires
the kind of targeted investigation an
[automated performance regression gate](performance-regression-gate.md)'s
pitfall list already calls for.
