---
type: concept
title: SLI Measurement Point Selection
description: >
  Where an SLI is measured — server-side, client-side, or via an external
  black-box prober — trades off representativeness of real user experience
  against cost and implementation complexity.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 9"
---

Common measurement points, roughly in order of how close they sit to the
real user experience:

- **Client-side instrumentation** — closest to what the user actually
  experiences (device, network, app), but harder to instrument reliably and
  subject to factors outside the service's control.
- **Server-side metrics** (request logs, RPC logs) — cheap and comprehensive,
  but blind to anything that happens between the server and the user (client
  network quality, DNS, CDN).
- **Black-box / synthetic probers** — external, realistic-but-artificial
  transactions run on a schedule; cover blind spots real traffic doesn't
  reach (low-traffic regions, off-peak times, rarely exercised paths) but
  don't reflect real user load or real user-side conditions.

Real User Monitoring (actual client traffic) and synthetic/canary monitoring
are complementary, not substitutes for each other — synthetic checks exist
specifically to cover the gaps real traffic leaves.

This is the "implementation" half of
[SLI specification vs implementation](sli-specification-vs-implementation.md):
the specification stays constant while the measurement point can be revised
as tooling and cost constraints change. Moving measurement closer to the user
is one of the standard remedies when an SLO turns out not to correlate with
real user pain — see
[identifying a miscalibrated SLO](identifying-a-miscalibrated-slo.md).

External [SLAs](sla-vs-slo.md) make the measurement boundary part of the
contract itself. A latency SLO might explicitly measure from request
arrival at the provider's endpoint to response being sent out, **excluding
network travel time** to and from the client — clarifying what the provider
controls versus what client-side conditions affect. Ambiguity here breeds
disputes and unrealistic expectations; spell it out in both the
[SLI specification](sli-specification-vs-implementation.md) and any
[violation-claims procedure](sla-violation-consequences.md).
