---
type: concept
title: Separating Stable and Volatile Knowledge
description: Decoupling slow-changing domain orientation from fast-decaying implementation details to ensure documentation remains maintainable.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 9"
---

A primary cause of documentation decay in operational handovers is intermixing stable, high-level system context with volatile, low-level implementation details. When volatile details (such as a specific server name or UI button path) change and go out of date, readers lose trust in the entire document, causing them to abandon it.

## Stable vs. Volatile Knowledge

```
             ┌────────────────────────────────────────────────────────┐
             │                 Knowledge Stratification               │
             └───────────────────────────┬────────────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
         Stable (Evergreen)                             Volatile (Transient)
  - Business goals, architecture invariants.      - CLI commands, config files, ports.
  - Core domain terminology & data model.         - UI screenshots, package versions.
  - High long-term value, changes slowly.         - Low long-term value, changes rapidly.
  - Written as carefully composed prose.          - Handled via automation or registries.
```

- **Stable (Evergreen) Knowledge**: High-level business objectives, system boundary diagrams, domain concepts, ubiquitous language, and system invariants. This context changes very slowly and justifies investment in carefully written prose (e.g., a system README).
- **Volatile (Transient) Knowledge**: Specific IP addresses, configuration keys, database port settings, UI routes, and software package versions. These change frequently and decay rapidly.

## Best Practices for Separation

To maintain system documentation without high overhead, apply these decoupling patterns:

1. **Organize Along Stable Axes**: Structure documentation folders and files around core domain boundaries (e.g., business capabilities, service boundaries) rather than volatile axes like temporary project names, specific team ownership, or release phases.
2. **Control the Flow of Dependency**: Ensure volatile documents point to stable documents, not vice versa. For example, a volatile alert runbook should reference the stable architecture README for context, but the stable README should never list individual hostnames or temporary port mappings.
3. **Externalize Volatile References**: Rather than copy-pasting volatile values (like API endpoints or contact rosters) across multiple pages, centralize them in a single metadata file, configuration directory, or service registry. Where possible, prefer a declarative, queryable definition over a prose restatement — see [Self-Documenting Declarative Systems](self-documenting-declarative-systems.md).
4. **Use Query-Based Linking**: When linking to volatile assets like monitoring dashboards or log groups, use parameterized search query links rather than hardcoding fragile, instance-specific URLs.

To balance this separation when writing specific procedures, refer to [Playbook Maintenance Tension](playbook-maintenance-tension.md) and [Runbook and Checklist Design](runbook-checklist-design.md).
