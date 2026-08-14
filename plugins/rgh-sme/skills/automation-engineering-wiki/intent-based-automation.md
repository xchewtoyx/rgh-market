---
type: concept
title: Intent-Based Automation
description: >
  An automation pattern where the system is given a high-level goal — an
  SLO, a growth forecast, a target state — and computes the low-level
  operational decisions itself, instead of being told the steps to execute.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 18"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Intent-Based Automation

Most automation is imperative: it executes a fixed sequence of steps a human
specified in advance. Intent-based automation inverts this — the operator
states a desired outcome (an SLO, a latency target, a capacity forecast) and
the system works out what changes are needed to satisfy it, re-deriving the
plan whenever the inputs or the current state change.

Google's Auxon is a worked example: instead of engineers manually computing
cluster resource allocations across dozens of services, they declare each
service's SLOs and growth forecasts, and Auxon computes the allocation. The
manual, error-prone version of this problem — hand-computed capacity plans
that go stale as soon as a forecast changes — is exactly the kind of
[toil](toil.md) this pattern is designed to remove.

The same pattern applies to **automated rightsizing** on a managed-compute
fleet: early schedulers took replica counts and CPU/RAM declarations from
engineers, but humans are poor at estimating resource needs, the cost of
determining those numbers scales with the number of services, and declared
configs drift from reality as programs grow organically — often until an
outage reveals that slack meant for spikes has been eaten. Automating
rightsizing well is surprisingly hard (some workloads remain too complex
for it), but when it works, most engineers stop hand-tuning sizing entirely
while complex cases stay possible — the same "easy things easy, hard things
possible" trade-off that makes [progressive compute
automation](progressive-compute-automation.md) worth building in stages
rather than all at once.

This sits at the advanced end of the [automation maturity
spectrum](automation-maturity-spectrum.md): it requires enough trust in the
automation's decisions that a human is no longer reviewing each individual
change, which raises the same need for
[safeguards against runaway automation](safeguards-against-runaway-automation.md)
as any other highly autonomous system. Autoscaling is the same pattern
applied specifically to capacity — see [autoscaling safety
practices](autoscaling-safety-practices.md) for the failure modes that come
with using a live load signal, rather than a forecast, as the input.

Intent-based automation is the same shape as [convergent
orchestration](convergent-vs-direct-orchestration.md): both compute their
own path toward a declared goal instead of executing a human-specified
sequence of steps. That shape is a poor fit for a procedure with
invariants that must hold mid-flight rather than just at the end — see that
note for when an explicit, ordered sequence is the safer choice instead.
