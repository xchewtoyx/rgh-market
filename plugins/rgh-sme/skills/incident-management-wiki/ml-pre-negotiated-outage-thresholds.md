---
type: concept
title: ML Pre-Negotiated Outage Thresholds
description: Agreeing in advance — not during a live incident — on numeric reliability thresholds, escalation triggers, and decision authority for a continuous ML system, so responders can act with minimum decision latency.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 10"
---

A continuous ML system has an unusual incident-readiness profile: an
older, rollback-ready model version is nearly always available (an
advantage most services don't have), but the whole system is constantly
evolving, which makes root-cause isolation harder — a model change may be
entangled with other concurrent changes such as new incoming data or
system integrations happening at the same time.

Given that, the most important preparation is agreeing on **roles,
authority, and escalation paths, plus concrete reliability standards** —
before a live incident forces the question, not during one. This is a
sharper, numeric version of the general principle behind [incident severity
classification](incident-severity-classification.md) and [escalation as a
resource request](escalation-as-resource-request.md): rather than only
defining severity tiers, pre-negotiate the actual trigger values. Example
standards: a model can be up to 12 hours stale without serious consequences
(though under an hour is generally preferred); crossing a quality-metric
threshold triggers an *automatic* rollback to an older model, with no human
decision in the loop; and crossing a worse threshold triggers waking
specific named business leaders.

Predetermining these parameters maximizes how fast a responder can act,
because the decision about *whether* a given number justifies action is
already made — only the diagnosis and the mechanical response (see [ML
crisis response options](ml-crisis-response-options.md)) remain to be done
live. Many organizations only formalize this after already experiencing a
few outages the hard way; treating it as prework rather than a lesson
learned after the fact is the point.
