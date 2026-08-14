---
type: concept
title: Parallel API Version Coexistence
description: >
  Run multiple major API versions side by side and announce retirement
  dates explicitly, instead of cutting consumers over to a breaking change
  all at once.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 14"
---

# Parallel API Version Coexistence

When a change is genuinely breaking under [semantic versioning](semantic-versioning.md)
(a MAJOR bump), the safe rollout path is to run the old and new versions
side by side — `/api/v1/...` and `/api/v2/...` concurrently — rather than
cutting all consumers over at once. This is the backwards-compatibility
window: the period during which both versions must be kept correct and
maintained, giving every consumer time to migrate on their own schedule
instead of on the producer's deploy schedule.

Retirement should be explicit and machine-readable, not just documented:
embed `Sunset` and `Deprecation` HTTP headers in responses from the
old version, carrying a concrete retirement timestamp, so consumers (and
their tooling) can detect and react to an approaching cutoff automatically
instead of being surprised by it.

This is the API-contract equivalent of [expand-and-contract schema migration](expand-and-contract-schema-migration.md):
both defer removing the old thing until every dependent has verifiably
moved to the new thing.

Not every evolution needs a full parallel major version, though. If the
change is additive and the old shape can be produced unchanged (e.g. a new
optional field), leave the original interface untouched and add the new
capability alongside it, so unmigrated consumers using
[the tolerant reader pattern](tolerant-reader-pattern.md) never notice.
When the new capability genuinely can't be expressed as a pure addition
(e.g. a field that used to be one string is now sent as separate
structured fields), keep a single internal representation and put a thin
translating layer at the boundary that maps it to whichever external shape
a given caller still expects — this avoids running and maintaining two
full parallel implementations for what is really one underlying change.
