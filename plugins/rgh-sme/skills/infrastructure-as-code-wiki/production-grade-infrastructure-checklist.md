---
type: concept
title: Production-Grade Infrastructure Checklist
description: The ten operational dimensions a production infrastructure deployment needs to address beyond a working proof of concept, and why that gap routinely takes far longer than expected.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 8"
---

Getting a prototype server running with an IaC tool takes hours; getting the same thing to production-grade quality routinely takes weeks or months, because production infrastructure carries a long list of non-functional requirements a proof of concept skips entirely. Each prerequisite tends to reveal further prerequisites — configuring a database might require a VPC, subnets, IAM roles, KMS keys, security groups, TLS certificates, monitoring, and a backup policy before the database itself is even reachable — the infrastructure equivalent of "yak shaving."

Ten dimensions worth explicitly checking before calling infrastructure production-ready: core network and account setup (VPCs, subnets, IAM governance); security (encryption at rest and in transit, perimeter controls, least-privilege IAM, [secrets management](handling-secrets-in-infrastructure-code.md), host hardening); high availability ([multi-AZ/region redundancy](cloud-regions-and-availability-zones.md), health checks, auto-healing, zero-downtime delivery — see [zero downtime infrastructure changes](blue-green-infrastructure-change.md)); scalability (auto scaling, load balancing, read replicas, caching); performance (rightsizing, latency benchmarks, CDN caching); monitoring and alerting (metrics, log aggregation, dashboards, on-call paging); disaster recovery (automated backups, defined RTO/RPO, tested restores — see [data continuity strategies](data-continuity-strategies.md) and [continuous disaster recovery](continuous-disaster-recovery.md)); cost optimization (scheduled scale-down, spot/preemptible capacity, automated cleanup of unused resources); documentation (diagrams, module usage examples, runbooks); and automated testing (static analysis through end-to-end verification — see [progressive testing for infrastructure](progressive-testing-for-infrastructure.md)).

This checklist is a useful lens for scoping any given piece of infrastructure work honestly — a change that looks "done" once it satisfies its immediate functional requirement may still be missing several of these dimensions, and naming them explicitly makes the remaining work visible rather than something discovered piecemeal after go-live.
