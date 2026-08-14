---
type: concept
title: Pre-Aggregation Is a One-Way Trip
description: Once telemetry is aggregated at write time, the underlying raw events are gone, and there's no way to retroactively recover an aggregate you didn't think to configure in advance — this is metrics' central structural limitation as a telemetry type.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 1"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
---

When telemetry is aggregated at write time — e.g. a per-instance average response time computed and stored as a single number — the individual events that went into it are discarded. If you later realize you needed a different aggregate (a weighted average across instances, a breakdown by a field you didn't tag at the time, the actual p99 rather than an average), there is no way to reconstruct it: the raw data is gone and only the pre-decided aggregate survives.

This is metrics' defining structural limitation as a telemetry type, and it's why the [wide-event model](three-pillars-vs-wide-events-model.md) treats preserving raw events as a core principle rather than an optimization: you don't know in advance what you'll need to ask later, so aggregation should happen at query time, not write time, wherever the cost model allows it. [Histogram metrics](metric-anatomy.md) (recording count + total rather than just a mean) partially mitigate this for the specific case of computing an accurate average later — but only if you thought to configure a histogram in advance, which is itself just a narrower instance of the same underlying problem: any pre-aggregation decision only pays off if it happens to be the one you need.
