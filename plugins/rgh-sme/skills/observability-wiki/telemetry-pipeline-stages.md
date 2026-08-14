---
type: concept
title: Telemetry Pipeline Stages
description: A telemetry pipeline exists because collecting everything and sending it everywhere no longer scales economically or organizationally, and decomposes into five stages — collect, normalize/secure, enrich, reduce, route — underpinned by data resilience and pipeline observability.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 16"
---

As telemetry volume grows, "collect everything, send everywhere" stops scaling both economically (ingest-priced vendors) and organizationally (nobody can reason about an undifferentiated firehose). A telemetry pipeline sits between instrumented services and final destinations, and decomposes into five stages:

- **Collect** — ingest from many sources through a vendor-neutral collection layer (e.g. the OpenTelemetry Collector, with 100+ receivers for OTLP, Prometheus, StatsD, JMX, host metrics, etc.), replacing proprietary per-vendor agents.
- **Normalize & secure** — parse and coerce unstructured logs into [structured events](structured-logging.md), normalize mixed formats into one common shape, redact PII, and enforce compliance centrally rather than per-service. Pipeline-side redaction is a backstop, not the first line of defense: instrumentation itself should default to *not* capturing sensitive payload data at all (Dapper, for example, records RPC method names but never payload contents), with an explicit, opt-in annotation mechanism for a developer to deliberately attach specific fields they've judged safe and useful — narrowing what can leak far more reliably than trying to scrub it back out downstream.
- **Enrich** — attach context that wasn't available at the point of emission: infrastructure metadata (pod/node/AZ), business context (customer ID, tier), or external lookups (IP geolocation, DNS).
- **Reduce** — the primary cost lever: filtering out low-value data, deduplication, aggregation/roll-ups, and [sampling](sampling-rate-selection-strategies.md) (head/tail/adaptive).
- **Route** — fan out to multiple destinations (SIEM, APM, analytics, cold storage) without re-instrumenting anything, turning "add/swap a destination tool" into a configuration change rather than a code change.

Two cross-cutting concerns underpin all five stages: **data resilience** (buffering/persistence at each stage, retry with exponential backoff plus backpressure to avoid a thundering herd, HA/failover for every component) and **pipeline control/observability** (real-time dashboards on the pipeline's own throughput/error/latency, centralized policy enforcement, runtime-adjustable configuration, and incident-response tooling like rehydrating historical data or rerouting around a faulty component) — the pipeline itself needs the same rigor applied to it that it's meant to apply to the services it observes. See [telemetry pipeline architecture](telemetry-pipeline-agent-gateway-architecture.md) for how these stages map onto physical deployment topology, and [batch export size and time triggers](batch-export-size-and-time-triggers.md) for how the collect stage's exporters decide when to actually flush accumulated records.
