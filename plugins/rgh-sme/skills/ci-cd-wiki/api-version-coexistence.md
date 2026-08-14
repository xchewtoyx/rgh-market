---
type: concept
title: API Version Coexistence and Deprecation
description: >
  Running multiple major API versions side by side (e.g. /v1 and /v2) rather
  than cutting consumers over abruptly, with explicit machine-readable
  deprecation notices signaling when an old version will actually be retired.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 14"
---

# API Version Coexistence and Deprecation

A breaking API change (per [semantic versioning](semantic-versioning.md), a
MAJOR version bump) can't rely on the
[tolerant reader pattern](tolerant-reader-pattern.md) alone, because by
definition it changes something a consumer already depends on. The mechanic
that keeps this from forcing a coordinated, simultaneous cutover across every
consumer: run the old and new versions side by side as distinct routes or
endpoints (`/api/v1/...` alongside `/api/v2/...`), so each consumer can
migrate to the new version on its own schedule rather than everyone needing
to move at once.

Retiring the old version still needs to actually happen eventually — parallel
versions aren't meant to run forever. Signal the retirement explicitly and
machine-readably, for example via `Sunset` and `Deprecation` HTTP response
headers carrying an actual retirement timestamp, so consuming systems (and
their own pipelines) can detect the deprecation programmatically rather than
relying on someone reading a changelog.

This is the API-consumer-facing counterpart to
[backward-compatible schema migration](backward-compatible-schema-migration.md)'s
expand-contract pattern: both exist to let a producer and its consumers
change versions independently instead of in lockstep, one at the database
layer and one at the API layer.
