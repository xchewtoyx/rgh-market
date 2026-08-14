---
type: concept
title: Training Data Consistency Requirement
description: >
  Whether a training pipeline needs a strict cross-replica consistency
  guarantee for its input data is driven by data sparsity, not by a blanket
  reliability rule, and can be resolved either by tolerating inconsistency or
  by paying for a consistency-guaranteeing storage layer.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 2"
---

At scale, ML training storage is normally distributed and replicated, so
different copies of the same data can transiently disagree. Whether that
disagreement actually matters to the model is a property of the data's
**sparsity**: dense data (each record represents something common) tolerates
an inconsistent read of any one copy without much model impact, since many
similar records exist to compensate; sparse data (each record represents
something rare) does not — an inconsistent read of a sparse record can
produce a model that's meaningfully wrong with respect to that record and
similar ones, because there's little redundant signal to average it out.
Waiting longer for data to arrive/sync is often enough to make consistency
easy to guarantee even where it would otherwise be hard.

Two ways to resolve this, each a genuine architectural choice rather than a
default:

1. **Build the model to tolerate inconsistent data** — lets training run
   faster and storage run cheaper, at the cost of flexibility: it locks the
   system into training only models that are satisfied with that property,
   for as long as the architecture stands.
2. **Operate the training system with a consistency guarantee** — most
   commonly, the replicated storage system exposes which data is fully and
   consistently replicated, and training reads only data flagged as such.
   Requires the storage layer to expose a replication-status API, and tends
   to be more complex, more expensive, and slower to make freshly-ingested
   data available for training.

Both are strategic, long-term cost/capability tradeoffs — not something to
decide implicitly by whatever the storage system happens to default to —
and belong alongside the rest of a service's data-reliability SLI choices,
next to [durability as SLI](durability-as-sli.md).
