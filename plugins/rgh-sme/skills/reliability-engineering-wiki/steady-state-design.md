---
type: concept
title: Steady-State Design
description: >
  Designing a service to run indefinitely without periodic manual reboots or
  cleanup, by actively bounding resource and state growth rather than masking
  leaks with restarts.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 3"
---

Steady state is the property of a service that can run perpetually without
requiring a periodic manual reboot or a scheduled cleanup script to reclaim
resources. Relying on restarts to clear accumulated memory, stale cache
entries, or leaked connections doesn't fix the underlying leak — it just
masks it on a schedule, and the system fails as soon as something (a delayed
restart, an unexpectedly long maintenance window, higher-than-normal load)
pushes it past the interval the restarts were covering.

Designing for steady state means treating resource and state accumulation as
something the running system must actively manage, not something an external
restart cycle cleans up:

- **Purge obsolete data** on an ongoing basis rather than letting it
  accumulate unbounded (stale sessions, orphaned temp files, unbounded log
  growth).
- **Bound state accumulation** — caches, in-memory collections, and queues
  should have explicit size or age limits, not grow without limit under
  sustained load.
- **Aggressively manage memory** so gradual leaks (unclosed handles,
  unreleased connections, retained references) are caught and prevented
  rather than accumulating until the process is forced to restart or crash.

Steady-state design is the primary defense against
[strain](system-stability.md) — sustained load that exposes latent resource
leaks — as distinct from the impulse (traffic spike) threats that
[load shedding](load-shedding.md) and
[circuit breakers](circuit-breaker-pattern.md) are built to absorb.
