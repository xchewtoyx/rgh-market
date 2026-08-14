---
type: concept
title: Local Buffering With Remote Fidelity Control
description: On resource-constrained clients where "log everything" isn't affordable but you also can't predict what you'll need later, keep a full local circular log buffer on-device and let a server-side control channel dynamically tell the device what to actually transmit and under what conditions.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 19"
---

On mobile and other resource-constrained clients, "log everything, ship everything" is unaffordable (data/battery cost to the user) but under-logging means missing exactly the failure you needed context for, since release cycles are too slow to quickly add missing instrumentation after the fact. A pattern that resolves this tension:

- **Local storage**: keep all logs in a high-performance, disk-persisted circular buffer on the device by default. Logs don't leave the device unless explicitly requested. This solves cost (no ingest until something is actually needed), durability (survives unplanned process termination — telemetry delivery is least reliable exactly when the app is about to be killed, so **data loss skews toward the worst moments**, which can create a false sense of security if you're not aware of the bias), and performance (minimal main-thread/UI impact) simultaneously.
- **Real-time control plane**: a bidirectional streaming connection lets the server tell devices what to send and under what conditions — a "fidelity dial" the server can turn up or down per device or cohort, rather than the device unilaterally deciding to stream everything.

This enables workflows that would otherwise be impossible on a constrained client: deriving synthetic metrics/histograms from local logs and shipping only the compressed summary; or defining a server-side condition ("if a user leaves checkout without completing within 15 seconds, dump the full session") for targeted, on-demand deep debugging of specific cohorts or even single users, without needing to have decided to capture that detail for everyone in advance. It's a specific application of [aggregating at the source instead of streaming raw events](in-kernel-aggregation-over-event-streaming.md) to a client-side, bandwidth-constrained context, combined with a [sampling](sampling-rate-selection-strategies.md) decision that the server can adjust after the fact rather than only at instrumentation time.
