---
type: concept
title: Ephemeral Compute Instances
description: >
  Managed-compute workers treated as interchangeable cattle — any instance
  may be killed and replaced by the scheduler without human intervention,
  which requires stamp-out automation and off-machine state.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Ephemeral Compute Instances

In a managed-compute fleet (Borg, Kubernetes, cloud autoscaling groups),
the scheduler may **unilaterally kill and relocate** any worker — kernel
updates, bad disks, rebalancing — and the application author should neither
know nor care why. The operational model contrasts **pets** (named servers
that need human nursing when broken and are hard to replace) with
**cattle** (numbered replicas a failed member is removed and a fresh one
stamped out automatically, with zero manual SSH or package installation).

Cattle applies equally to VMs and containers: what matters is that a new
instance can be provisioned from a known image or template with no per-host
tuning. Pet fleets impose linear-or-worse maintenance as the fleet grows;
cattle fleets self-heal without weekend pages.

Cattle alone is not sufficient — the **processing architecture** must
tolerate [partial failure](partial-failure.md) gracefully. At hundreds of
parallel workers, losing one replica is routine, not exceptional; static
work assignment can waste tens of minutes of progress per death. See
[dynamic work assignment](dynamic-work-assignment.md) for the standard fix.

For **serving** traffic, automatic replacement restores a healthy fleet, but
user-visible errors during churn require extra design: the scheduler may
signal intent to reschedule ahead of time so a container can enter a
**lame duck** state — refuse new requests while draining in-flight work —
and the [load balancer](datacenter-load-balancing.md) must honor that
signal and redirect elsewhere.

Any **local or in-process state** is lost on replacement (and local disk is
lost if the job moves machines). Treat it as transient; push durable state
to [replicated storage](single-leader-replication.md) or accept bounded loss
for cache and batch outputs. See [stateless services and session
affinity](stateless-services-and-session-affinity.md).

Hardcoding hostnames breaks the model — callers reach services through
[service discovery](service-discovery.md) indirection the scheduler
maintains.
