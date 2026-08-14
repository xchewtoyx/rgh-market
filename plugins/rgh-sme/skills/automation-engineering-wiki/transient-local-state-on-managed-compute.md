---
type: concept
title: Transient Local State on Managed Compute
description: >
  Replicas treated as cattle lose all in-process and local-disk state on
  replacement or migration, so durable application state must live off-machine
  unless a local copy is explicitly disposable.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Transient Local State on Managed Compute

Whenever a [cattle](pets-vs-cattle.md) job is replaced, in-process state
vanishes. If the scheduler moves the job to another machine, anything on
local disk vanishes too. The operational rule follows directly: treat
local state as **transient** and push "real" storage to durable,
off-machine systems. If all local inputs are immutable, failure resistance
is comparatively painless.

Durable storage itself is usually built from cattle — state replication
across multiple replicas with consensus for writes, the same way RAID
treats individual disks as disposable — which is why organizations invest
in shared storage platforms rather than expecting every application team
to implement replication correctly.

Local storage still has legitimate uses when loss is acceptable or
bounded:

- **Caching** — transient data that trades a small loss risk for lower
  average latency. Provision the cache for latency goals, but provision
  the core application for total load so losing cache capacity causes
  degradation, not outage.
- **Warm-up pulls** — copying external data into local storage at startup
  to improve serving latency, knowing it may need repeating after
  reschedule.
- **Batched writes** — aggregating high-volume, low-criticality output
  (monitoring metrics feeding [autoscaling safety
  practices](autoscaling-safety-practices.md), batch intermediates that can
  be recomputed) where losing a fraction is tolerable.

The pattern generalizes: anything that must survive [progressive compute
automation](progressive-compute-automation.md) killing or moving replicas
cannot depend on locality without an explicit recovery story.
