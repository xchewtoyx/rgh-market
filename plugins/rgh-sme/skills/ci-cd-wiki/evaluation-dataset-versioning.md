---
type: concept
title: Evaluation Dataset Versioning
description: >
  Treating an ML eval/regression-test dataset as a versioned pipeline
  artifact, so that when the dataset changes out of band, past and present
  evaluation results stay comparable against a known dataset version instead
  of silently drifting.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

# Evaluation Dataset Versioning

An [ML dependency regression gate](ml-dependency-regression-gate.md) (or any
automated eval regression suite) only produces a trustworthy pass/fail if the
thing it scores against is stable enough to compare across runs. Eval
datasets are not static, though: they get extended with new labeled
examples, corrected for annotation errors, or rebalanced for new topics —
changes made by data science independently of any pipeline run. If the
pipeline treats the dataset as an unversioned, always-latest blob, a metric
change between two runs becomes ambiguous: did the model regress, or did the
eval set just change under it?

The fix is the same one applied to code dependencies: version the dataset
explicitly, and record which dataset version produced each result. A
baseline comparison is then always baseline-vs-current *on the same dataset
version*, or an explicit, deliberate re-baselining when the dataset version
changes — never an implicit comparison across two different datasets. This
is what makes a metric like "F1 dropped 25% over the year" attributable to
the model/dependency under test rather than dismissible as "the eval data
changed."

Practically, this means every recorded eval result is keyed by dataset
version alongside whatever model versions are under test (see [ML dependency
regression gate](ml-dependency-regression-gate.md) for the full key), and
producing labeled eval examples — slicing raw samples and annotating them
for the condition being tested — is itself pipeline-relevant work: it is
frequently the bottleneck constraining how fast new eval coverage can be
added, not the compute cost of running the evaluation itself.
