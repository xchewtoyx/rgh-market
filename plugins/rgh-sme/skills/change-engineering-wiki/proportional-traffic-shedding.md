---
type: concept
title: Proportional Traffic Shedding
description: >
  Migrate traffic from an old cluster to a fully-built parallel new one by
  gradually shifting the load-balanced percentage from 0 to 100, at the
  cost of running double capacity for the transition.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Proportional Traffic Shedding

Build the new version of a service on an entirely separate set of
machines, running in parallel with the old cluster, then have the load
balancer gradually shift ("shed") an increasing percentage of live traffic
from old to new until the new cluster carries 100%. The old cluster stays
up and reversible throughout — if a problem appears at any shed
percentage, traffic can be shifted back immediately.

This differs from [rolling deployment](rolling-deployment.md) and
[canary release](canary-release.md) in what's being varied: those replace
capacity in place, in-fleet, machine by machine or replica by replica.
Proportional shedding instead builds a second, independent cluster and
migrates load-balancer weight between two whole clusters — closer in
spirit to [blue-green deployment](blue-green-deployment.md), but without
blue-green's instant, single-flip cutover; the shift here is gradual and
gated on the same kind of health signal a staged rollout would use.

The defining cost is capacity: for the duration of the migration, both
clusters must be able to serve real traffic, which means holding roughly
double the steady-state capacity. This is cheap for a single-machine
service and can be prohibitively expensive at fleet scale, though the cost
shrinks over the migration as traffic (and therefore required old-cluster
capacity) drains away — freed old-cluster machines can be recycled directly
into the new cluster as the shed percentage climbs.
