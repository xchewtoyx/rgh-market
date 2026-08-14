---
type: concept
title: Ambiguous Threats and the Standardized vs Experimental Mindset
description: >
  Weak, ambiguous danger signals are evaluated through an organisation's
  operating mindset — a standardized, compliance-driven culture dismisses
  them as known issues, where an experimental culture treats each as a
  hypothesis to test.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

The Columbia disaster (2003) is the defining case. Sixteen days before the
shuttle broke up on re-entry, mid-level NASA engineers saw the foam strike
on launch video and reported it immediately. Managers replied that foam
dislodgement was a known "maintenance problem" — it had never been
catastrophic before — and the signal died there: [normalisation of
deviance](normalization-of-deviance.md) operating in real time on a live
warning.

Roberto, Bohmer & Edmondson's analysis (HBR, 2006): organisations run on one
of two mindsets —

- **Standardized model**: routines and systems govern everything; strict
  timeline, budget, and process compliance; deviations are noise to be
  managed away.
- **Experimental model**: every day, exercise, and new data point is
  evaluated and debated, R&D-lab style; anomalies are data.

A mindset dismissing the signal is one way a weak threat dies unactioned.
A distinct, later way is structural: the signal is noticed and taken
seriously, but the organisation has no reliable channel for [translating
that perception into a formally recognised, escalatable safety
issue](signal-perception-vs-translation-gap.md).

"Firms get into trouble when they apply the wrong mind-set to … ambiguous
threats." NASA by the 1970s had built a culture of rigid standardization
(having sold the shuttle to Congress as cheap and reusable), so an ambiguous
threat was processed as a compliance question — is this in the known-issues
category? — rather than as a hypothesis to test. The authors' conclusion:
**vigilance alone will not prevent ambiguous threats from becoming costly
failures** — exhorting carefulness changes nothing if the mindset classifies
the signal as normal (which is also why try-harder countermeasures fail
generally: [old view vs new view](old-view-vs-new-view-of-human-error.md)).

Implications:

- Weak signals are exactly what pre-catastrophic [drift](drift-into-failure.md)
  emits; whether they are heard depends on culture and mindset, not on
  signal strength ([Westrum's information-flow
  thesis](westrum-typology.md)).
- When the ambiguous signal concerns a piece of hardware rather than a
  process, the same absorption happens through [unruly
  technology](unruly-technology.md)'s three conditions: the anomaly is
  common, a routine compensation exists, and a real fix would be
  disruptive.
- Watch the vocabulary an anomaly is discussed in over time: [risk
  relabelling](risk-relabeling-as-leading-indicator.md) toward a less
  alarming category is itself a signal, independent of whether the
  downstream consequence can be predicted.
- At the individual cognitive level, the same absorption is the [garden path
  fallacy](garden-path-fallacy-and-snap-back.md): each dismissal of a weak
  signal is locally reasonable, and only the running tally of dismissals is
  diagnostic.
- Treat safety-relevant work as fundamentally experimental: each anomaly is
  a data point about the system's real behaviour, to be investigated at the
  threshold set by [ever-lower incident
  tolerances](seeking-weaker-failure-signals.md).
- "It's never hurt us before" is not evidence of safety — it is the
  [incubation period speaking](chronic-unease.md).
- Westrum's own term for the weak end of this signal spectrum is **faint
  signals**: early hints subtle enough that they are almost never recognised
  as warnings until after a failure has already made their significance
  obvious in hindsight. Deliberately building faint signals into a [proactive
  monitoring architecture](proactive-monitoring-control-model.md), rather
  than waiting for them to accumulate into something unambiguous, is the
  structural countermeasure to this whole dynamic.
