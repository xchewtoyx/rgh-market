---
type: concept
title: Graceful Log Degradation and Retention Tiers
description: When you can't afford to keep every log at full fidelity forever, degrade gracefully by retaining a full-fidelity copy briefly and a cheaper summarized/compressed copy for longer, rather than deleting everything once storage fills — and prioritize retention budget on the highest signal-to-noise sources.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

Log/telemetry storage cost grows with event volume, index size, and retention length, so retaining everything at full fidelity indefinitely is rarely affordable — but under-investing is dangerous too: if an investigation needs data older than your retention window, you simply can't do it (the average time to discover a compromise or a slow-building issue can be measured in months, far longer than a typical short retention window).

Rather than deleting data outright once storage fills, **design for graceful degradation**:

- **Data summarization**: write both a full-fidelity log and a lower-fidelity summary at collection time (avoiding an expensive re-read/re-parse later); once storage pressure hits, delete the larger full-fidelity file first and keep the smaller summary for the long term (e.g. full packet captures deleted after N days, but derived netflow-style summaries kept for a year).
- **Warm/cold tiering**: keep recent or incident-relevant data on fast local storage ("warm"), and move older data to cheap offline storage ("cold") — compressed raw logs can live a long time in cold storage even though only recent data sits in an expensive, fully-indexed store. See [tiered hot/cold storage](tiered-storage-and-log-retention.md) for how this pattern also appears inside observability datastores themselves, not just at the retention-policy level.
- **Prioritize by signal-to-noise**: not all logs are equally worth the storage budget — routinely-blocked traffic a firewall logs by the millions may be nearly worthless, while a small volume of high-signal error logs is worth keeping much longer. Compression is typically very effective on telemetry, since most log lines share a lot of repeated metadata.
- **Rotate intelligently**: default to deleting the oldest data first, but let specific high-value log types (e.g. security-relevant categories — see [log event selection](log-event-selection-and-severity.md)) be retained longer than the default policy.

This retention/cost trade-off is a core part of what makes an observability *data system* practical at scale, distinct from what to instrument in the first place.
