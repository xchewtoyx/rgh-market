---
type: concept
title: Legacy System Automation Pathway
description: >
  Automating away a legacy system that can't simply be replaced outright
  moves through recognizable stages — avoidance, encapsulation, replacement,
  then retirement of the stragglers — rather than one big migration.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 6"
---

# Legacy System Automation Pathway

A legacy system that's generating [toil](toil.md) — expensive, fragile,
manually operated — usually can't be automated away or replaced in one
step, because it has too many existing users and too much accumulated
special-case behavior to migrate atomically. A staged pathway manages that:

1. **Avoidance** — stop new work from depending on the legacy system,
   even while existing usage continues, so the problem stops growing while
   a real fix is built.
2. **Encapsulation / augmentation** — wrap the legacy system behind a
   defined API or add monitoring around it, without changing its internals.
   This buys visibility and a stable interface for the next stage to target,
   at low risk. It's a way of refinancing the toil "debt" at a lower
   ongoing interest rate rather than paying it down yet.
3. **Replacement / refactoring** — build the real alternative
   incrementally, behind the common interface encapsulation already
   established, migrating traffic gradually (e.g. via canary or blue-green
   cutover) rather than in one cutover.
4. **Retirement / custodial ownership** — the small remainder of usage that
   resists migration gets quarantined and handled as a special, low-priority
   case, rather than blocking retirement of the legacy system for everyone
   else.

The value of treating this as distinct stages, rather than one "migrate
everything" project, is that most of the payoff — stopped growth, restored
visibility, a stable interface — arrives at stage 2, long before the harder
replacement work in stage 3 is finished. It also keeps the small number of
stragglers in stage 4 from holding the whole effort hostage: a system
doesn't need 100% migration to be considered successfully replaced, it
needs the stragglers isolated so they stop being everyone else's problem.
