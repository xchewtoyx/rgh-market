---
type: concept
title: Compliance Requirements as SLOs
description: >
  Framing an externally-imposed compliance requirement as an SLO, and the
  reporting that demonstrates it as the underlying SLI, lets compliance work
  be tracked with the same machinery and rigor as ordinary reliability work
  instead of as a separate, ad hoc process.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 2"
---

Policy and compliance requirements (data residency, retention limits,
consent handling) typically originate outside engineering — legal, a
regulator, a national government — but the ongoing work of demonstrating
compliance is still a measurable, trackable engineering activity. Framing it
in [SLO](service-level-objective.md) terms makes that explicit: the
compliance requirement becomes the target, and the reporting that establishes
current implementation status against it becomes the
[SLI](service-level-indicator.md).

This is a framing move, not a new kind of target — it reuses ordinary
SLI/SLO machinery for work that would otherwise sit in a separate compliance
process with its own ad hoc tracking, which normalizes that work alongside
the rest of a service's reliability reporting rather than treating it as a
special case. This is distinct from an [SLA](sla-vs-slo.md): a compliance
requirement typically carries legal consequences for non-compliance the way
an SLA does, but framing the associated engineering work as an SLO/SLI pair
is what makes that work observable and manageable day to day.
