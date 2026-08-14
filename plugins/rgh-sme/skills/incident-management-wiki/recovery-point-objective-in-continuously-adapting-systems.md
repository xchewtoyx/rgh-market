---
type: concept
title: Recovery Point Objective in Continuously Adapting Systems
description: Recovery time objective (RTO) still applies to ML incidents, but recovery point objective (RPO) mostly doesn't, because a continuously adapting system's only meaningful restore target is "now," which keeps moving.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

Two standard disaster-recovery concepts apply unevenly to ML incidents:

- **Recovery time objective (RTO)** — how long it will take to restore
  functionality after an outage — applies straightforwardly: retraining a
  model or copying in an older version both take real, estimable time.
- **Recovery point objective (RPO)** — the point in time the system can be
  restored *to* — mostly doesn't apply, for systems whose whole purpose is
  adapting to a currently-changing world. Outside of systems that run
  entirely on preexisting, static inputs, there is no fixed prior state
  worth restoring to; the only RPO that matters is "now," for an
  ever-changing "now." A model trained a few minutes ago might already be
  good enough for the current moment, or might not be — there's no way to
  know in advance the way a conventional system knows "yesterday's
  snapshot is fine."

This is the same underlying limitation as [ML rollback limits in a
changing world](ml-rollback-limits-in-a-changing-world.md), stated as a
standard disaster-recovery term: a conventional system's RPO is a fixed
target (the last good backup), while an ML system's implicit RPO target
keeps sliding forward in time even while the recovery is happening. That
significantly complicates how "resolved" gets defined for an ML incident
compared to a conventional one, where restoring a known prior good state
is a clear, sufficient resolution on its own.
