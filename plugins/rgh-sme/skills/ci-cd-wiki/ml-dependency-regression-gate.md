---
type: concept
title: ML Dependency Regression Gate
description: >
  An eval pipeline that automatically re-scores a downstream ML model against
  a fixed dataset whenever an upstream model it depends on publishes a new
  version, catching silent accuracy degradation from data drift that no code
  diff would ever surface.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

# ML Dependency Regression Gate

In a multi-model production system, one model's output is often another
model's input — e.g. an ASR (speech-to-text) model feeding several
downstream NLP models. This is [downstream pipeline
triggering](component-pipeline-triggering.md) applied to ML artifacts
instead of code components, but the failure mode is different: a new
upstream model version can silently degrade a downstream model's accuracy
even though no line of the downstream model's own code or training data
changed. The upstream model's *output distribution* shifted — new vocabulary
entering transcriptions, transcription accuracy itself improving and
shifting the input shape, or a topic surge changing what's being talked
about — and the downstream model was trained on the old distribution. There
is no commit to bisect and no code diff to review; the change is purely in
the data flowing between two models.

## The gate

Extend the "publish triggers downstream pipeline" pattern so that publishing
a new upstream model version auto-triggers an evaluation pipeline for every
downstream model that depends on it:

```
[New ASR model version published] -> [Trigger eval pipeline for each dependent NLP model]
                                                        |
                                                        v
                                        [Score NLP model against fixed eval dataset,
                                         using the NEW upstream model's output]
                                                        |
                                                        v
                                [Compare metric (e.g. F1) vs. established baseline]
                                                        |
                                      (flag / alert if degradation exceeds tolerance)
```

This is the accuracy-metric analogue of an [automated performance regression
gate](performance-regression-gate.md): both compare a build's output against
a historical baseline and treat unexplained drift as a failure signal, but
here the "build" under test is a *combination* of dependency versions rather
than a single commit.

## Why this needs its own eval infrastructure, not just CI

A production ML dependency graph is rarely one linear pipeline — it's
typically many-to-many (several upstream model variants, e.g. per-dialect or
per-product-line, each feeding several downstream task models), so the
pipeline has to handle a combinatorial set of version pairs, not one. Design
requirements this implies:

- **Assemble evaluation infrastructure per run rather than persisting it.**
  Each run selects the correct upstream and downstream model artifacts on
  the fly; the testbed itself is decoupled from any specific model version
  and only encodes dependency *ordering*. This keeps cost bounded as the
  model count grows and mirrors why [ephemeral test
  environments](ephemeral-test-environments.md) are provisioned fresh per
  run rather than kept warm.
- **Key every result by the full combination under test** — (upstream
  version, downstream version, dataset version) — not just by downstream
  version. Because the same downstream model can be evaluated against
  multiple upstream versions concurrently (and vice versa), a result is only
  interpretable once all three axes are recorded; collapsing any one of them
  makes it impossible to tell whether a metric change came from the upstream
  model, the downstream model, or the eval data itself. See [evaluation
  dataset versioning](evaluation-dataset-versioning.md) for the third axis.
- **Feed raw input, not the upstream model's cached output**, when the point
  is to detect whether the upstream model's *behavior* changed. Re-running
  the upstream model as part of the eval (audio in, not pre-transcribed
  text) is what actually exercises the dependency; scoring against a frozen
  transcript would test the downstream model in isolation and miss the
  interaction entirely.
- **Scale to run many combinations concurrently.** As the number of upstream
  variants times downstream models grows, evaluations must run in parallel
  rather than queue serially, or the gate becomes a bottleneck that teams
  route around.
- **Retain inference artifacts and logs** from every run (a fixed retention
  window, e.g. 30 days, is enough for most debugging) so a flagged
  regression can be traced back to specific inputs rather than just a
  degraded aggregate number.

## Secondary benefit: self-service prerelease evaluation

Because the same pipeline already knows how to evaluate any (upstream,
downstream, dataset) combination on demand, it doubles as a self-service
tool: before committing to release a new upstream model variant (e.g. a
new-dialect ASR model), an engineer can run an ad hoc evaluation against
each downstream model that would depend on it, surfacing incompatibilities
before they reach production rather than after.

## Limits

This pattern catches accuracy degradation the eval dataset is designed to
detect; it does not by itself explain root cause (a human still traces a
flagged metric drop back to a specific kind of data drift) and it can't
evaluate behavior only visible in live, transient production traffic that
resists offline replay. It is also only as good as its human-in-the-loop
review step until that step is itself automated into a direct alert — this
is a known limitation of the pattern in practice, not just a rollout detail.
