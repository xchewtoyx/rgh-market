---
type: concept
title: Data Contract
description: >
  A written agreement between a source system's owner and the team ingesting
  from it, stating what data is extracted, how, how often, and who to
  contact.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

A data contract (definition from James Denmore's *Data Pipelines Pocket
Reference*) is a written agreement between the owner of a source system and
the team ingesting data from it for a pipeline. It states what data is being
extracted, via what method (full snapshot or incremental —
see [incremental vs. full extraction](incremental-vs-full-extraction.md)),
how often, and who the contacts are on both the source-system side and the
ingestion side.

Formalizing this closes exactly the gap that
[schema evolution in source systems](schema-evolution-in-source-systems.md)
and [source system evaluation](source-system-evaluation.md) both flag as
recurring risks: a pipeline finding out about a breaking upstream change only
when a job fails. A contract gives both sides an explicit, discoverable
reference for what's expected — ideally stored somewhere searchable (a
repo, an internal docs site) and, where practical, in a machine-queryable
format rather than only prose, so drift from the contract can eventually be
checked automatically rather than relying on someone reading it.

A lighter-weight companion is agreeing expectations as an SLA (what's
promised — e.g., "data will be reliably available and of high quality") with
an SLO to measure it (e.g., "99% uptime"). Even without a formal contract,
setting these expectations explicitly with the upstream owner — rather than
assuming them — is one of the highest-value, most commonly skipped steps in
building a reliable pipeline against a source you don't control.

**A contract should state explicitly what it does *not* promise, not only
what it does.** A pipeline that ingests and delivers events on behalf of
many independent producing teams can deliberately scope its own contract to
delivery integrity alone — on time, complete, unaltered — the way a postal
service guarantees delivery of a package without taking responsibility for
what's inside it, and leave content accuracy as each producing team's own
responsibility. Making that boundary explicit in the contract avoids a
predictable failure mode: a consumer assuming a delivery-focused pipeline
also guarantees content correctness, then treating a producer's
data-quality bug as if the pipeline itself had failed its contract.

**A contract also has to name who actually depends on it, not just what it
delivers.** In a real incident, an upstream team's own alerting correctly
caught their feed breaking, and they judged the impact against what they
knew they were responsible for (eventual billing accuracy) — but they had
no record that a downstream ML training pipeline treated their feed's
*completeness* as a hard correctness dependency, so nobody paused training
while the feed was down, and a training pipeline for several days silently
learned from data that looked complete but wasn't. Listing known downstream
consumers and what completeness or availability standard each one actually
needs — not just documenting the data's shape and schedule — is what turns
an upstream team's own outage detection into a signal the affected
consumers can act on, instead of information that stays inside the
producing team's own on-call channel.
