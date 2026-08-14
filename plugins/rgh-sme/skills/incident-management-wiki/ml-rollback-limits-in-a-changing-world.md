---
type: concept
title: ML Rollback Limits in a Changing World
description: Rolling back to an older model or software version doesn't fully mitigate ML outages the way it does for conventional services, because the model's job is tracking a world that keeps moving even while the outage is being fixed.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

For a conventional service, rolling back to a prior release restores a
known-good state — the old binary behaves exactly as it did before,
because nothing about what it needs to do has changed in the meantime.
[ML crisis response options](ml-crisis-response-options.md) treats roll
back the same way for ML: revert to a known-good checkpoint or binary.
That works when the corruption is in the model or the code, but it has a
real limit specific to ML — the model's job is to track a world that keeps
changing regardless of whether an outage is in progress, so an old
checkpoint isn't a snapshot of "the world as it should be," only a
snapshot of the world as it *was* at that checkpoint's training time. If
customer preferences, supply, or behavior have genuinely shifted since
then, rolling back trades one kind of wrongness (broken) for another kind
(outdated), and retraining a materially better replacement may exceed
available compute capacity on any timeline that helps.

In a documented case, a team facing this exact tradeoff tested an older
model against current queries before deciding: the old model produced
somewhat more output than the broken current one, but still far less than
it had produced against queries from when it was current — evidence that
the world had moved enough that the old model wasn't simply "correct
again." The team judged rolling back too risky to revenue and left the
broken-but-current system running rather than reaching for the reflexive
mitigation. This is why choosing the best ML mitigation is described as
requiring business or product judgment more often than pure engineering
judgment does for non-ML incidents — see [ML incident organizational
breadth](ml-incident-organizational-breadth.md) — and why confirming
resolution is harder too: aggregate metrics compared against a
pre-outage baseline are an imperfect check when the correct target itself
kept moving throughout the incident. See [recovery point objective in
continuously adapting systems](recovery-point-objective-in-continuously-adapting-systems.md)
for the standard disaster-recovery term for this same limitation.
