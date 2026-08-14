---
type: concept
title: Telemetry Pipeline Agent/Gateway Architecture
description: Telemetry pipelines are typically deployed as lightweight agents near the data source doing minimal processing, feeding centralized, horizontally-scaled gateways that do the heavy processing, with a control plane managing the whole fleet's configuration and rollout.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 16"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §4.2"
---

The physical deployment of a [telemetry pipeline](telemetry-pipeline-stages.md) commonly separates into three roles:

- **Agents** — lightweight collectors deployed near the data source (sidecar, host daemon), doing minimal processing before forwarding onward.
- **Gateways** — centralized, horizontally-scaled clusters that do the heavier processing: normalization, enrichment, compliance redaction, sampling, and routing to final destinations.
- **Control plane** — manages fleet configuration and visibility across every agent and gateway, including versioned rollouts and health reporting (e.g. via OpAMP, the Open Agent Management Protocol).

Because an agent runs co-located with the workload it's collecting from, it competes with that workload for CPU on the same host — the mitigation is to run the agent at the **lowest available OS scheduler priority**, so any contention resolves in favor of the foreground application it's monitoring rather than the collector itself. Google's Dapper daemon follows this pattern and, combined with keeping collection overhead low (never more than ~0.3% of one core under a heavy synthetic load), stays effectively invisible to the traced application even under worst-case conditions.

A single collector binary (e.g. the OpenTelemetry Collector) can typically run as either an agent or a gateway, since the distinction is about deployment role and configuration (pluggable receivers/processors/exporters/extensions) rather than different software. Deployment scales up through three patterns as an organization grows: agent-only (simplest, but doesn't scale and tightly couples every source to its destination), agent+gateway (the standard production pattern), and multi-tier (local gateways feeding regional gateways, enabling HA, disaster recovery, and cost efficiency at large or geographically distributed scale).

Adoption is typically phased rather than big-bang: start with a simple pipeline on a greenfield service to build confidence, then redirect existing legacy telemetry into gateways for centralized reduction/compliance without re-instrumenting anything, and only later replace legacy agents with the standard collector once trust is established — a fragile legacy application can remain in the middle phase indefinitely as an acceptable trade-off. The same build-confidence-first sequencing applies to whether a feature is *on* by default: Google's Dapper daemon shipped disabled by default in its early days and only flipped to enabled-by-default once its stability and low overhead had been established in practice — see [auditing for unjustifiably disabled telemetry](audit-for-unjustifiably-disabled-telemetry.md) for the corresponding long-term discipline once a capability like this has graduated to on-by-default.

One deployment technique that measurably improves how close an agent gets to true ubiquity: bake the agent into the organization's standard base machine/host image, rather than requiring each service to opt in and install it separately — a service gets baseline collection for free just by being deployed on the standard image, and reaching "virtually every host" becomes a property of the image rather than something that has to be chased service by service.
