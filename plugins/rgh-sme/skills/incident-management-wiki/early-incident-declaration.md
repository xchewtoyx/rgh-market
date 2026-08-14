---
type: concept
title: Early Incident Declaration
description: Formally declaring an incident as soon as it is suspected, rather than waiting for certainty, because undeclared incidents miss coordinated response.
sources:
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 9"
---

Incidents should be declared early and often. An undeclared incident — one
being worked informally through a bug tracker or ad hoc chat rather than
through the [incident command system](incident-command-system.md) — misses
coordinated communication between teams, invites miscommunication, and
delays root-cause work because no one has explicit ownership of driving it
forward.

In one illustrative case, a rollout caused a quota-exhaustion bug that a
team debugged informally over a bug tracker; the rollout continued
unattended over a weekend, the symptom self-mitigated three separate times
through unrelated quota increases, and root cause wasn't found until day
four — all avoidable costs of not declaring formally on day one. Declaring
early also discourages ad hoc heroics (e.g., quietly firefighting through a
weekend) in favor of pausing risky changes until the situation is
understood, and centralizes communication in one place (a physical or
virtual "war room") instead of scattering it across side channels.

Having pre-agreed criteria for what counts as an incident — set in advance
from past outages and known high-risk areas, not improvised in the moment —
removes the hesitation that causes under-declaration. See
[incident severity classification](incident-severity-classification.md) for
how those criteria map to response structure.

Formal declaration is the escalation path for problems too large for an
informal first response. Before that point, [swarming](andon-cord-and-swarming.md)
— immediately pulling in help the moment something looks wrong, without
waiting for certainty or a formal trigger — is what catches most problems
early enough that they never need to become a declared incident at all.
