---
type: concept
title: Brier Score
description: >
  A proper scoring rule measuring distance between forecast probability and
  outcome — lower is better, like golf.
sources:
  - title: Superforecasting
    resource: "Superforecasting (Tetlock, Gardner), ch. 12"
---

The **Brier score** (Glenn W. Brier, 1950) measures forecast accuracy as the
distance between stated probability and actual outcome. Lower is better (like
golf): perfect = 0; random 50/50 guessing = 0.5; maximally wrong (100%
confident, wrong every time) = 2.0.

Raw Brier scores need **benchmarks**: compare against naive baselines (e.g. a
Phoenix forecaster who always says "hot and sunny" scores near 0 — skill means
beating that baseline, not the absolute number). A crude "no change from 2008"
rule would have scored 48/50 US states in 2012 — the real skill increment over
naive rules is often smaller than hype suggests.

Scores need **comparability** across questions of similar difficulty. Forecasting
Phoenix weather is easier than Springfield, Missouri — 0.2 means different
things in each context. Real-world forecasters rarely predict identical
questions over identical windows.

Rigorous measurement requires: precise terms, explicit timelines, numerical
probabilities, and *many* forecasts per forecaster — a single probabilistic
forecast cannot be judged; a track record can.

See [calibration versus resolution](calibration-vs-resolution.md) and
[Sherman Kent probability language](sherman-kent-probability-language.md).

**Asymmetric costs**: Brier scoring treats false alarms and misses equally, but
for terrorist attacks misses matter more. Fix: tell forecasters the asymmetric cost
in advance (e.g. false positives cost one-tenth of false negatives) so they
calibrate accordingly. Imperfect scores still beat judging forecasters by titles,
confidence, story-spinning, book sales, and media appearances — like credit scores
vs. whimsical loan officers (see [adversarial collaboration for forecasts](adversarial-collaboration-for-forecasts.md)).
