---
type: concept
title: Uniformity as an Automation Prerequisite
description: >
  Automation is cheapest to build and safest to run when the things it
  operates on are interchangeable, so converting special-cased "snowflakes"
  into uniform, identically-handled instances is often the real
  prerequisite work before automating at all.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 6"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

# Uniformity as an Automation Prerequisite

The "pets vs. cattle" framing is usually stated as an infrastructure design
principle, but it is just as much a precondition for
[automation](value-of-automation.md) to be worth writing. See [pets versus
cattle](pets-vs-cattle.md) for the full distinction — interchangeable
replicas automation can replace without manual nursing versus servers that
accumulate unique state. A script or service that has to special-case every
exception ends up encoding as much branching logic as the manual process
it was meant to replace — the automation gets complicated in direct
proportion to how non-uniform its inputs are.

This makes converting exceptions into the common case — "melting
snowflakes" — a distinct piece of automation work in its own right, done
*before* or *alongside* writing the automation rather than assumed as a
given. Retooling automation to absorb an edge case uniformly, instead of
special-casing around it, keeps that conversion happening continuously
rather than as a one-time cleanup that erodes again over time. It carries a
real upfront conversion cost — migrating existing non-uniform instances
into the uniform shape — which is why it competes for priority against just
writing the automation and living with its exception-handling branches.

This is a large part of why [reusable platforms cost more up front than
bespoke scripts](reusable-platforms-over-bespoke-scripts.md): a platform
serving many teams has to either enforce uniformity across its users or
absorb their differences as complexity, while a one-off script can often
get away with matching one team's specific, non-uniform reality.

Uniformity doesn't always have to be forced through a one-time migration
before automation starts — sometimes automating just the common case is
what *creates* the uniformity, by making the "special" cases voluntarily
disappear. One team facing three manually-defended VM-provisioning paths,
each defended by its users as uniquely necessary, stopped trying to
automate all three up front and instead automated only the common path
(dropping provisioning time to minutes, no sysadmin required, able to run
nights and weekends). Both "edge case" groups then quietly adopted the
automated common path themselves, because it was simply better than what
they'd been defending — and the edge cases never needed automating at all.
The lesson generalizes: don't assume every exception needs to be absorbed
before automation is worth building; a sufficiently good common-case
automation can dissolve exceptions by making them not worth keeping. See
[toil triage categories](toil-triage-categories.md) for where this fits
among the other choices available for a given piece of toil.
