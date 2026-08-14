---
type: concept
title: Confidence Decay in Unpracticed Safeguards
description: >
  A countermeasure that only runs during a real emergency — a failover, a
  restore, a manual override — silently loses reliability between
  incidents, so it needs to be exercised deliberately rather than trusted
  on the strength of its last successful use.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), Preface; ch. 2, 6"
---

# Confidence Decay in Unpracticed Safeguards

A countermeasure that fires constantly (an auto-restart, a load-shedding
rule) gets continuously proven correct just by running. A countermeasure
that only fires during a genuine emergency — a database failover, a backup
restore, a manual kill switch — gets no such continuous proof. Between
incidents, the underlying system keeps changing (config drift, dependency
upgrades, topology changes) while the countermeasure itself sits untouched,
so confidence in it decays even though nothing about the countermeasure's
own code changed. The failure is discovered at the worst possible time:
during the real incident the countermeasure exists to handle, rather than
during a planned check.

The general fix is to convert "infrequent and untested" into "infrequent
but deliberately, regularly exercised" — scheduling planned exercises of
exactly the mechanisms that would otherwise only run once, for real,
without warning:

- **Fire drills / game days** — deliberately trigger the failure a
  safeguard is meant to handle (reboot a random production machine, force
  a database failover, kill a dependency) on a planned schedule, so a
  broken countermeasure is discovered at 10am on a Monday during a planned
  drill instead of at 4am during a real outage. One large-scale example of
  this turned into routine maintenance: draining and rebooting every
  machine in a fleet for a kernel upgrade every few months means every
  single machine gets a controlled, observed reboot on a predictable
  schedule, surfacing "won't boot after a power cycle" problems as a
  planned finding rather than as a surprise during a real, uncontrolled
  outage.
- **Frequently-triggered countermeasures should be automated outright** —
  automating a countermeasure that already fires often converts "confidence
  from repetition" into a structural guarantee instead of relying on it
  remaining habitual.
- **Overuse of a countermeasure is itself a signal** — a rate of triggering
  well above baseline usually indicates a deeper problem the countermeasure
  is quietly masking, not that the countermeasure is doing its job well.

This is the same underlying principle as [risk reduction through frequent
repetition](risk-reduction-through-repetition.md) — practicing a risky
procedure often is what keeps it safe — applied specifically to safeguards
and failure countermeasures rather than to routine changes like releases.
It's also a structural alternative (or complement) to [crash-only
software](crash-only-software.md): where crash-only design removes the
untested path by construction, fire drills keep a path that can't be
removed — like a physical failover — honest through repetition instead.
Left unaddressed, an unpracticed safeguard compounds with [automation
bias](automation-bias.md): the people who would need to operate it
manually if it failed have also had no recent practice exercising it.
Scheduling the drill is necessary but not sufficient — see [unbriefed
surprise exposure](unbriefed-surprise-builds-uncertainty-competence.md) for
why a drill that's pre-briefed and scripted still leaves the operator's
general adaptive competence untested, even when it successfully verifies
the mechanism itself.
