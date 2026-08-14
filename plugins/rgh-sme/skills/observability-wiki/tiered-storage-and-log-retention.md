---
type: concept
title: Tiered Hot/Cold Storage
description: Observability datastores keep recent data on fast local storage and age older data out to cheap object storage, fetching it back on demand when a query needs it — the same hot/hot-to-cold spectrum retention policy uses to balance storage cost against how far back an investigation might need to reach.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 13"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
  - title: "Implementing Service Level Objectives"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 7"
---

Observability datastores commonly tier storage by age: recent data stays on fast local disk (SSD/NVMe) for low-latency querying, while older, closed [time-partitioned segments](time-partitioned-columnar-storage.md) are compacted and pushed out to cheap object storage (e.g. S3), then fetched back into memory on demand only when a query actually needs that range. `TTL`-style lifecycle rules automate this: move data to a colder tier after N days, delete it entirely after M days — and a conditional TTL can retain high-signal categories (e.g. errors) longer than routine data. Dropping whole time-partitioned blocks wholesale (rather than scanning and deleting row-by-row) is cheap specifically because data is physically clustered by time.

This is the same underlying trade-off as [graceful log degradation](graceful-log-degradation-and-retention-tiers.md) — balancing storage cost against how far back an investigation might need to reach — applied at the level of a datastore's internal storage engine rather than at the level of an organization's log-retention policy. Both converge on the same shape: cheap, coarse, long-retained data for the distant past; expensive, fully-indexed, fast data for the recent window investigations actually run against most often.

The raw-event **retention horizon** — how far back a store keeps un-aggregated events before they're dropped or only available in a coarsened tier, sometimes under a week in systems tuned for cost — is also a direct limit on backtesting: [evaluating a new threshold or grouping against history](event-granularity-vs-time-bucket-aggregation.md) is only possible as far back as raw events still exist. A store with excellent per-event flexibility but a short retention horizon may still be unable to answer "how would this new rule have performed over the last quarter" — that question needs raw data reaching back further than the horizon allows.
