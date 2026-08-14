---
type: concept
title: Corrupted Validation Can Mask Incidents
description: A validation, canary, or golden-set check that shares the same broken upstream dependency as the system it's meant to catch can certify a broken change as an improvement, because both are corrupted by the same failure at the same time.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 15"
---

In a documented case, an ad-click-prediction model trained on database rows
whose "was clicked" label was populated by a separate, upstream click-log
pipeline. That pipeline silently failed for several days; every ad shown
during the outage window was recorded as not-clicked regardless of ground
truth. A new model trained on this window learned, correctly given its
(corrupted) data, that clicks were far rarer than they actually were — and
the automated promotion gate, a held-out validation set built from the same
48-hour window using the same click feed, showed the new model as an
*improvement* over the old one, because the validation labels were exactly
as corrupted as the training labels. The validation system worked exactly
as designed and still certified a broken model, because "designed
correctly" implicitly assumed the labels it validated against were
trustworthy. Rerunning the identical validation later, after the click feed
caught up and the held-out rows got relabeled, flipped the result: the same
model pair now showed the new model as worse.

The general failure shape, not specific to ad click prediction: any
automated check meant to catch a regression — a validation set, a golden
set, a canary comparison — is only independent evidence if it doesn't share
the same broken dependency as the thing it's checking. When both the
system under test and its own validation gate read from the same upstream
pipeline, a failure in that pipeline corrupts both simultaneously and in
the same direction, so the check confirms the corrupted state instead of
catching it. This is a sharper version of why [ML pre-negotiated outage
thresholds](ml-pre-negotiated-outage-thresholds.md) should include an
explicit availability target for upstream data dependencies, not just for
the model-serving system itself — and why [cross-team blind spots in
incident diagnosis](cross-team-blind-spots-in-incident-diagnosis.md) matter
even when the diagnosis includes "we ran the validation and it passed": a
green check from a contaminated validation set is not the same evidence as
a green check from an independent one.

The concrete postmortem follow-ups this case produced are worth naming as
a template for the same failure mode elsewhere: add a coarse sanity check
on the validation data itself (here, flagging when the test set's
positive-label ratio is suspiciously low or high) so a corrupted validation
set is itself detectable; and establish a cross-team notification process
so an upstream data owner who already knows their pipeline is broken (as
the click-log team did, days before the model incident was declared) has an
explicit channel to tell downstream consumers to pause rather than train
through it.
