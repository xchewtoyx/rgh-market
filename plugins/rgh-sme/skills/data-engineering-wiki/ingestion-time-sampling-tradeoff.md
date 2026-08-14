---
type: concept
title: Ingestion-Time Sampling Tradeoff
description: >
  Dropping or sampling a fraction of incoming data at ingestion to control
  downstream processing cost, and why the sampling has to be rate-aware to
  avoid quietly losing burst detail.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 2"
---

Not all created data has to be ingested as-is. When downstream processing
cost scales with volume — a common constraint once storage or compute
becomes the binding cost, not just source availability — a pipeline can
filter out fields or records believed unnecessary, or sample down when raw
volume is too large to process affordably. Both are real cost levers, and
both carry a real quality cost that has to be weighed against the savings
rather than assumed to be free.

**Sample proportionally to volume, not with a fixed rate applied
uniformly across time.** A flat sampling rate applied evenly regardless of
traffic level quietly loses more detail during bursty, high-volume periods
than during quiet ones — exactly when the most unusual (and often most
interesting) events are likely to be happening. Sampling proportional to
the actual rate or volume in each time slice avoids that bias, at the cost
of a more involved sampling implementation than "keep 1 in N records."

This is a distinct decision from
[incremental vs. full extraction](incremental-vs-full-extraction.md), which
is about *which time range* to pull — sampling is about *what fraction of
records within that range* to keep, and the two compose independently in a
pipeline that needs both.
