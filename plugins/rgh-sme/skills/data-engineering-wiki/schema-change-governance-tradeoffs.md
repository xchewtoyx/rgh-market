---
type: concept
title: Schema Change Governance Trade-offs
description: >
  The spectrum between slow command-and-control schema review and fully
  automatic schema propagation, and why both extremes fail a pipeline in
  different ways.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

Handling upstream [schema evolution](schema-evolution-in-source-systems.md)
sits on a spectrum with real failures at both ends:

- **Command-and-control review**: every schema change goes through a formal
  approval process before it can land. This protects downstream consumers
  from surprise breakage, but can impose absurd lead times — a real-world
  quote of six months to add a single field at a large enterprise — that are
  unacceptably slow for teams that need to iterate.
- **Fully automatic propagation**: ingestion tooling auto-detects and
  auto-applies schema changes to the target table on arrival. This solves
  the ingestion-stage problem (the load doesn't fail), but a change can still
  silently break transformations or reports further downstream of staging,
  or quietly degrade report and model accuracy without failing anything
  loudly enough to notice.

A middle path worth considering: borrow a Git-style branching model for
schema changes. Because cloud storage is now cheap (unlike the
resource-constrained on-prem MPP systems this problem originally grew up
around), a team can maintain multiple parallel "development" versions of a
target table via the orchestration layer, letting schema and
upstream-transformation changes surface and get validated in a development
table before being promoted to the table production consumers actually
depend on — closer to a pull-request workflow than either an approval
committee or a live auto-apply.

Whichever point on the spectrum a pipeline picks, it should be paired with
proactive communication with the owning team about planned changes — the
mechanism (review, automation, or branching) reduces the *blast radius* of a
schema change, but only direct communication tells a downstream consumer
*why* a field disappeared or changed meaning.
