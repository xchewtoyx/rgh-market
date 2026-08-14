---
type: concept
title: Nonfunctional Requirements Specification Template
description: >
  A standalone "Supplemental Specification" document, organized by
  quality category, gives non-functional requirements a fixed home when
  a team's process has no natural place for a requirement that doesn't
  belong to any single backlog item.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 17"
---

Where the [Volere specification template](volere-specification-template.md)
folds non-functional requirements into one part of a larger, unified
requirements document, some teams instead maintain a standalone
"Supplemental Specification" dedicated entirely to
[non-functional requirements](non-functional-requirement.md) and
[mandated constraints](mandated-constraint.md), organized by quality
category: introduction (purpose, scope, definitions, references), then a
section per category — usability, reliability, performance,
supportability, security, and so on — followed by applicable standards
(citing the specific relevant section, per the [incorporation-by-reference
hazard](incorporation-by-reference-hazard.md)), internationalization and
localization, required physical deliverables, installation and
deployment, and a catch-all "other requirements" section.

The choice between folding NFRs into a unified specification and giving
them their own supplemental document is mostly a question of which
process a team already has a natural home for: a team already producing a
single Volere-style specification should keep NFRs inside it rather than
fragmenting the record across two documents; a team whose process is
otherwise backlog-only (no natural home for a requirement that isn't
scoped to one backlog item) benefits from a fixed, standalone NFR document
so that quality requirements have exactly one place to live rather than
being scattered across ad hoc comments on whichever stories happened to
prompt them.
