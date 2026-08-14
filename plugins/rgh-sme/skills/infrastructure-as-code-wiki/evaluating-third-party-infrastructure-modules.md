---
type: concept
title: Evaluating Third-Party Infrastructure Modules
description: What to check before adopting an external module or provider plugin — secure defaults, supply-chain risk, and license obligations — and mirroring approved dependencies internally to reduce exposure to upstream changes.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 13"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 6"
---

Adopting a third-party module or provider plugin — from a public registry, an open-source project, or a vendor — carries risk beyond whether it does what it claims, and is itself worth weighing as a [reversible or irreversible decision](reversible-infrastructure-decisions.md): how hard would it be to walk back once the module is load-bearing in production? Worth checking before internal teams start depending on it: whether it applies secure defaults and behaves predictably without hidden complexity; whether its code contains telemetry, hardcoded external endpoints, or other signs of unauthorized data exfiltration, ideally checked with the same [policy-as-code](policy-as-code-for-infrastructure.md) scanners already used on internal code; and its license — permissive licenses (MIT, Apache 2.0, BSD) allow private modification and embedding without obligations, while copyleft licenses (GPL, AGPL, MPL) can require publishing modifications under the same license, which usually needs legal review before adoption in an organization's own codebase.

Once a module or plugin passes this evaluation, mirroring it into an internal artifact registry — rather than continuing to pull directly from the public source on every build — reduces exposure to two separate risks: an upstream registry outage blocking builds, and an upstream maintainer publishing a malicious or broken update that would otherwise reach internal pipelines automatically. This is the infrastructure-tooling analogue of pinning dependency versions rather than tracking a moving upstream target; see [Terraform module versioning and promotion](terraform-module-versioning-and-promotion.md) for the equivalent discipline applied to an organization's own internal modules.

A community role/module registry's requirements manifest is the same discipline applied to [server configuration code](server-configuration-code.md): rather than installing individual third-party roles ad hoc, listing every one a project depends on in a single version-controlled file — with each entry pinned to an explicit version and, where the role lives outside the primary registry (a plain git or HTTP source), an explicit source URL and local name — makes the whole dependency set reproducible from one command and reviewable as a diff when a version bumps, rather than depending on whatever happened to be installed on someone's machine at the time.
