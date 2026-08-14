---
type: concept
title: Data Lineage
description: >
  Recording an audit trail of a dataset's processing history and upstream
  dependencies, and what it's used for operationally.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Data lineage is the recorded audit trail of a piece of data through its whole
lifecycle: which systems processed it and in what order, and what it depended
on upstream. It serves several concrete pipeline needs at once: tracing an
error back to the transformation or source that introduced it, assigning
accountability when something's wrong, debugging unexpected output, and
meeting compliance obligations (e.g., knowing every place a specific user's
data landed, in order to honor a deletion request).

Lineage has historically been an enterprise/compliance-driven practice at
large companies, but tooling has made it accessible to smaller teams too.
Closely related is **Data Observability Driven Development (DODD)**: watching
data continuously across dev, test, and production to catch quality and
conformity problems as they happen, rather than after a report has already
been read by a stakeholder — the data-pipeline analogue of test-driven
development for application code.

**Dependency analysis** is lineage's forward-looking mirror image: instead of
starting from a data element and tracing where it came from, it starts from
a source or intermediate table and identifies every downstream table, report,
or derivation that depends on it. Where lineage answers "how did this value
get here," dependency analysis answers "what breaks if I change this
upstream" — the concrete tool for assessing blast radius before a proposed
source-system schema change ships.

Lineage capture is technical metadata (see also
[pipeline metadata categories](pipeline-metadata-categories.md)); it's most
useful when it's automatic and continuous rather than manually reconstructed
after an incident, because reconstruction is exactly the work an engineer has
no time for during an active data-quality incident.
