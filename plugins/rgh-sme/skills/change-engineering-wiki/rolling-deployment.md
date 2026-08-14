---
type: concept
title: Rolling Deployment
description: >
  Update a fleet to a new version incrementally, node by node or shard by
  shard, rather than all at once, so a bad version is caught while most of
  the fleet is still running the old one.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 14"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 8"
---

# Rolling Deployment

Rolling deployment updates a fleet incrementally — one node, one shard, or
one small group at a time — instead of cutting every instance over
simultaneously. Each unit is drained, updated, and reintroduced before the
next one starts, so a defect is exposed on a shrinking-but-bounded slice of
the fleet while most of it is still serving the previous, known-good
version.

Unlike [blue-green deployment](blue-green-deployment.md), rolling
deployment does not require a full duplicate environment — it updates the
existing fleet in place, at the cost of a slower, less instantaneous
rollback (reverting means rolling the same units back through the old
version, rather than a single router flip). Unlike [canary release](canary-release.md),
a plain rolling deployment does not necessarily hold back an evaluation
step between batches — canarying can be layered on top of a rolling
deployment by evaluating each batch before letting the rollout proceed to
the next one.

For clustered stateful systems, the mechanics differ by replication
topology: write-anywhere clusters can drain, patch, and reintroduce any
node in any order; write-leader clusters must patch followers first, then
fail over to a pre-patched node before updating the former leader.

Even a rolling deployment's per-instance gap (drain, restart, reintroduce)
is too much for some systems (e.g. active sessions that can't be dropped);
[hitless in-service software upgrade](hitless-in-service-software-upgrade.md)
patches a process's code in place instead of replacing the instance.
