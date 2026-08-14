---
type: concept
title: Progressive Rollout Data-Layer Isolation
description: >
  A progressive rollout isolates risk by code and serving version, but any
  component that changes what it writes to shared storage or logs
  silently couples old and new versions at the data layer too — and a
  rollback can amplify a failure instead of fixing it if the reintroduced
  old code can't read data the newer code already wrote.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 1, ch. 9"
---

# Progressive Rollout Data-Layer Isolation

[Progressive rollout](staged-percentage-rollout.md) — ramping a change
gradually across users and server capacity — isolates risk at the
code/serving layer: at any moment, only a fraction of the fleet runs the
new version. That isolation silently breaks if the new version also
changes what it *writes* to a store, queue, or log that the rest of the
fleet reads — an intermediate storage artifact rather than the code path
itself. If a newer component writes output in a changed format and an
older, not-yet-updated component reads it, isolating the rollout at the
serving layer alone does nothing to stop the two versions from
interfering through the data they share. See [backward and forward
compatibility during rollout](backward-and-forward-compatibility-during-rollout.md)
for the general compatibility requirement this creates.

**Illustration.** During a rollout of a stateful system, error rates rose
in proportion to rollout progress. The team treated rollback as the "easy
fix." Instead, errors spiked to 100%. Root cause: the new version had
already started writing data in a new format, in anticipation of an
upcoming feature. Reintroducing the old binary via rollback removed the
only code that could still read the new-format data already on disk — the
rollback didn't restore a known-good state, it created a new,
fleet-wide failure worse than the partial one it was meant to fix. Had the
rollout been allowed to complete (or been done all at once instead of
gradually), the errors would have resolved.

**The generalization**: a rollback only reverts *code*; it does not
revert data already durably written by the version it's replacing.
Treating rollback as a clean undo is safe only if the code being
reintroduced can still read everything written since it was retired — in
other words, rollback specifically depends on *forward compatibility*
(old code reading new-format data), not merely on redeploying an old
artifact. See [roll back vs. roll forward](rollback-vs-roll-forward.md)
for the broader case that rollback is never fully risk-free.

**Mitigation**, mirroring [expand-and-contract schema
migration](expand-and-contract-schema-migration.md)'s phased approach:
roll out *read* support for a new data format on its own, and let that
rollout complete fleet-wide, before any component begins *writing* in the
new format. Once every reader already tolerates the new shape, the
write-side rollout — and any later rollback of it — is safe regardless of
where the rollout currently stands, because no live component can ever
encounter data it doesn't understand.

The same hazard recurs whenever two coupled artifacts version
independently — for example a served model and the feature store it
reads. Feature transformations can differ subtly between model versions
(e.g. one version defaulting a missing input to "last seen location," a
later version defaulting it to "closest previously saved location") even
without any schema change at all, which is enough on its own to make
rolling back one side of a coupled pair while leaving the other on the
newer version actively unsafe, not merely inconsistent — the sharper
reason [release atomicity and tuple testing](release-atomicity-tuple-testing.md)
treats a coupled pair as one atomic rollback unit rather than two
independently revertible ones.
