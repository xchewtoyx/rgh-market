---
type: concept
title: Dual Data Copy Divergence Risk
description: Maintaining two authoritative-seeming copies of the same data, synced by periodic merge, is a latent failure pattern where an upstream schema change can silently zero out the merge for weeks before anyone notices.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

In a documented case, a marketplace ML system kept a per-partner data
extract synced to a main store via a daily incremental merge — two
authoritative-ish copies of the same underlying data. Two weeks before
anyone noticed a problem, an unrelated analytics change to the unique
partner key used in log entries meant every newly extracted record no
longer matched the identifiers already in the main store, so the merge
step began succeeding (no error) while finding zero mergeable records for
any partner, every day. Every partner's model kept training on
increasingly stale data, and every partner's recommended-product values
declined day over day for two weeks before internal detection happened —
and even then, only because one engineer happened to notice zero recent
conversions while producing an unrelated report, not through any
monitoring.

This is a common latent-failure shape wherever a system maintains two
copies of "the same" data connected by a periodic sync or merge step: the
merge can silently degrade to doing nothing at all while still exiting
successfully, because "zero records merged" and "correctly found nothing
new to merge" look identical to a health check that only watches whether
the job completed. The gap only becomes visible in the emergent metric
several hops downstream (the model's predictions) rather than at the sync
step itself. The general fix that generalizes across this failure shape is
crude but effective: an explicit lower-bound sanity check on the merge's
own output (a "records merged must be greater than zero" alert) catches
the catastrophic case cheaply, even where a more refined statistical check
(comparing merged-volume against a trailing average) is too noisy to tune
reliably in a naturally fluctuating environment.

The upstream change that triggered this — a schema or key change made far
from where the failure eventually manifested — is exactly the kind of
change [dependency owners rarely know to check
for](cross-team-blind-spots-in-incident-diagnosis.md) before making it;
requiring any schema change to notify downstream consumers, rather than
relying on them to notice a silently degrading merge, addresses the same
gap from the other direction.
