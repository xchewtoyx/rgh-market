---
type: concept
title: Training-Serving Skew
description: >
  Any drift between the environment a model was trained in and the
  environment it's served from — platform, feature-generation code, or
  plumbing — that causes correct offline behavior to fail or crash once the
  model is actually deployed.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 5"
---

# Training-Serving Skew

A model is trained in one stack (offline, batch, research tooling) and
served from another (online, low-latency, production infrastructure). When
those two stacks diverge — in ways nothing about the model's own weights or
architecture would reveal — the model can crash or misbehave in production
despite having been trained and validated correctly. This is the concrete
failure category the "can it serve a result without crashing" step of a
[model validity gate](model-validity-vs-quality-gate.md) exists to catch,
and it recurs in a handful of specific shapes:

- **Platform version incompatibility**: the serving stack runs a different
  version of a (often third-party or open-source) ML platform/framework than
  the training stack used, so an operation the model relies on behaves
  differently or doesn't exist at serving time.
- **Feature version incompatibility**: feature-generation code differs
  between the training and serving stacks, because the two evolve somewhat
  independently and have different memory, compute, and latency constraints.
  Concrete example: a word-token-to-integer dictionary used at training time
  that has gone stale relative to the one actually loaded in serving.
- **Corrupted model artifact**: write-time errors or NaN values get written
  into the saved model file because training-time sanity checks were
  insufficient to catch them before the artifact was persisted.
- **Missing plumbing**: a feature implemented and used in training was never
  wired into the serving pipeline, so any model that depends on it crashes
  the moment it's loaded into a serving environment that can't supply it.
- **Out-of-range results**: the model produces outputs outside its valid
  space at serving time — a probability model returning exactly `0.0` or a
  negative value, or a fixed 100-class classifier returning class `101` —
  which a downstream consumer expecting a bounded value has no reason to
  guard against.

None of these are caught by evaluating the model's predictive quality
against held-out training data, because the training data never passes
through the serving stack at all — they only appear once the model is
actually exercised end-to-end in a production-equivalent environment, which
is exactly what a validity check does deliberately and a quality evaluation
does not.
