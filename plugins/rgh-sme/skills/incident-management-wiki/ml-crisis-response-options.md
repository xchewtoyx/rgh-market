---
type: concept
title: ML Crisis Response Options
description: Five immediate mitigation choices for a continuous ML system in crisis — stop training, fall back, roll back, remove bad data, roll through — and how to pick among them under time pressure.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 10"
---

A continuous ML system inherits every production vulnerability of large,
complex software, plus ML-specific undefined or unreliable behavior that
theoretical guarantees don't cover. Crisis mitigation must happen in real
time rather than waiting for a full diagnosis, for three reasons: models are
often mission-critical minute to minute; a model can be in a feedback loop
with itself, so delay lets the corruption feed back into the input data the
model itself will train on next; and a model can sit inside a larger
ecosystem (other models, or lasting external harm — a chatbot that started
cursing at users) that's hard to reset to a known-good state just by fixing
the immediate cause.

Five immediate responses form the standard mitigation toolkit; not every
crisis needs all five, and which to reach for depends on severity and how
fast a diagnosis is possible:

- **Stop training**: the "First Rule of Holes" — when the incoming data
  stream itself is corrupted (bad model, outage, code bug), halt training
  and halt pushing new versions to serving. A short-term response to stop
  things getting worse, not a fix. Needs both an easy manual stop mechanism
  (a "Big Red Button") and automated alerting, so a silently-stopped model
  doesn't go undiscovered for weeks.
- **Fall back**: swap in an ultra-reliable, deliberately simpler
  non-continuously-trained replacement (a simpler model, a lookup table of
  common responses, or a function returning the median prediction) to keep
  the product usable while the rest of the response proceeds. Intentionally
  lower-performing and meant to be short-lived.
- **Roll back**: revert to a known-good state — production binaries if the
  root cause is bad code (staged, in case of new incompatibilities), or the
  model checkpoint if the root cause is bad data that corrupted the model's
  state. Example: a Black Friday purchase surge breaks fraud detection by
  making the model think all products are now unlikely to be purchased;
  rolling back to a pre-Black-Friday checkpoint serves reasonable
  predictions while the rest of the system gets fixed.
- **Remove bad data**: delete the corrupted data so retraining doesn't
  re-encounter and get re-corrupted by it. Useful when the bad data is
  unrepresentative, unlikely to add value, and its cause (an external event
  or a fixable bug) is temporary.
- **Roll through**: resume training after removing bad data and fixing
  bugs — but for genuine external-world events, the right response is
  sometimes to let the model train on the atypical data and recover
  naturally as the event passes, since the world rarely has zero unusual
  events happening somewhere and exposure to atypical data helps general
  robustness.

**Choosing among them**: compare current behavior to the model's historical
response to similar past events, which is easiest when the model was
trained on sequential temporal data. Separately, check whether the
crisis-indicating metrics reflect a genuinely broken model or a model
correctly handling a harder-than-usual world state, by recomputing offline
golden-set metrics frequently — a sharp golden-set performance drop signals
real corruption (in which case roll through is probably the wrong call);
stable golden-set performance despite alarming production metrics points
toward the world having changed rather than the model having broken.

This crisis response is far more effective when it's rehearsed, not
improvised — see [preparedness drills](preparedness-drills.md) for the
general practice of building that muscle memory before it's needed, and
[ML pre-negotiated outage thresholds](ml-pre-negotiated-outage-thresholds.md)
for agreeing in advance on the numeric triggers that decide which of these
five to reach for. Roll back specifically has a limit worth knowing before
reaching for it — see [ML rollback limits in a changing
world](ml-rollback-limits-in-a-changing-world.md).
