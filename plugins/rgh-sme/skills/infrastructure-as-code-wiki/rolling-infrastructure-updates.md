---
type: concept
title: Rolling Infrastructure Updates
description: Updating a fleet's nodes or module instances one at a time — cordoning, draining, testing, and cutting over each before moving to the next — rather than replacing the whole fleet in one operation.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 10"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 9"
---

A rolling update applies a change to one node, or one instance of a module, at a time, rather than to an entire fleet simultaneously: cordon the target so it stops receiving new work, drain whatever work it's currently handling, apply and verify the update, cut traffic back over to it, and only then move to the next one. This bounds the [blast radius](blast-radius.md) of a bad change to whatever fraction of the fleet has been updated when the problem is noticed, and it avoids the availability gap a full-fleet, all-at-once replacement would cause.

Rolling updates are the incremental, node-by-node sibling of the [blue-green infrastructure change](blue-green-infrastructure-change.md) pattern — where blue-green swaps a whole environment or component at once via a parallel instance, rolling updates apply the same "replace, don't mutate in place" discipline at finer grain, one member of a pool at a time, which fits naturally with server or application clusters where the platform already understands how to add and remove individual instances (see [zero downtime autoscaling group deployment](terraform-zero-downtime-asg-pattern.md) for a concrete implementation on a compute autoscaling group).

[Feature flags](feature-toggles-for-infrastructure.md) are a common companion technique here: a rolling update can attach new instances behind a flag that starts disabled (preserving current behavior and idempotency), get flipped on once the new instances are verified, and finally have the flag and any now-dead old-path code removed once the rollout has fully stabilized.

For a very large fleet, a strict one-at-a-time sequence is too slow to be practical — see [canary infrastructure rollout](canary-infrastructure-rollout.md) for the variant that starts with a very small batch and widens geometrically instead of linearly.

Two concrete, nameable controls tune how a rolling update bounds its own blast radius: a **batch-size** setting controls how many hosts a single pass processes concurrently — as an absolute count or a percentage of the fleet — trading rollout speed against how much of the fleet a bad batch can affect before the run stops; a **failure-threshold** setting controls what fraction of a batch is allowed to fail before the whole update aborts rather than proceeding to the next batch, so a systemic problem (a broken new version, not a one-off flaky host) halts the rollout with most of the fleet still on the known-good version rather than continuing regardless. Sizing both is an explicit trade-off against available spare capacity: more headroom tolerates larger batches and looser failure thresholds, while a fleet running close to capacity needs smaller batches and tighter thresholds — or more capacity provisioned before the rollout starts.

Where a load balancer sits in front of the fleet, a rolling update through it typically wraps each node's update in three phases: before the update, mark the node disabled/drained in the load balancer's own configuration so no new traffic reaches it; run the actual update against the now-quiescent node; after the update, poll the node until it's confirmed healthy again, then re-enable it in the load balancer before moving to the next node. If the update step fails partway through, the node simply stays disabled in the load balancer rather than being put back in front of live traffic in a broken state — the rest of the fleet keeps serving normally while the one bad node is investigated. This pattern generalizes beyond any one load balancer implementation: it's the same drain-update-verify-restore sequence regardless of which load-balancing or [service-discovery mechanism](service-discovery-mechanisms.md) is actually in front of the fleet.
