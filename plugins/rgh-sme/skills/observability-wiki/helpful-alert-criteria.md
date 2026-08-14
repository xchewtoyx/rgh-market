---
type: concept
title: What Makes an Alert Genuinely Helpful
description: A helpful alert must be both a reliable indicator of degraded user experience and actionable — a responder can systematically investigate and act on it without having to guess what to do — and anything failing either test should be deleted, not tuned.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 11"
---

A genuinely helpful alert satisfies two conditions:

1. It's a **reliable indicator of degraded user experience** — not a proxy that fires regardless of whether users are actually affected.
2. It's **actionable** — a responder can systematically investigate and act on it, without having to "divine" what to do from a bare threshold breach.

Anything that fails either test should be **deleted, not tuned** — a non-actionable or unreliable alert doesn't get better by adjusting its threshold, because the underlying problem is what it's measuring, not how sensitively it's measuring it. This is consistent with [actionable paging hygiene](actionable-paging-hygiene.md) and [symptom-based vs. cause-based alerting](symptom-based-vs-cause-based-alerting.md); it adds the explicit two-part test and the "delete, don't tune" corollary.

A related failure mode: **threshold/potential-cause alerting** (CPU > 80%, disk > 95%) fuses a presumed cause with an assumed symptom, and the correlation to actual user pain is frequently weak — this is well-suited only to [known-unknowns](known-unknowns-vs-unknown-unknowns.md), enumerable risks with an unambiguous fix, and structurally cannot catch [unknown-unknown](known-unknowns-vs-unknown-unknowns.md) failure modes, since you can't pre-write a threshold for a failure you can't yet imagine. Repeated exposure to alerts like this is one of the main paths to [alert fatigue and normalized deviance](alert-fatigue-and-normalized-deviance.md).
