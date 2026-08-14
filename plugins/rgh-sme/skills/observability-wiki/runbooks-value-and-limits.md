---
type: concept
title: "Runbooks: Value and Limits"
description: Runbooks remain valuable for ownership, escalation, and dependency information and a handful of good entry-point queries, but comprehensive "every failure mode" runbooks are largely wasted effort and actively dangerous once stale, because wrong documentation misleads an investigator worse than no documentation at all.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 8"
---

Runbooks are still genuinely useful for a narrow set of things: who owns a system, who to escalate to, what its dependencies are, and a handful of good entry-point queries to start an investigation with. Every alert should link to one — see [actionable paging hygiene](actionable-paging-hygiene.md).

What a runbook is *not* good for, despite how often teams try to make it do this job, is comprehensively cataloging every possible failure mode and its fix. That's largely wasted effort for a system whose failure modes multiply combinatorially as it grows (see [known-unknowns vs. unknown-unknowns](known-unknowns-vs-unknown-unknowns.md)), and it's actively dangerous once the documentation goes stale — a responder following a wrong runbook step during an incident can be led further from the answer than a responder with no runbook at all, precisely because false confidence in a plausible-looking but wrong instruction is harder to catch than an admitted absence of guidance.

The practical alternative for anything beyond the narrow entry-point role is [debugging from first principles](debugging-from-first-principles-vs-tacit-knowledge.md): a hypothesis-driven investigation using the [core analysis loop](core-analysis-loop.md), which doesn't depend on someone having anticipated and documented this specific failure in advance.
