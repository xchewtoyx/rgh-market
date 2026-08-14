---
type: concept
title: Model Validity vs. Quality Gate
description: >
  Splitting "will this model break the serving system?" (validity) from "is
  this model any good?" (quality) as two distinct pipeline gates, since a
  model can fail either one independently of the other.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 5"
---

# Model Validity vs. Quality Gate

Before a new or retrained model replaces the one running in production, two
independent questions need answering, and conflating them leaves a gap:

- **Validity**: will this model cause a system-level failure or crash if
  deployed? A model can be validity-safe and still be terrible — a model
  that mislabels every input identically causes no crash, just bad
  predictions. This question is answered by the checks below.
- **Quality**: is this model actually good — does it improve the business
  metric it's meant to improve, and is it better than the model it would
  replace? This is a separate evaluation, covered by [pre-rollout model
  comparison testing](pre-rollout-model-comparison-testing.md) and an [ML
  dependency regression gate](ml-dependency-regression-gate.md) when the
  question is whether an *upstream* dependency change degraded this model.

The reverse failure is just as real: a model can have excellent offline
predictive performance and still be invalid — it depends on a feature
version unavailable in production, an incompatible package version, or
rarely emits a value (e.g. NaN) that crashes a downstream consumer. Quality
evaluation run against training/offline data has no way to catch this, since
the failure only exists in the gap between the training environment and the
production serving environment. A pipeline needs both gates; passing one
says nothing about the other.

Both gates need to be automated, systemic parts of the training pipeline
itself rather than something each model developer assembles ad hoc. A
quality-evaluation step is easy to treat as optional scaffolding around the
"real" work of building the model, but skipping it just pushes the cost onto
every individual developer, who then builds a less consistent, less
reliable version of the same check themselves — at higher organizational
cost than building it once, centrally, as a mandatory automatic gate that
stores results comparably against previous model versions.

## The validity check sequence

Each check below answers a narrower question than the last, in the order a
pipeline should run them — cheap and structural first, expensive and
traffic-dependent last:

1. **Is it the right model?** Verify the artifact intended to serve is the
   artifact actually loaded — e.g. via a version/timestamp embedded in the
   model file itself and checked at load time, rather than trusting that the
   right file landed in the right place. This is the model-artifact instance
   of the same guarantee [artifact integrity
   verification](artifact-integrity-verification.md) provides for code
   builds: what gets deployed should be verifiably what was intended,
   automated rather than assumed.
2. **Will it load in a production-equivalent environment?** Attempt the load
   against a copy of the actual serving environment, not just locally — file
   formats drift across framework versions, and a model's on-disk size only
   loosely predicts its in-memory footprint, so a model that's too large to
   fit in a memory-constrained serving target (especially on-device) may
   only surface this by actually attempting the load there.
3. **Can it serve a single result without crashing the infrastructure?** Send
   one minimal request before any volume — this is the model-serving
   instance of a [smoke test](smoke-test.md): a narrow, fast check that the
   deployment itself works, run before trusting any deeper test. See
   [training-serving skew](training-serving-skew.md) for the specific
   failure modes this step is designed to catch.
4. **Is its computational performance within allowable bounds?** Measure
   latency (and, for batch serving, compute cost) as close to the real
   production environment as possible — dev environments often lack
   bottlenecks (network, storage, contention) that only show up on real
   production hardware. This is the same [nonfunctional test
   gate](nonfunctional-test-gate.md) discipline applied to a model's
   inference cost specifically, and the same production-hardware caveat
   [capacity test environment fidelity](capacity-test-environment-fidelity.md)
   makes generally.
5. **Does it survive a gradual canary ramp?** Even after every prior check
   passes, don't move straight to full production load — start with a small
   traffic trickle and increase only after confirming expected behavior.
   This is where validity checking hands off to [canary
   release](canary-release.md): the final validity check is a controlled,
   monitored production ramp-up, not a fixed pre-deployment test suite.
