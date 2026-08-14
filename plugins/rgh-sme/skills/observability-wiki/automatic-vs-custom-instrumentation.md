---
type: concept
title: Automatic vs. Custom Instrumentation
description: Automatic instrumentation gives broad, low-effort coverage of technical plumbing (HTTP, DB calls) but can't understand domain logic, while custom instrumentation captures what matters to the business and has to be added deliberately — a good strategy uses both, and prunes automatic instrumentation's tendency toward overwhelming detail.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 4"
---

Two complementary sources of instrumentation:

- **Automatic instrumentation** — library/framework-level hooks (HTTP handlers, DB clients) that instrument technical plumbing with no code changes. Broad coverage, low effort, but blind to domain/business logic and, left unpruned in production, can generate an overwhelming volume of low-value detail that adds cost without adding insight. When instrumentation lives at the shared-library level rather than in application code, retrofitting it onto an existing codebase can be as cheap as recompiling against a newer version of libraries the codebase already depends on — Google found this true of Dapper support for legacy services already built on its common threading/RPC libraries, with no source changes required at all.
- **Custom instrumentation** — deliberately added by the engineers who own the code, capturing what actually matters for their domain (e.g. "insufficient inventory," "wrong experiment group" — distinguishing temporary vs. permanent, actionable vs. not). This can't be auto-generated because it requires domain knowledge; see [the wide-event attribute checklist](wide-event-attribute-checklist.md) for a practical guide to what to add.

Instrumentation strategy should be owned by the engineers writing the code, not bolted on afterward by a separate team — backed by shared conventions/libraries so individual engineers don't need deep observability expertise to instrument correctly. A practical framework for building a custom-instrumentation strategy: identify critical user journeys; instrument domain-specific error conditions automatic instrumentation can't see; ask what questions are routinely needed during an investigation and instrument to answer those; capture *why*, not just *what* (business context, active flags, request source); and establish naming/attribute conventions so instrumentation stays consistent as the team grows — see [telemetry naming conventions](telemetry-naming-conventions.md).

A related discipline: over-collecting telemetry has real costs beyond storage/compute — cognitive overload triaging many fragmented signals, and delayed incident resolution from noise. Treat what you emit as a deliberate decision, not a "capture everything just in case" default; deciding how to process/sample telemetry is a downstream concern, not something to bake irreversibly into instrumentation code, since that would remove optionality later.
