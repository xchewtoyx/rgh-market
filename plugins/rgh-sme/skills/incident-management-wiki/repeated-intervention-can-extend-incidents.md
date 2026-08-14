---
type: concept
title: Repeated Intervention Can Extend Incidents
description: Each well-intentioned mitigation attempt during a self-correcting anomaly can independently re-trigger the same failure mechanism, extending the incident further than restraint would have.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 15"
---

In a documented case, a mobile app update caused every installed device to
reissue its most recent query simultaneously, producing a spike of
click-less traffic that corrupted a continuous ML model's training signal
(the model inferred the world's click-through rate had halved and adjusted
predictions downward). Diagnosing this took time because the app team and
the model team had no shared visibility into each other's systems — the app
engineers who knew queries got reissued on update had no idea that behavior
fed a continuous ML training pipeline, so the connection between "we pushed
an update" and "the model broke" wasn't obvious to either side.

What made the incident far longer than it needed to be wasn't the original
bug — it was the response. An unrelated bug caused the update to be rolled
back, which itself triggered every device to revert and reissue its query
again: a second wave of the same corrupting traffic. Once root cause was
traced to the app push, the team (still not understanding the specific
mechanism) assumed a new bug and rolled the app back a second time,
triggering a third round. Each of these interventions was reasonable given
what its author knew at the time, but each independently re-triggered the
identical corrupting mechanism and did as much harm as good — materially
extending the incident beyond what the original anomaly would have caused
on its own.

The retrospective lesson: letting the model simply roll through the very
first anomaly, without intervening at all, would likely have produced a
faster, smoother recovery than the entire chain of well-meant fixes. This
is the reflexive-action counterpart to [plan continuation
bias](plan-continuation-bias.md) — where that bias is sticking with an
existing plan too long, this is *switching to a new corrective action* too
readily, when the situation actually called for recognizing a
self-correcting anomaly and deliberately not acting. See [ML crisis
response options](ml-crisis-response-options.md) for "roll through" as one
of the standard responses this case study argues for reaching toward
sooner, and [cross-team blind spots in incident
diagnosis](cross-team-blind-spots-in-incident-diagnosis.md) for why the
mechanism went unrecognized for as long as it did.
