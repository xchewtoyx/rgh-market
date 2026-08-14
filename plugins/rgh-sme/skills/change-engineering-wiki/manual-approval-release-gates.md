---
type: concept
title: Manual Approval Release Gates
description: >
  For sufficiently critical systems, require an explicit human sign-off
  between each stage of an otherwise automated rollout, rather than letting
  automated metrics alone decide progression.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 13"
---

# Manual Approval Release Gates

Automated [canary analysis](canary-metric-selection.md) is usually enough
to gate progression through a [staged percentage rollout](staged-percentage-rollout.md)
on its own. For a system whose full outage would be severe enough — Spotify's
event-delivery pipeline is a worked example: a full outage there would stall
every downstream data process that depends on it — the rollout instead
requires manual approval at each stage boundary (staging with mirrored
production traffic → canary on a small instance subset → full production),
in addition to the automated checks.

This is a deliberate trade against pure velocity: it caps how fast a change
can reach 100% of production regardless of how good the automated signal
looks, in exchange for a human explicitly taking responsibility for each
widening of blast radius. It's the release-gating analogue of
[peer review as change control](peer-review-as-change-control.md) — human
judgment applied at the point of highest leverage rather than as a blanket
policy on every change.

Because this gate trades speed for safety, it needs a narrow, audited
[emergency change breakglass](emergency-change-breakglass.md) escape hatch
for the case where an incident makes waiting for the next stage boundary
itself the bigger risk.

How much of the rollout needs a human gate is not fixed for the life of
the system: a smaller or newer team, or an unusually large/unusual
rollout, should default to manual review at each stage; as the automated
[canary](canary-metric-selection.md) signal builds a track record of
catching real problems, review can be pulled back and automation takes
over more of the progression, which directly raises the sustainable rate
of shipping. This mirrors the same earn-it-incrementally logic [migration
rollback testing cycle](migration-rollback-testing-cycle.md) applies to
migration automation — don't grant a gate full automation until the
thing it's gating has a proven record, but don't leave it permanently
manual once that record exists either.
