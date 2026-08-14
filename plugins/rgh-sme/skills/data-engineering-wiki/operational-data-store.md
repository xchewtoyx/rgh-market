---
type: concept
title: Operational Data Store (ODS)
description: >
  An integrated, near-real-time operational repository that sits between
  source systems and the warehouse, serving tactical queries the warehouse's
  load cadence is too slow for.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 6"
---

An operational data store integrates data from multiple source systems the
same way a [data warehouse](data-warehouse-architecture.md) does, but for a
different purpose and on a very different clock: it serves near-real-time
operational and tactical decisions (checking current stock for a specific
item across stores, say) rather than historical trend analysis. Where a
warehouse might load daily or weekly, an ODS integrates continuously or every
few minutes, and it deliberately keeps only a short rolling window of data —
current operational state, not an organization's entire history.

An ODS earns its place when source-system reporting is too limited on its
own, when a better query tool than the source system provides is needed, or
when only a few people have source-system access but more people need to
report against it — situations where standing up a full warehouse pipeline
would be both too slow to build and too infrequent to actually serve the
need. Data usually keeps a structure close to its source systems, though the
ODS's integration step can still clean, normalize, and apply business rules
at the point of merge — it's doing real transformation work, just at much
higher frequency and lower latency than a warehouse's [batch cadence](latency-tier-triage.md)
would allow.

**The ODS-as-staging pattern**: rather than treating the ODS and the
warehouse's staging layer as two separate, redundant extraction paths against
the same sources, an ODS can double as the
[staging layer](warehouse-layering-source-staging-presentation.md) feeding
the warehouse — data is reconciled and cleansed into the ODS in near-real
time to serve operational consumers directly, and the warehouse's own,
less time-pressured load cycle then pulls from the ODS instead of hitting
the original sources a second time. This cuts the number of independent
extraction paths against a source system in half and shrinks how much
staging-area machinery the warehouse pipeline needs to maintain on its own —
though any warehouse-required data the ODS doesn't happen to carry still
needs its own staging path, since the ODS's scope is set by operational
need, not by what the warehouse eventually requires.
