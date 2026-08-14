---
type: concept
title: Cross-Team Blind Spots in Incident Diagnosis
description: A team can take an action whose consequences land entirely inside another team's system, so neither team can connect cause to effect without shared visibility that neither may know to seek.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 15"
---

In a documented ML incident, an app team's update caused every device to
reissue its most recent query once — reasonable, self-contained behavior
from the app team's own vantage point. The consequence, though, landed
entirely inside a different team's system: a continuous ML model
downstream interpreted the resulting click-less traffic spike as a
real-world drop in click-through rate and adjusted its predictions
accordingly. The model-ops team on call could see the effect (predictions
degrading, alerts tripping) but not the cause, because nothing connected
"app update behavior" to "training data corruption" in either team's
mental model — they were organizationally distant, with no shared context
linking the two systems.

This is a specific, common shape of diagnostic difficulty: it isn't that
either team lacked skill or attention, it's that the causal path crossed a
boundary neither team had visibility across. The app engineers who knew
queries got reissued on update had no reason to know that behavior fed an
ML training pipeline at all — that fact simply lived outside their system's
boundary. See [ML incident organizational
breadth](ml-incident-organizational-breadth.md) for why ML incidents in
particular tend to have unusually wide sets of implicated systems, and
[repeated intervention can extend
incidents](repeated-intervention-can-extend-incidents.md) for what happened
next once the diagnosis stayed incomplete: each side's independently
reasonable next action kept re-triggering the same corruption.

The generalizable implication for incident readiness is that closing this
kind of gap can't happen live, under pressure, for the first time — it
needs the two teams to already know of each other's existence and inputs
before an incident forces the connection, which is part of what makes
cross-team [preparedness drills](preparedness-drills.md) valuable beyond
just rehearsing procedure: they also build the working knowledge of which
other systems consume your team's outputs.

A second documented case shows the same shape from the opposite direction:
an upstream click-logging pipeline broke, and the team that owned it
noticed via their own alerting and mitigated for their own purposes (ad
billing) — but didn't realize their feed was also a hard data dependency
for a downstream ML training pipeline, so no one told the model team
anything was wrong until the model's behavior had already visibly degraded.
Here the blind spot wasn't "which system does my action affect," it was
"who else depends on data I already know is broken" — see [corrupted
validation can mask incidents](corrupted-validation-can-mask-incidents.md)
for how that gap let a bad model pass automated validation before anyone
noticed.
