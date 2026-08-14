---
type: concept
title: Interrupt Shielding
description: Designating one on-call role to absorb tickets, requests, and non-paging interrupts so the rest of the team can protect uninterrupted engineering time.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 29"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan), ch. 7"
---

Uncontrolled interrupts — tickets, user requests, chat pings, non-paging
operational queries — destroy the sustained focus multi-week engineering
projects need, both by directly consuming time and by imposing a context-
switching cost each time attention has to jump back and forth. Left
unmanaged, this is a major contributor to [operational
overload](operational-overload-recovery.md) even when no single interrupt
looks individually large.

**Interrupt shielding** designates a single role per shift — often the
secondary on-call — to absorb all incoming non-paging interrupts, while
every other engineer on the team is explicitly protected from them to do
uninterrupted project work. Two supporting practices make the shielded
role sustainable rather than just relocating the overload onto one person:

- **Batch, don't react**: process routine tickets in scheduled blocks
  rather than handling each one the moment it arrives, which itself
  reduces the number of context switches even for the person whose job it
  is to handle them.
- **Treat every recurring interrupt as a bug to eliminate**: a routine
  manual request that shows up weekly is a sign that a self-service tool
  or automated workflow should exist. The fix isn't handling the ticket
  faster — it's reducing the [pager load](pager-load-management.md)-style
  interrupt rate itself so the same request stops generating tickets at
  all.

### Splitting emergency response from ticket triage

A fuller version of the same design splits the shielding role in two: at
any moment, exactly one person has emergency response (paging incidents) as
their top priority, one other person has non-urgent ticket triage as their
top priority, and everyone else does uninterrupted project work — rather
than the whole team perpetually firefighting together with zero project
bandwidth. A team of eight rotating through one-week shifts, for example,
gives each person one on-call week, one ticket-duty week, and six project
weeks per cycle; the two interrupt-facing roles hand off individually
(not as a group meeting) to keep shift changeover simple. A rule of thumb
for catching drift back into overload: **if combined on-call and ticket-duty
time exceeds roughly a quarter of the team's total capacity, that itself is
a symptom of a firefighting problem**, not a staffing level to just accept —
see [operational overload recovery](operational-overload-recovery.md) for
what to do once that threshold is crossed. Both interrupt-facing roles carry
their own explicit exit discipline: an on-call shift closes out each paged
incident with an alert-journal entry, a follow-up bug for anything patched
rather than fixed, and — for anything user-visible — a [blameless
postmortem](blameless-postmortems.md); a ticket-duty shift aims not just to
close tickets but to eliminate the need for the next one, since a request
that keeps recurring is itself a signal of a missing self-service path or
documentation gap.
