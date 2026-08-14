---
type: concept
title: Thinnest Viable Platform
description: >
  Start an internal automation platform at the smallest scope that solves
  consumers' real problem — even just a documented convention — and grow it
  only as consuming teams' needs actually justify more investment.
sources:
  - title: Team Topologies, Second Edition
    resource: "Team Topologies, Second Edition (Skelton, Pais), ch. 5"
---

# Thinnest Viable Platform

A platform doesn't have to start as a dedicated team running dedicated
infrastructure. The simplest viable version can be a wiki page documenting
which components/services to use and how — if the underlying pieces already
work reliably, no dedicated automation or team is needed yet. As the
underlying substrate grows more complex (even when parts of it are
outsourced or vendor-provided), a platform team adds a genuine management
abstraction; further investment (custom integration, self-service APIs,
automated provisioning) is added only as consuming teams' actual needs
justify it.

This is a direct application of the same judgment call every step up the
[automation maturity spectrum](automation-maturity-spectrum.md) requires:
building [reusable platforms over bespoke
scripts](reusable-platforms-over-bespoke-scripts.md) pays off only once
there's real reuse to capture, and over-building a platform ahead of that
demand wastes the same engineering time that a toil-focused team is trying
to protect via its [toil budget](toil-budget.md). A platform that grows past
what consumers actually need starts imposing its own cognitive tax —
mandatory ceremony, unused flexibility, features nobody asked for — which
looks a lot like the toil it was built to remove, just relocated onto the
platform team instead of eliminated. The failure mode runs in both
directions: too thin, and teams fall back to solving the same problem
bespoke, one-off, per team; too thick, and the platform team spends its
budget maintaining unused surface area instead of the reliability and
usability that make the platform worth adopting in the first place.

Treating the platform itself as a live product — not a one-time build — is
what keeps this calibration honest over time: the same [software-engineering
rigor expected of any operational
tooling](software-engineering-rigor-for-ops-tooling.md) applies, plus an
explicit channel for the platform's own users (the teams consuming it) to
report friction and shape the roadmap, since a platform that only ever grows
in response to its builders' assumptions — rather than consumers' demonstrated
needs — tends to overshoot the thinnest viable scope.
