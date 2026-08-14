---
type: concept
title: Toil
description: >
  Toil is operational work that is manual, repetitive, automatable,
  reactive, produces no enduring value, and grows linearly with the system
  it supports.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 5, 29"
---

# Toil

Toil is the specific kind of operational work tied to running a production
service that has all of these characteristics at once:

1. **Manual** — executed by hand (running a script manually, editing a
   database schema by hand).
2. **Repetitive** — the same task performed over and over, not a one-off.
3. **Automatable** — a machine could do it as well as a human could; there's
   no judgment call that requires a person. This is the property that makes
   toil a target for the [automation maturity
   spectrum](automation-maturity-spectrum.md) — moving a toil task up that
   spectrum is what eliminates it.
4. **Tactical** — reactive, interrupt-driven work (handling a ticket,
   responding to an alert) rather than planned.
5. **No enduring value** — the system is in the same state after the task as
   it would need to be in again next time; nothing about the architecture
   or tooling improved. This is what separates toil from [engineering
   work](engineering-work-vs-toil.md).
6. **Scales linearly** — the amount of it grows O(N) with traffic, machine
   count, or user count, rather than sublinearly.

Because toil scales with the system rather than shrinking as the system
matures, an organization that doesn't actively eliminate it ends up needing
proportionally more people just to keep operating at the same level of
service — see [the case for eliminating toil](case-for-eliminating-toil.md).
Organizations that track this explicitly cap how much of it they'll
tolerate; see the [toil budget](toil-budget.md).

A useful trigger for spotting it in the wild: treat every *recurring*
interrupt — the same manual request submitted again and again by users or
other teams — as a bug report about a missing tool, not as routine
workload to staff for. One team member absorbing all such interrupts for a
shift (shielding the rest of the team's focus) makes the volume visible
without eliminating it; writing a self-service tool or automated workflow
for the specific recurring request is what actually eliminates it.

Not every piece of toil gets the same response, though — see [toil triage
categories](toil-triage-categories.md) for sorting a backlog into what to
automate now, what isn't worth automating, and what can only be
streamlined rather than automated away.
