---
type: concept
title: Rollback Retriggers Shared Update Side Effects
description: >
  A rollback or reapply is not a neutral undo when the update mechanism
  itself fires a stateful side effect on every transition — reversing it
  can retrigger the exact fault the rollback was meant to fix, and
  repeated toggling can retrigger it repeatedly, compounding harm instead
  of curing it.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

# Rollback Retriggers Shared Update Side Effects

[Roll back vs. roll forward](rollback-vs-roll-forward.md) usually treats
rollback as a clean, low-risk undo. That assumption fails when the update
mechanism itself has a side effect that fires identically regardless of
*which direction* the transition goes — the client or system reacts to
"an update just happened," not specifically to "the new version arrived."
In that case a rollback doesn't undo the side effect, it re-executes it a
second time.

**Illustration.** A mobile app was changed so that, on receiving an
update, it would reissue its most recent search query once, to guarantee
freshly served results. Every device that received the push fired a
duplicate, click-less query simultaneously — a traffic spike with no
corresponding user intent — which got staged as training data for a
continuously retraining click-through-rate model. An unrelated bug forced
the update to be rolled back, which itself triggered every device to
revert — reissuing the same query and producing a *second* wave of
corrupted training data. The model, trained on doubly-diluted
click-through data, inferred the world's click-through rate had halved
and adjusted predictions downward, tripping alerts. Diagnosis was slow
because the team that owned the update mechanism and the team that owned
the downstream model had no shared visibility into each other's systems.
Each further attempted fix — re-pushing the (now-fixed) update, then
reflexively rolling it back again when the symptom reappeared — retriggered
the same corrupting side effect a third and fourth time, extending the
incident well past what a single hands-off wait would have taken.
Stopping all further app updates and letting the model roll forward
naturally on clean data resolved it.

**The generalization**: before assuming rollback is a clean fix, check
whether the update mechanism has any effect that fires *on transition
itself* — a client-side hook, a cache invalidation, a re-subscription — as
opposed to an effect that only depends on which version is currently
running. A mechanism like that makes every toggle, in either direction, a
fresh occurrence of the side effect, not an undo of it. And where the
system downstream of that side effect is expected to be self-correcting —
a continuously retraining model that converges back to clean data once
new, uncorrupted input arrives — the lowest-harm response can be to hold
and let it recover, since each additional intervention is another chance
to retrigger the same side effect. This is a narrower, mechanism-specific
case than the general point in [roll back vs. roll
forward](rollback-vs-roll-forward.md) that rollback is never fully
risk-free; here the risk isn't drift in unrelated system state, it's the
rollback action itself sharing a trigger with the original fault.
