---
type: concept
title: Roll Back vs. Roll Forward
description: >
  When a change causes a production regression, reverting to the last
  known-good state is a safer default mitigation than pushing a forward
  fix, and designing releases to be cheaply revertible is what keeps that
  option available.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 8"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Roll Back vs. Roll Forward

When a release causes a production regression, there are two ways to stop
the bleeding: **roll back** (revert to the last known-good version) or
**roll forward** (push a fix on top of the bad version). "Detect, roll
back, fix, roll forward" is the safer default over "detect, continue
rolling forward" — a forward fix is itself an unverified change made under
time pressure, which carries its own risk of making things worse, while a
rollback returns the system to a state that was already verified to work.

This preference is only actionable if releases are designed to make it
true — it requires small, frequent, cheap-to-roll-back releases (see
[working in small batches](working-in-small-batches.md)). A release that
bundles a large batch of unrelated changes, or that has already made a
destructive, non-reversible mutation (e.g. dropped data, an unreversed
migration — see [expand-and-contract schema migration](expand-and-contract-schema-migration.md)),
cannot be cleanly rolled back regardless of intent.

Rollback is not always sufficient by itself (e.g. it doesn't undo data
corruption written by the bad release), and per-feature
[feature flags](feature-flag-blast-radius-isolation.md) can substitute for
a full release rollback when only one feature within a release is at
fault. Diagnosing *which* recent change is responsible for a symptom, and
the broader incident-response sequence, belong to `incident-management`;
this note is scoped to why release design should default to keeping
rollback cheap and available.

The same pairing applies in continuous integration: tests give confidence
to change; rollbacks give confidence to undo. Without tests, rollbacks
aren't safe; without rollbacks, broken tests can't be cleared quickly and
confidence in the suite erodes — see [build cop rollback
discipline](build-cop-rollback-discipline.md).

A sharper framing worth holding in mind: **rollback is never truly
risk-free either.** Reinstalling a "known good" prior release is itself an
untested production change in the system's *current* context — other
state (data, dependent services, traffic patterns) has moved on since that
release last ran, so the rollback is not actually reproducing a previously
verified condition, just a previously verified binary. That makes rollback
a real production action taken during an incident, exactly when risk
tolerance is at its lowest and confidence should matter most, not an
automatic escape hatch. In practice this argues for a **hybrid** policy:
prefer roll-forward when the fix is genuinely fast to ship (which requires
short pipeline lead time and confidence built up by
[continuous deployment](continuous-deployment-vs-continuous-delivery.md)),
fall back to rollback when forward-fixing would take too long, and treat a
narrowly-scoped [emergency breakglass](emergency-change-breakglass.md)
hotfix as a third, deliberately under-tested option for when neither
rollback nor a proper roll-forward is fast enough — with a mandatory
follow-up to eliminate whatever made the hotfix necessary.

A sharper version of "other state has moved on": rollback only reverts
*code*, not data already durably written by the version being replaced.
See [progressive rollout data-layer isolation](progressive-rollout-data-layer-isolation.md)
for a case where rollback made an outage worse, not better, because the
reintroduced old code could no longer read data the new code had already
written — and [rollback retriggers shared update side
effects](rollback-retriggers-shared-update-side-effects.md) for a related
case where the act of rolling back itself re-triggered the exact failure
it was meant to fix. When neither rollback nor roll-forward is safe or
fast enough, [falling back to a simpler safe
default](fallback-to-a-safe-default.md) is a third option distinct from
the breakglass hotfix above. For continuously-retrained ML models
specifically, see [retraining as roll-forward for
models](retraining-as-roll-forward-for-models.md).
