---
type: concept
title: Self-Documenting Declarative Systems
description: Using declarative, inspectable automation (configuration, deployment, dependency definitions) as the source of truth so the system documents its own current state instead of relying on separately-maintained prose.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 10"
  - title: "Infrastructure as Code"
    resource: "Infrastructure as Code (Morris), ch. 4"
---

Prose documentation of a system's configuration, dependencies, or deployment topology drifts from reality the moment the system changes and the prose isn't updated in lockstep. A declarative, machine-readable definition of that same state doesn't have this failure mode, because the definition and the running system are the same artifact — inspecting the definition *is* inspecting the current truth, not a claim about it that might be stale.

## The Pattern

- **Let automation express desired state declaratively**: Infrastructure-as-code, configuration-as-code, and dependency manifests describe what should exist. Because the running system is produced from that same definition, reading the definition tells a maintainer what's actually there, not what someone once wrote down about it.
- **Scaffolding for step-by-step discovery**: Tooling that generates or walks through a system's structure interactively (rather than a static diagram) lets a new maintainer explore the real current structure at their own pace.
- **Machine documentation exposes facts without a prose intermediary**: Where a fact about the system can be queried directly from the system itself (a schema, a live dependency graph, a running configuration), prefer exposing that fact through tooling over restating it in prose that will need separate upkeep.
- **Executable specifications double as behavior documentation**: Behavior-Driven Development scenarios (readable prose examples wired to automated step definitions) describe intended system behavior in a form that is continuously checked against reality — a failing scenario is simultaneously a bug report and a signal that the documentation itself is now wrong. This gives prose-like readability the same self-correcting property as declarative config, as long as the correspondence between the scenario text and its implementation stays direct rather than being hidden behind opaque step libraries.
- **Runtime introspection for facts that only exist while the system runs**: Some authoritative facts — which services are actually deployed, current topology, live configuration values, in-flight event flows — don't exist in any static definition at all, only in the running system. Expose these through registries, reflection, or queryable endpoints so a maintainer can ask the live system directly, rather than trusting a deployment diagram that was accurate only at the moment someone drew it.

## Why This Matters for Handover

This is the most durable way to solve the [stable vs. volatile knowledge](separating-stable-and-volatile-knowledge.md) problem for the volatile side: rather than writing prose about configuration values, ports, or dependency versions and hoping someone updates it, make the volatile facts queryable directly from the live system, and reserve prose for the stable, slow-changing context that's actually worth writing carefully. A new operator who was not involved in building the system can trust a declarative definition or a live query in a way they cannot fully trust a hand-maintained document, because the former cannot silently drift out of sync with what's actually running.
