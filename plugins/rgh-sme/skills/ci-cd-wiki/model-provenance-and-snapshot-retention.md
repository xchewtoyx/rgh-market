---
type: concept
title: Model Provenance and Snapshot Retention
description: >
  Retaining every trained model as a versioned snapshot alongside metadata
  about the data, features, hyperparameters, and authorship that produced
  it, so a production model can be recovered, reused, or traced back to its
  origin after the fact.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 7"
---

# Model Provenance and Snapshot Retention

Training a model produces two things worth keeping beyond the currently
serving version: the model artifact itself, and the metadata describing how
it came to exist. Retaining both, for every version and not just the
current one, is what makes [model rollback](rollback-and-roll-forward.md)
possible in the first place — you can't revert to a previous model version
that was never kept.

## What to retain per model version

- **The model snapshot itself** — the trained artifact, versioned, not
  overwritten by the next training run.
- **Model configuration and hyperparameters** — kept in a versioned system
  separate from the training system's own configuration, so a specific
  model's settings can be inspected or reproduced independently of whatever
  the training pipeline's current defaults are.
- **Data and feature provenance** — which data version and which feature
  definitions (see [evaluation dataset
  versioning](evaluation-dataset-versioning.md) for the parallel discipline
  applied to eval data specifically) went into this version, and who built
  it.

## Why it matters beyond rollback

- **Disaster recovery**: if a production model is accidentally deleted or
  corrupted, a retained snapshot is the only way to restore it without
  re-running training from scratch — which may not even reproduce the same
  result if the underlying data has since changed.
- **Bootstrapping new variants**: a retained snapshot is a starting point for
  transfer learning on a new variant, rather than every new model starting
  training from nothing.
- **Incident traceability**: when a production issue traces back to a
  specific model version, the retained metadata is what lets an engineer
  follow that thread backward — through the model, to the feature
  definitions it used, to the data version it trained on — to find the
  actual root cause. Without this metadata, that trace is frequently
  impossible: the model file alone doesn't say what produced it, and
  "whatever configs happened to be in the developer's working directory at
  the time" is not a substitute for a versioned, queryable record.

## Where this differs from generic build artifact retention

An [artifact repository](artifact-repository.md) retaining versioned code
builds solves an analogous problem for code, but a model snapshot needs
richer metadata than a code artifact does: a code build's provenance is
adequately captured by its source commit, while a model's behavior depends
on data and features that live outside version control entirely, so the
snapshot's metadata has to capture that data/feature lineage explicitly
rather than relying on an implicit link to a commit hash.
