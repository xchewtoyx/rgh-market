---
type: concept
title: Alert Fatigue and Normalized Deviance
description: Alerts that fire without real user impact train responders to dismiss alerts generally, and this normalization of deviance eventually means the one alert that actually matters has to fight through learned distrust before anyone takes it seriously.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 11"
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 15"
---

Repeated non-actionable or unreliable alerts (see [what makes an alert genuinely helpful](helpful-alert-criteria.md)) don't just waste an individual responder's time — they change behavior at the team level. Responders learn, correctly, that a given alert usually doesn't mean anything is actually wrong, and start routinely dismissing it. The term borrowed for this pattern, from the Challenger disaster investigation, is **normalization of deviance**: a condition that should be alarming becomes accepted as routine simply because it's been observed and survived many times before.

The dangerous consequence is that this learned distrust doesn't stay scoped to the noisy alert — it erodes trust in alerting as a whole, so the one alert that represents a genuine, novel problem has to fight through the same skepticism earned by all the noisy ones before anyone takes it seriously. This is the deeper reason bad alerts should be deleted rather than merely tuned (see [what makes an alert genuinely helpful](helpful-alert-criteria.md)) and why [minimum-duration requirements](time-series-alert-rule-evaluation.md) and sensible [routing/silencing](alert-routing-and-notification-management.md) matter beyond just reducing pager volume — they protect the credibility of the alerting system itself.
