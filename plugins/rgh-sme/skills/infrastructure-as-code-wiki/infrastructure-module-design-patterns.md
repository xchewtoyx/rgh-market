---
type: concept
title: Infrastructure Module Design Patterns
description: Five creational patterns — Singleton, Composite, Factory, Prototype, and Builder — adapted from software design to classify what kind of infrastructure module a given piece of code should be.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 3"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), Appendix B"
---

Borrowing from classic software design patterns gives a useful vocabulary for classifying infrastructure modules by what they're actually for, distinct from how [low-level or high-level](low-level-vs-high-level-infrastructure-languages.md) their language is:

- **Singleton** — encapsulates a unique, rarely-changed, single-instance resource: a cloud provider account or project, a root DNS hosted zone, an organization-level IAM root, a master TLS certificate. Very low complexity, but deliberately not designed for replication across environments.
- **Composite** — groups related resources into a managed hierarchy that callers treat as one unit, such as a network module bundling a VPC with its subnets. This is essentially the [bundle module pattern](bundle-module-pattern.md) by another name; it risks becoming a [monolithic stack](monolithic-stack-antipattern.md) if it keeps absorbing unrelated resources.
- **Factory** — takes input parameters to instantiate a customized instance of a standard resource type, such as a server factory accepting name, subnet, and machine type. This corresponds to the [facade module pattern](facade-module-pattern.md) when its parameter surface stays simple, and drifts toward the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md) once the customization needs real logic.
- **Prototype** — returns a copy of standardized metadata or defaults without provisioning anything itself: standard tags, standard labels, baseline alert thresholds, preset firewall rules. Its value is centralizing an organization's defaults in one place that factories and other modules can pull from and, where necessary, override.
- **Builder** — orchestrates multiple factories and sub-modules into a complete, high-level system exposed through simple configuration flags, such as a Kubernetes platform builder assembling VPC, node pools, ingress, and monitoring. This is the composable, top-down shape an [abstraction layer](abstraction-layer-for-infrastructure.md) usually takes at its outermost level, and it inherits that pattern's trade-off of hiding real complexity behind a simple interface.

Whether a repeated pattern is worth extracting into one of these module shapes at all, rather than left as duplicated inline code, is governed by [flexibility mechanism cost justification](flexibility-mechanism-cost-justification.md) — the module's own authoring and testing cost has to be paid back across enough consuming call sites.

Choosing between them comes down to a short set of questions: is the resource global and rarely modified (Singleton)? Is it static metadata copied elsewhere (Prototype)? Does it take inputs to produce a customized resource (Factory)? Does it bundle already-related resources (Composite)? Does it orchestrate several of the above into a higher-level system (Builder)? When only a raw cloud SDK or API is available, rather than a declarative DSL, the same shape can still be imposed by wrapping each resource in an idempotent Create/Read/Update/Delete (CRUD) module and orchestrating those modules with a Builder-style script.

A recurring implementation problem inside a **Factory**-shaped module is offering a sensible, per-platform default for a value that a caller should still be free to override — a config-file path that differs between operating system families, say. Naively hardcoding the platform-specific value inside the module's overridable-defaults layer breaks the moment a caller actually wants to override it, since the module's own logic would silently recompute and clobber the override on every run. A robust fix: give each platform variant its own private, non-overridable value (conventionally named to signal it's an internal implementation detail, not part of the module's public interface); at module-evaluation time, pick the right private value for the current platform; then set the module's real, publicly-overridable default from that picked value, but only if the caller hasn't already supplied their own override. This gets both properties at once — a correct value out of the box on every supported platform, and a value callers can still freely override — without one clobbering the other.
