---
type: concept
title: Reusable Platforms over Bespoke Scripts
description: >
  Building automation as a reusable platform framework that many teams can
  build on captures more value than writing a one-off script tied to a
  single service, at the cost of needing genuine software-engineering
  investment to build.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 18"
---

# Reusable Platforms over Bespoke Scripts

A script written to solve one service's operational problem solves that
one problem. The same engineering effort aimed at a reusable platform
framework — one that exposes the automation as something other teams can
adopt for their own services — multiplies its payoff across every team that
uses it, without each of them re-solving the same problem in their own
one-off way.

This is the practical target of moving up the [automation maturity
spectrum](automation-maturity-spectrum.md): the "internal service
automation" and platform stages are valuable specifically because they're
built to be reused, not because they're more sophisticated for its own
sake. Reaching that stage well requires [treating the platform as
production software](software-engineering-rigor-for-ops-tooling.md) — a
tool other teams depend on can't be maintained the way a personal script
can. It also usually requires [uniformity across what the platform
operates on](uniformity-as-automation-prerequisite.md): a platform that has
to special-case every team's differences ends up as complex as the scripts
it was meant to replace.

The reuse payoff doesn't mean building the biggest platform possible up
front, though — start from the [thinnest viable
platform](thinnest-viable-platform.md) that solves the real problem, and
grow it only as consuming teams' demonstrated needs justify the added
investment.
