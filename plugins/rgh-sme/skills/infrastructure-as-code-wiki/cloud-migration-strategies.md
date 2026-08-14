---
type: concept
title: Cloud Migration Strategies (the 6 R's)
description: A vocabulary of six distinct strategies for moving an infrastructure component to the cloud — rehost, replatform, repurchase, refactor, retain, or retire — each trading off migration effort against how much cloud-native benefit is captured.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Susanne Kaiser), ch. 10"
---

When moving an infrastructure component from on-premises (or one platform) to the cloud, "migrate it" is underspecified — there are several distinct strategies available per component, each a different trade-off between migration effort and how much cloud-native benefit is captured:

- **Rehost** ("lift and shift") — copy the component as-is onto cloud infrastructure with no architecture change, for example moving a self-managed VM's image onto a cloud-hosted VM. Lowest effort and fastest, but captures none of the cloud platform's native elasticity, managed-service automation, or operational offload.
- **Replatform** ("lift, tinker, and shift") — swap the component for a cloud-managed equivalent that preserves the surrounding application's architecture while gaining cloud-native characteristics: managed scaling, availability, and automated operations. For example, replacing a self-hosted relational database with a managed database-as-a-service, keeping the same engine and schema so the application layer barely changes. Can also target a private cloud instead of a public one, trading some of the managed-service benefit for more control over compliance and data placement, while the organization retains responsibility for the underlying compute.
- **Repurchase** ("drop and shop") — replace a self-run application outright with an equivalent SaaS offering. Effort scales with how much configuration, data, and customization has to migrate into the new product rather than with any code change.
- **Refactor** (re-architect) — restructure the component to exploit cloud-native features directly, typically breaking a larger unit into smaller ones (a monolith into services, or into serverless functions). Highest effort and highest cloud adoption; usually justified by a concrete need for better scalability, elasticity, or delivery agility rather than migration for its own sake.
- **Retain** — leave the component where it is for now, because it isn't ready to move or because compliance constraints block it; can be combined with the other strategies as a deliberate hybrid state rather than a single migration wave.
- **Retire** — decommission a component that's redundant or being consolidated, rather than migrating it at all.

Choosing among these per component (rather than applying one strategy uniformly across an entire estate) keeps migration effort proportional to the benefit each component can actually realize — a rehost is appropriate for a component with no near-term need for cloud-native scaling, while replatforming or refactoring is worth the extra effort for components whose growth or reliability needs the platform's managed capabilities. Replatforming a stateful component specifically — a database, search index, or message broker — still has to solve the problem of migrating live state without loss or downtime, which is the same problem [blue-green migration for stateful infrastructure](blue-green-migration-for-stateful-infrastructure.md) addresses: replicate into the new managed instance, keep it current, then cut over reads and writes once it's confirmed caught up, using whichever replication mechanism the specific stateful technology provides (snapshot-and-restore, change-log replication, or a purpose-built mirroring tool).
