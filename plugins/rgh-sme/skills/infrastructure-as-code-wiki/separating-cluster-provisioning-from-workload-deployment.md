---
type: concept
title: Separating Cluster Provisioning from Workload Deployment
description: Why provisioning a cluster and deploying workloads onto it need separate stacks and state, rather than one module configuring a workload-orchestration provider from the very cluster it just created.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 7"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 14"
---

A design that looks convenient — one module that both creates a Kubernetes cluster and configures the Kubernetes provider to deploy workloads onto it, using the cluster's own outputs (endpoint, credentials) to configure that same provider — fails in a specific, hard-to-diagnose way: most stack tools try to resolve every provider's configuration during planning, before any resource in that plan actually exists, so a provider configured from a not-yet-created cluster's outputs produces intermittent authentication errors, broken dependency resolution, or outright planning failures, depending on ordering.

The reliable design instead splits this into two phases with two separate states: one stack provisions the cluster infrastructure itself (networking, IAM, the managed cluster resource) and exposes what a workload-orchestration provider will need as outputs; a separate, downstream stack configures that provider from the first stack's already-applied outputs and deploys workloads onto the now-real cluster.

This is a specific, concrete case of the general principle of [aligning infrastructure boundaries with component life cycles](drawing-boundaries-between-infrastructure-components.md) — cluster infrastructure and the workloads running on it change at very different rates and for different reasons, and the [micro stack pattern](micro-stack-pattern.md) that follows from that alignment isn't just a convenience here, it's what avoids a genuine planning-order failure mode that a single combined stack can't reliably work around.

Building the cluster infrastructure itself has its own build-vs-buy spectrum worth naming: a minimal bootstrapping tool bundled with the orchestrator (functional on any infrastructure, but leaving the surrounding automation to the team); a dedicated cluster-lifecycle tool with broader production features (upgrades, more environments supported out of the box); or a managed, platform-provided cluster service configured through the platform's own stack tooling, trading operational ownership of the control plane for less flexibility. Whichever is chosen, cluster bootstrapping tends to accumulate environment-specific workarounds (networking-plugin configuration tuned to the exact virtual network topology in use, node IP autodetection overridden because the platform's own detection gets confused) and deliberate version pinning across every cluster component together, rather than letting each float independently — both are ordinary instances of [minimizing variation](minimize-variation-principle.md) and the [reproducibility principle](reproducibility-principle.md) applied to a cluster's own control plane.

Before adopting this pattern at all, it's worth checking whether the workload is actually a good fit for a workload orchestrator in the first place: a poor fit is a workload that depends on locally-available stateful data (see [data continuity strategies](data-continuity-strategies.md) for why most databases and filesystem-heavy applications struggle here), while a workload with pieces that can run ad hoc — a periodic, cron-like job — is a low-risk starting point for incremental adoption, mirroring the same incremental-adoption instinct behind [minimizing variation](minimize-variation-principle.md) and small, [incremental infrastructure changes](incremental-infrastructure-change.md) generally.
