---
type: concept
title: Telemetry Naming Conventions
description: Span and metric names should be identifier-free, stable templates shared consistently across services, with type/unit information kept in attributes rather than encoded into the name string — standardized naming (semantic conventions) is what makes telemetry learnable and predictable across a whole organization rather than memorized per service.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 31"
---

Two related naming disciplines:

**Span/metric name formatting**: names should contain no identifiers or variable path segments — a route template like `/users/{user.id}`, never a materialized path like `/users/349827487124` (the latter creates unbounded [cardinality](cardinality.md) in the name itself). Use consistent dot-notation/snake_case, and put type/unit information into attributes rather than the name string — `http.server.request.duration` with a `unit` attribute, not `..._duration_ms` baked into the identifier.

**Semantic conventions**: standardized, portable attribute names (e.g. `http.request.method`, `db.system`) organized by namespace so the naming pattern is learnable and predictable across every service, rather than memorized independently per service. This is OpenTelemetry's most durable contribution for cross-team consistency — it prevents the situation where the same logical field ends up with a dozen conflicting keys across different teams' code, which is bad for humans and considerably worse for an AI agent trying to reason over inconsistent field names (a model has no reliable way to infer which of several conflicting keys is canonical).

Both disciplines can be enforced with **schema-driven telemetry**: define conventions in a schema file (e.g. via OpenTelemetry Weaver) and validate emitted telemetry against it at compile time or runtime, particularly valuable when migrating a codebase that has accumulated inconsistent ad hoc naming over time.

Practical tips for writing a telemetry schema: start from the "why" — the actual questions people ask of the data — rather than from what happens to be easy to emit; get the **namespace level right**, since shared cross-system identifiers (e.g. `acme.transaction.id`) belong above service-specific ones, or cross-service queries will silently drop or wrongly include records; abstract at the **actor/role level** (client/server, producer/consumer) rather than binding names to protocol-specific details, so the same convention survives a transport change; and keep attribute keys consistent across signal types, layering low-cardinality attributes onto [metrics](metric-anatomy.md) while reserving high-[cardinality](cardinality.md) ones for traces/events. When changing a pipeline's sampling or processing configuration, dual-sending telemetry to cheap blob storage alongside the main pipeline for a transition period means nothing is silently lost, which matters because "data I expected but can't find" is one of the fastest ways to break an organization's trust in its own telemetry.
