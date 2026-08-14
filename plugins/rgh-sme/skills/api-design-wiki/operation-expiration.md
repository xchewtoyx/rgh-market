---
type: concept
title: Operation Expiration
description: >
  A uniform rolling retention policy for completed operations, keyed off
  completion time rather than creation, with an expireTime field on the resource.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

Operations differ from normal resources: created implicitly, critically
important until `done`, then often worthless. Retention options:

- **Keep forever** — simplest; fine unless volume reaches millions per day.
- **Rolling window after completion** — recommended default: set `expireTime`
  from the **completion** timestamp (not creation), for example purge 30 days
  after done.
- Tiered archival schemes — discouraged; unpredictable purge behavior for
  little gain.

Apply the **same expiration policy** across operation and result types.
Different windows per result type make outcomes disappear unpredictably.

See [operation resource shape](operation-resource-shape.md).
