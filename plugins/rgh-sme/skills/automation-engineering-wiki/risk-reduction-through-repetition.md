---
type: concept
title: Risk Reduction Through Repetition
description: >
  The instinctive response to a risky procedure is to do it less often, but
  that concentrates more change into each attempt and lets skill decay
  between attempts — doing it smaller and more often is usually safer.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), Preface; ch. 8"
---

# Risk Reduction Through Repetition

When a procedure feels risky, the instinctive reaction is to do it less
often — fewer releases, fewer failovers, fewer changes. This instinct
backfires. Doing a risky thing less often doesn't remove the risk, it just
batches it: each attempt now bundles more simultaneous change (harder to
isolate a fault in), is executed by people with less recent practice (more
likely to make an execution mistake), and is exercised by tooling that gets
correspondingly less real-world validation between uses. The alternative —
doing the risky thing in smaller increments, more frequently — trades a
rare, high-stakes, poorly-practiced event for a routine, low-stakes,
well-practiced one.

This shows up as the same underlying pattern across several different
procedures:

- **Releases**: many small releases beat a few large ones — each is easier
  to isolate faults in if something breaks, and the release *process*
  itself gets exercised often enough to actually improve, rather than
  staying rusty between rare, high-stakes attempts.
- **Failover and disaster recovery**: a database failover or full
  disaster-recovery cutover rehearsed regularly is one the team can execute
  calmly under real pressure; one attempted for the first time during a
  real incident is a coin flip.
- **Automated safeguards generally**: see [confidence decay in unpracticed
  safeguards](confidence-decay-in-unpracticed-safeguards.md) for why any
  countermeasure that only runs during emergencies needs this same
  treatment.

The mechanism is twofold: repetition keeps the *people* executing the
procedure skilled at it (the inverse of the skill atrophy described in
[automation bias](automation-bias.md)), and it keeps the *procedure and its
tooling* under continuous real-world validation instead of going stale
between rare uses. Both effects point the same direction — toward doing the
risky thing more, in smaller pieces, rather than less, in bigger ones.

This principle motivates moving up the [automation maturity
spectrum](automation-maturity-spectrum.md) in the first place: automating a
procedure is what makes running it far more often actually affordable, since
a human repeating a multi-step procedure daily is expensive in a way a
machine repeating it is not.
