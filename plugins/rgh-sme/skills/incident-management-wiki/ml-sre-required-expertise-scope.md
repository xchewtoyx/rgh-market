---
type: concept
title: ML SRE Required Expertise Scope
description: What an ML production engineer actually needs to know to be effective on call — the flow and relationships between the systems that build a model — rather than modeling expertise itself, which most ML SREs at scale never need.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

Because many ML incidents present as model-quality problems, it's tempting
to assume ML production engineers need substantial modeling skill. That
holds in small organizations, where model developer, systems developer,
and production engineer are often the same one or two people — the same
way a small team's developer also owns their own service's reliability.
As organizations and services grow, though, that requirement mostly
disappears: most SREs doing production engineering on ML systems at scale
rarely or never train models themselves, and that isn't the expertise
their job actually needs.

What this role does need is basic familiarity with what ML models are and,
above all, the shape of the interconnected systems that build and serve
them — the relationships and data flow between components matter far more
than learning-algorithm internals. For a supervised-learning system using
scheduled training jobs reading from a feature store to produce a saved
model, the production engineer needs to know roughly how the training
framework works, how feature-store data updates, how training is
scheduled, what a saved model file looks like and how to validate it — but
not how many layers the model has or how its labels were originally
generated, unless regenerating them becomes part of the incident. The
inverse holds for modeling engineers who package and deploy their own
models: they need to understand how their configuration choices affect the
deployed container and basic health-check and log inspection at the
deployment location, but low-level platform internals implicated in a
failure should hand off to a specialist rather than becoming something
every modeler is expected to debug themselves.

The practical conclusion for staffing an ML on-call rotation: detailed ML
knowledge is a helpful addition to a production engineer's toolkit, but the
biggest reliability gap most organizations actually have is a shortage of
people who understand building and operating distributed systems in
general — that shortage, not a lack of ML-specific knowledge, is usually
the higher-leverage hiring or training investment. This scoping also
shapes what [software engineers](ml-software-engineer-incident-role.md) and
[model developers](ml-model-developer-incident-role.md) are each expected
to own during an incident, rather than leaving the boundary between the
two roles implicit.
