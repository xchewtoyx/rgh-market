---
type: concept
title: Training Label Correctness as SLI
description: >
  A supervised model's training label is a recorded proxy for ground truth,
  not ground truth itself, so the pipeline that produces labels needs its
  own correctness/completeness SLI rather than being trusted implicitly.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

A supervised model never learns "the true outcome" directly — it learns
whatever a label-producing pipeline recorded as the outcome, which is a
[proxy for reality](user-centric-sli-selection.md) exactly like any other
SLI, and can silently diverge from it the same way any proxy can.

**Case study**: an ad-click-prediction pipeline recorded a click-boolean
column, defaulted `false`, later flipped `true` by a downstream click-logging
system once a click was verified. When the click-logging system's own
pipeline broke for several days, every ad shown during the outage kept its
default `false` label regardless of whether it was actually clicked. Nothing
about the training data looked malformed — it was well-formed, complete-
looking, and internally consistent — the model correctly learned "probability
this ad gets marked clicked in the database," which had quietly stopped
meaning "probability this ad gets clicked." The held-out validation set used
to gate the new model's promotion suffered the identical, correlated
corruption (it was drawn from the same window of poisoned labels), so it
could not catch the problem either — a systematic failure that corrupts
training and validation data the same way defeats generalization-style
validation checks, which are built to catch overfitting, not a shared,
correlated ground-truth error.

**Practical SLI response**: don't assume label correctness — monitor it.
A concrete, cheap technique from this case's postmortem: track the
aggregate positive-label ratio of the (held-out or live) data stream and
alert when it moves outside its normal historical range — a
suspiciously low or high click-through rate is a coarse but effective signal
that the label pipeline itself, not just the model, may be broken. This is
the [pipeline correctness/completeness](pipeline-sli-types.md) discipline
applied specifically to the label-producing stage of a training pipeline,
and it depends on first recognizing the label-producing system as a
[hard dependency](hard-vs-soft-dependency.md) of the training pipeline, since
the fix implied by monitoring for this (pausing training or holding the
model back) only works if there's a real hard-dependency relationship the
label pipeline's operators know they're expected to protect.
