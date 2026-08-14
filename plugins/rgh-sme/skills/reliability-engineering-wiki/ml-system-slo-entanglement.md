---
type: concept
title: ML System SLO Entanglement
description: >
  An ML system is typically entangled with adjacent systems across the
  business, so beyond the smallest deployments it's generally impractical to
  set an SLO for the ML system without also setting SLOs for the systems
  around it.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

ML systems tend to be entangled across the rest of the business they serve —
their outputs feed, and are fed by, other systems that were not designed or
owned as part of the ML system itself. A practical consequence for
[SLO count and scope](slo-count-and-scope.md): for anything beyond the
smallest ML deployments, it's generally impractical to specify an SLO for the
ML system in isolation without also specifying SLOs for the adjacent systems
it's entangled with — an ML SLO that only covers the model-serving boundary
can look healthy while the business outcome it's meant to protect is not,
because the failure is entering or leaving through one of those entangled
neighbors instead.

This compounds the case made in
[ML SLOs scoped to business outcome](ml-slo-scoped-to-business-outcome.md)
for scoping around the business objective rather than the model in
isolation: the entanglement is exactly why a model-only scope tends to be too
narrow to say anything trustworthy about that objective.
