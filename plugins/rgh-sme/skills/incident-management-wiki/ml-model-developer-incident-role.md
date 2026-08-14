---
type: concept
title: Model Developer Incident Responsibilities
description: What a model developer or data scientist should prepare before an ML incident and how they participate once one is declared, distinct from their day-to-day modeling work.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

Data and modeling staff often prefer to avoid "operations" work, but become
unavoidably involved in incident response once ML matters to the
organization. Three preparations pay off specifically during incidents:

- Having historical model versions stored in ready-to-serve format is the
  single fastest mitigation available during a rapid, unexplained quality
  decline — reverting to a known-good prior model buys time to diagnose the
  real cause without leaving the outage live.
- A specified, tested fallback (even something as blunt as "no
  personalization") gives the incident commander a mitigation option that
  doesn't depend on this role being reachable. The fallback needs periodic
  testing, because as a model improves the gap to an untested fallback can
  grow large enough that the fallback itself becomes unacceptable to ship
  under pressure.
- Model-quality metrics chosen ahead of time to be independent of
  implementation detail are what let anyone — not just the person who built
  the model — recognize during an incident that the model itself, and not
  something downstream, has stopped working.

During an incident, this role explains how the model currently works and
generates or validates hypotheses about the cause; they need to be reachable
off-hours through an organized on-call rotation, though not expected to be
paged often if the preparation above was done. They may be asked to run
custom data analysis or produce model variants to test a hypothesis, but
should be prepared to push back on any request that would require violating
user privacy or another ethics principle rather than complying to resolve
the incident faster.

Post-incident, this role's highest-value recurring investment is shortening
the model-quality-evaluation loop — the delay between a change and its
evaluation — since a shorter loop speeds up resolution the next time a
quality regression happens, not just ordinary development.

See also [software engineer incident
responsibilities](ml-software-engineer-incident-role.md) for the adjacent
role that owns the systems moving data between these models.
