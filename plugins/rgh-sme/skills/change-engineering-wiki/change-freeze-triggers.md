---
type: concept
title: Change Freeze Triggers
description: >
  Conditions that should automatically suspend non-essential releases —
  an active incident on the system, or exhaustion of its error budget —
  until the underlying condition clears.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 13"
---

# Change Freeze Triggers

Two conditions that should suspend ordinary releases until they clear:

- **During an active incident**: avoid deploying further changes to the
  affected system except a rollback of the specific change suspected to
  have caused the incident. Every other in-flight change adds a new
  candidate cause into an already-uncertain situation, which is exactly
  the moment you can least afford new uncertainty. This is a narrower rule
  than a full freeze — it explicitly still permits the one change most
  likely to resolve the incident: [rolling back](rollback-vs-roll-forward.md)
  the suspect release.
- **On error-budget exhaustion**: when a system's error budget is spent for
  the measurement window, non-essential releases halt until the budget
  recovers — typically P0 fixes and security patches remain exempt. A
  worked example policy: at or above SLO, releases proceed normally; error
  budget exhausted over the trailing window means halt all changes/releases
  except P0 issues and security fixes until back within SLO. Whether the
  team *must* pivot to reliability work or *may* keep shipping features
  during exhaustion typically depends on cause (a code or process bug
  forces the pivot; an out-of-scope cause like a company-wide network
  incident or another team's already-frozen failure does not). The budget
  itself, and the policy for when it's considered exhausted, is
  `reliability-engineering`'s concern; the release-halt mechanism this
  triggers — an automated or process-level gate that blocks deploys — is
  the change-engineering side of the same policy.

Both are narrower and more targeted than the blanket, calendar-driven
freeze windows that [change approval board pathology](change-approval-board-pathology.md)
describes as risk-management theater: they trigger on an actual, current
risk signal rather than a fixed schedule, and they lift automatically once
the signal clears.

For embedded and physical systems, a further, per-device gate applies
below the fleet level: see [update safe-state gating](update-safe-state-gating.md)
for why a single device may need to refuse an otherwise-approved update
based on its own current physical operating state.
