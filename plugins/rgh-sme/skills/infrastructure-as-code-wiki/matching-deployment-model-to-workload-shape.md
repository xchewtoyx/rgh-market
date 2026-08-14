---
type: concept
title: Matching Deployment Model to Workload Shape
description: Four characteristics of a workload — statefulness, lifecycle duration, pooling, and redundancy topology — that determine which infrastructure deployment pattern actually fits it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 10, ch. 14, ch. 21"
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 9"
---

Before choosing an infrastructure deployment model — a single server, a cluster, a FaaS platform, a particular redundancy topology — it's worth checking the workload's actual shape against four independent axes. Each axis points toward a different existing pattern in this bundle, so the goal here isn't to re-explain those patterns but to help pick which one to load next.

**Stateful vs. stateless.** A stateless workload can be destroyed and rebuilt freely from code with no data-loss risk, which is what makes [immutable servers](immutable-server-pattern.md) and ordinary [blue-green infrastructure changes](blue-green-infrastructure-change.md) straightforward. A stateful workload — a database, an object store, anything holding data the workload itself doesn't reproduce on restart — needs an explicit plan before any of that applies: see [data continuity strategies](data-continuity-strategies.md) for the general lock/segregate/replicate/reload toolkit, and [blue-green migration for stateful infrastructure](blue-green-migration-for-stateful-infrastructure.md) for what a cutover actually looks like once dual-writes and replication are involved instead of a single traffic switch.

**Long-running vs. short-lived.** A workload that runs continuously, holding state in memory or maintaining open connections, fits the [application runtime layer](application-runtime-layer.md) model of servers, containers, or an [application cluster](application-cluster-as-code.md) that keeps instances alive and replaces them on failure. A workload that's genuinely short-lived and event-triggered — respond to a request, process a queue message, run on a schedule, then terminate — is a better fit for [FaaS serverless infrastructure](faas-serverless-infrastructure.md), where the infrastructure code shrinks because there's no host server lifecycle to manage, only the surrounding networking, storage, and triggers.

**Single instance vs. pooled/clustered.** A workload that needs to scale horizontally or tolerate individual-instance failure belongs in a pool the platform actively manages — an autoscaling group or an [application cluster](application-cluster-as-code.md) — rather than as a hand-provisioned singleton. Once a cluster is in the picture, keep its own provisioning separate from the workloads it schedules: see [separating cluster provisioning from workload deployment](separating-cluster-provisioning-from-workload-deployment.md) for why combining them in one stack fails in a specific, hard-to-diagnose way. Changes to a pooled workload should generally go out via [rolling infrastructure updates](rolling-infrastructure-updates.md) rather than replacing the whole pool at once.

**Redundancy topology.** Whether a workload runs as a single environment with a cold standby or as multiple environments simultaneously sharing live traffic is a further, largely independent choice — see [active-passive vs active-active topology](active-passive-vs-active-active-topology.md). This choice constrains what the other three axes can practically achieve: active-active only works if the workload's statefulness story (above) tolerates multiple concurrently-live copies, and [continuous disaster recovery](continuous-disaster-recovery.md) is naturally easier to exercise routinely against an active-passive standby than against a topology with no idle environment to fail over to.

None of these axes are exclusive — a real system usually has to answer all four for a given workload before its deployment model is actually settled — but treating them as separate questions keeps each answer traceable to a specific characteristic of the workload rather than a default reached for out of habit.
