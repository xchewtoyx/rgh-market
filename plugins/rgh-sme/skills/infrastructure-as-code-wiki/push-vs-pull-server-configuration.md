---
type: concept
title: "Push vs Pull Server Configuration"
description: The two mechanisms for running server configuration code against an instance — a central process connecting out to servers, versus an agent on each server pulling and applying code itself.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 12"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), Introduction"
---

With **push server configuration**, a process outside the server connects to it and executes the configuration tool — typically over SSH, run by hand, from a central orchestration server, or from a CI/CD job. Push gives finer control over timing, which matters when a sequence of activities (like a software deployment) needs to be orchestrated across multiple servers from one place. It requires each server to accept incoming connections for the configuration process, which is itself an attack surface, so it demands strong authentication and careful secret management — see [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md) — and it's awkward to combine with servers the platform creates automatically (autoscaling, auto-recovery), though not impossible.

With **pull server configuration**, a process running on the server itself downloads and applies the code — triggered on first boot, and on a schedule thereafter for [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md). Pull avoids needing to open inbound access to servers at all, which shrinks the attack surface, and it naturally handles platform-created instances, since the bootstrapping (via cloud-init or similar) is baked into the [server image](server-image-as-code.md) rather than depending on an external actor reaching the new instance. Saltstack's messaging-based model is a variant: agents connect out to a shared service bus and receive commands from it, rather than either polling on a schedule or accepting inbound connections.

Either pattern can be paired with the [apply on change antipattern](apply-on-change-antipattern.md) or with [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) — the push/pull choice is about *how* code reaches a server, while apply-on-change versus continuous synchronization is about *how often* it's applied.

Ansible is a concrete, deliberately agentless instance of the push model: rather than running a persistent daemon on every managed node (the agent-based model used by tools like Puppet and Chef, where each node pulls its configuration on a schedule), it connects out over plain SSH, transfers a small module payload, executes it, and removes it — no extra software runs on managed servers between applies. This was an explicit design goal (named alongside "clear," "fast," "complete," and "secure" in the tool's own stated design principles): no agent means no extra memory footprint on managed servers, no daemon to install/upgrade/keep alive, and no additional listening port beyond SSH itself. The trade-off is the push model's usual one — a control machine needs SSH access to every managed server, so authentication and secret management for that access path matters (see [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md)).
