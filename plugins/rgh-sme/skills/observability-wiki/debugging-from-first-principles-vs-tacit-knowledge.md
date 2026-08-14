---
type: concept
title: Debugging from First Principles vs. Tacit Knowledge
description: Debugging from accumulated tacit knowledge (runbooks, dashboard familiarity) works but doesn't scale or transfer, since modern systems rarely fail the same way twice; debugging from first principles — treat understanding as provisional, form a hypothesis, test it against telemetry, iterate — is teachable, repeatable, and doesn't require prior system familiarity.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 8"
---

Two contrasting debugging modes:

- **Debugging from known conditions** — relies on accumulated tacit knowledge, runbooks, and dashboard familiarity built up over time on a specific system. It works, but it doesn't scale to new engineers or transfer across systems, and it's poorly matched to modern systems, which rarely fail the same way twice as they grow more complex. [Recognition-primed diagnosis](recognition-primed-diagnosis.md) describes the cognitive mechanism behind this mode: pattern-match the situation, mentally simulate the first plausible fix, act if it holds up — fast and usually right, but only as good as the operator's library of prior patterns.
- **Debugging from first principles** — treat your current understanding of the system as provisional; form a hypothesis, test it against telemetry, iterate. This is the [core analysis loop](core-analysis-loop.md) in practice: a repeatable, teachable, evidence-driven method that doesn't require prior familiarity with the specific system, and which *democratizes* debugging — curiosity and diligence matter more than tenure.

This doesn't make runbooks worthless — see [runbooks: value and limits](runbooks-value-and-limits.md) — but it reframes their role: a good entry point and escalation path, not a substitute for being able to investigate a failure mode nobody has documented yet. This distinction is the practical answer to [known-unknowns vs. unknown-unknowns](known-unknowns-vs-unknown-unknowns.md): tacit-knowledge debugging only scales to known-unknowns, while first-principles debugging is what's actually required for a novel, unknown-unknown failure.
