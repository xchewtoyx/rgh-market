---
type: concept
title: Infrastructure Change Taxonomy
description: Classifying infrastructure changes as standard, normal, or emergency based on risk and routineness, and matching each category to how much automated delivery versus manual approval it goes through.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 7"
---

Not every infrastructure change carries the same risk, so it's worth explicitly classifying changes and matching each category to an appropriate level of automation versus human gatekeeping, rather than routing every change through the same process regardless of risk:

- **Standard changes** — low-risk, routine, frequent, with predictable behavior and a known rollback path (a container image bump, a monitoring threshold tweak, adding an environment tag). These are good candidates for **continuous deployment** — passing the automated test suite is sufficient to reach production with no manual gate.
- **Normal changes** — non-routine or architecturally significant (a core network topology change, a primary database engine upgrade). These warrant **continuous delivery** — automated testing through to a staging environment, then a deliberate peer or subject-matter-expert approval gate before production.
- **Emergency changes** — rapid hotfixes made during a live incident, prioritizing restoring service over following the normal process. These need explicit post-incident reconciliation back into IaC afterward — see [out-of-band change remediation](out-of-band-change-remediation.md) — so the emergency shortcut doesn't become permanent, silent drift.

Which category a change actually belongs in depends partly on what assurance the tooling applying it can offer before it lands — see [change assurance mechanisms by tooling](change-assurance-mechanisms-by-tooling.md) for how a reviewable plan, an idempotent dry-run, or immutable replace-with-rollback each justify a different amount of automated trust.

This taxonomy gives concrete criteria for deciding where a given team or system sits on the **CI → CD → continuous deployment** continuum, and for which categories: continuous integration alone (linting, static tests on every commit) is table stakes for everything; continuous delivery adds automated provisioning into a test environment plus dynamic tests, pausing before production for a manual quality gate — appropriate for normal changes; continuous deployment removes that gate entirely for changes that pass every automated stage, appropriate for standard changes given adequate test coverage and a reliable rollback path. A specific anti-pattern to watch for at the continuous-delivery manual gate: letting unapproved changes queue up into a large batch before someone finally reviews and pushes them through together, which reintroduces exactly the [blast radius](blast-radius.md) and hard-to-diagnose-failure problems [small, incremental changes](incremental-infrastructure-change.md) are meant to avoid.
