---
type: concept
title: Retraining as Roll-Forward for Models
description: >
  For a model, retraining plays the role a code roll-forward normally
  plays — producing a new, hopefully-fixed version instead of reverting to
  a prior one — but it carries two failure modes an ordinary roll-forward
  doesn't share, and needs the same validation discipline before it ships.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

# Retraining as Roll-Forward for Models

[Roll back vs. roll forward](rollback-vs-roll-forward.md) frames the two
options as reverting to a known-good version versus shipping a fix on top
of the bad one. For a model, retraining — building a new model and hoping
it fixes the problem — is the model-specific instance of roll-forward,
used when rolling back to an older model version has failed, isn't
available, or doesn't fit the incident's infrastructure — see [fallback
to a safe default](fallback-to-a-safe-default.md) for what to do when
neither rollback nor retraining is fast enough.

Retraining has two failure modes an ordinary code roll-forward doesn't:

- **Retraining over the same data reproduces the same behavior.** Unlike a
  code fix, which directly targets the defective logic, retraining without
  changing the input changes nothing — the model will converge to
  approximately the same weights and repeat the same problem. The
  workaround is "hacking" the training data deliberately: use a different
  corpus, replace or exclude bad data, change the date range trained over,
  or reweight examples — retraining is only a fix if *something* about the
  inputs changes along with it.
- **Retraining can be too slow to be a tactical incident fix.** A full
  training run can take far longer than an incident can tolerate, unlike
  a code roll-forward whose fix, once written, ships as fast as the normal
  pipeline allows. This is an argument for investing in periodic automatic
  retraining ahead of time, where affordable, rather than treating
  retraining as something to stand up reactively mid-incident.

Retraining also carries a risk ordinary roll-forward doesn't have to the
same degree: there is no guarantee the newly trained model is actually
better. A model trained over an unrepresentative window (e.g. a holiday
period with atypical behavior) can be worse than the one it's replacing.
Without meaningful validation automation, every retraining attempt spends
both compute and staff time on a fix that isn't yet known to work — which
is exactly the [canary](canary-release.md) and pre-rollout validation
discipline the rest of a model's release path already requires; a
retrained model earns no exemption from it just because it was produced
in response to an incident.
