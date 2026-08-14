---
type: concept
title: Rolling Deployment
description: >
  Sequentially updating application instances across a fleet, one (or a small
  batch) at a time behind a load balancer, so the service stays available
  throughout without requiring a second full environment.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 9"
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 4"
---

# Rolling Deployment

Instances behind a load balancer are updated one at a time (or in small
batches): a node is taken out of rotation, updated to the new version, checked
healthy, and returned to rotation before the next node is touched. Unlike
[blue-green deployment](blue-green-deployment.md), this requires no second
full-capacity environment — it reuses the existing fleet — but during the
rollout, old and new versions serve traffic simultaneously, so message and
record formats need compatibility in both directions at once: **backward
compatibility** (new code can read data written by old code) and **forward
compatibility** (old code, still running on nodes not yet updated, can read
data written by the new code) — see
[backward-compatible schema migration](backward-compatible-schema-migration.md)
for the database-specific version of this requirement.

Rollback follows the same mechanism in reverse: roll the previous version back
out across the fleet the same way it was rolled in.

## Tuning batch size and failure tolerance

Two parameters control how much of the fleet a bad rollout can reach before
it's stopped: how many hosts are updated concurrently in each batch, and what
fraction of a batch's hosts are allowed to fail before the entire rollout
aborts. A batch size of one gives the smallest possible blast radius per step
but takes longest to complete; a larger batch finishes faster but exposes
more of the fleet to a bad release before the rollout has a chance to detect
it and stop. Running the deployed application's own test or smoke check as
part of every batch (not just at the very end) is what makes an abort-on-
failure policy actually catch a bad release before it reaches every host,
rather than after. Tune both settings against available infrastructure
headroom: more spare capacity affords smaller batches (safer, slower); tight
capacity pushes toward larger batches, which trades safety for speed unless
additional capacity is provisioned instead.

## Draining and rejoining behind a load balancer

The concrete sequence behind "take a node out of rotation, update it, check
healthy, return it to rotation": before deploying to a given host, mark it
disabled at the load balancer so it stops receiving new traffic (existing
in-flight requests can drain); perform the deployment; wait for the service
to report healthy again; re-enable the host at the load balancer. If a
deployment step fails partway through, the affected host simply stays
disabled while the rest of the fleet continues serving all traffic normally
— the load balancer's disable/enable state is what turns a single host's
failure into graceful degradation instead of a visible outage.

## Singleton tasks during a rolling deploy

Some deployment steps must run exactly once for the whole fleet, not once per
host — a [database migration](database-migration-scripts.md), or clearing a
shared cache. Running such a step redundantly on every host in the batch is
at best wasteful and at worst actively harmful (a migration applied twice).
These steps should be pinned to run against a single designated host (or
delegated to a dedicated management target) rather than included in the
per-host deployment loop.
