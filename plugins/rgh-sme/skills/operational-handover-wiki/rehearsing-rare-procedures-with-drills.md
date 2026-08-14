---
type: concept
title: Rehearsing Rare Procedures with Deliberate Drills
description: A recovery or failover procedure that is only ever invoked during a real emergency loses reliability over time, so it must be exercised on a schedule via deliberately induced failures.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), Preface; ch. 1; ch. 8"
---

Every documented failure mode should have a countermeasure, but the countermeasures that run constantly are not the risky ones — automation and frequent use keep them correct, because anything broken about them surfaces quickly. The dangerous countermeasures are the ones that exist for rare situations: a database failover procedure, a datacenter evacuation, a restore from backup. Confidence in a rarely-used procedure decays over time as the system around it changes and nobody notices the procedure no longer matches, precisely because nobody has had occasion to run it.

## The Practice

Counter this by periodically and deliberately exercising rarely-used procedures on a schedule, via intentionally induced failures — a "fire drill" — rather than waiting for a genuine emergency to be the first real test since the last one. The underlying principle: risk goes down with repetition, not with avoidance. A team's instinct when a procedure feels risky is often to do it as rarely as possible; the opposite response — doing it more, on purpose, in a controlled setting — is what actually keeps it safe.

The payoff is in when the failure is discovered. Finding out a database failover script no longer works during a planned Monday 10am drill is a minor inconvenience with time to fix it calmly. Finding out during an actual 4am Sunday outage compounds an already-bad situation with a broken safety net.

## Relationship to Other Maintenance Practices

This is distinct from [Mandatory Staging/Simulation Testing](runbook-checklist-design.md) for a *new* checklist, which validates a procedure once before it's deployed. Rehearsal via drills is the ongoing discipline applied to a procedure that is already deployed and presumed to work, to catch the drift that accumulates as the surrounding system changes underneath it. A procedure that passed its initial staging test can still silently rot if it is never run again until the day it's actually needed.

Drilling a procedure also surfaces whether its documentation has kept pace with the real system — a runbook that no longer matches what the drill operator actually had to do is a concrete, dated signal to fix the document immediately, rather than a vague sense that "the docs might be stale."

A related, quieter risk affects the schedule around a procedure rather than the procedure itself: see [Decremental Drift in Maintenance Intervals](decremental-drift-in-maintenance-intervals.md) for how the interval between required maintenance or inspection steps can erode through many small, individually-reasonable relaxations until a once-adequate margin is gone, with no single step ever looking like the decision that removed it.
