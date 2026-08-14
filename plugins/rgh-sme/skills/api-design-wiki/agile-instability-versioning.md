---
type: concept
title: Agile Instability Versioning
description: >
  A sliding-window lifecycle with one Preview and one Current version, rapid
  promotion, and timed deprecation that trades long-term stability for fresh features.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 24.3.2"
---

**Agile instability** caps simultaneous active versions via a lifecycle:

| State | Stability | Change policy |
| --- | --- | --- |
| Preview | Unstable | All changes allowed |
| Current | Stable for fixed window | Mandatory fixes only |
| Deprecated | Removal scheduled | Mandatory fixes only |
| Deleted | Gone | N/A |

Flow: v1 starts Preview (no guarantees); graduates to Current when mature. New work
opens as v2 Preview. When v2 becomes Current, v1 enters Deprecated with a removal
clock, then Deleted. At most one Preview and one Current at a time — forces continual
progress and bounds maintenance.

Trade-off: code against Current will eventually stop working — no multi-year pin
without migration. Suits engaged consumers who prioritize new capability over frozen
contracts; poor fit for "write once, ignore for years" clients.

Contrast [perpetual stability versioning](perpetual-stability-versioning.md) (long-
lived majors with in-place compatible drift) and [semantic versioning for APIs](semantic-versioning-api.md)
(granular major.minor.patch with many coexisting pins).

Govern with [limited lifetime guarantee](limited-lifetime-guarantee.md) or
[two in production](two-in-production.md) when Preview/Current alone is too aggressive.
