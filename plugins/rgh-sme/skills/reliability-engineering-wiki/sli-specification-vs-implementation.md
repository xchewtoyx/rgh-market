---
type: concept
title: SLI Specification vs Implementation
description: >
  What you want to measure (the SLI specification) and how you actually
  measure it (the SLI implementation) are separate decisions that trade off
  quality, coverage, and cost independently.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 7"
---

**Specification**: what you want to measure — e.g. "ratio of homepage loads
under 100ms."

**Implementation**: how you actually measure it — via server logs, black-box
probers, or client-side JS instrumentation. Each implementation choice trades
off measurement quality, coverage, and cost differently; see
[SLI measurement point selection](sli-measurement-point-selection.md) for how
those choices compare.

Keeping the two separate matters because the specification is what should
stay stable and discoverable (it's what stakeholders agree to), while the
implementation is free to change as tooling, cost, or coverage needs evolve
without that change looking like a change to the promise itself.

A related design question is where to draw the line between the indicator
and the objective in the first place — whether a percentile choice or
threshold lives inside the SLI or inside the SLO. Pushing such specifics out
of the SLI and into the SLO tends to preserve more flexibility to revise
targets later without losing historical comparability, particularly in
storage systems that cannot cheaply reprocess raw historical data. See
[SLO measurement infrastructure design goals](slo-measurement-infrastructure-design-goals.md)
for the broader implementation trade-offs this decision interacts with.
