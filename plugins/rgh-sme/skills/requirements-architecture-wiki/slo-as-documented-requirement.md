---
type: concept
title: SLO as Documented Requirement
description: >
  A service level objective is a reliability requirement, and setting one
  well means treating it with the same rigor Volere expects of any
  requirement — a fit criterion, an explicit rationale, ownership, and
  discoverability.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 5, ch. 6, ch. 15, Appendix A"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (ed. Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2, Appendix A, Appendix B"
---

A service level indicator (SLI) is, in effect, an automated, continuous
check on whether a stated user-journey requirement is actually being
honored in production — and setting a service level objective (SLO) is a
requirements-scoping exercise, not just a monitoring configuration task.
An SLO belongs in the same document as the user journeys it protects, for
the same reason a [fit criterion](fit-criterion.md) belongs attached to
the requirement it verifies rather than living separately.

The clearest worked template for this treats an SLO like a fully specified
Volere requirement: **ownership** and **approvers** (never a single
person — outside-team senior engineers or dependent-team representatives
should be included); **definition status** (proposal date, last-updated
date — incremented on every revisit even when nothing changes, approval
date, next scheduled revisit date, prior versions kept via changelog); a
plain-language service overview; the SLI/SLO stated both in plain English
and as a precise formula, linked to a live dashboard rather than recorded
as a static number that can silently go stale; and — the section most
often skipped elsewhere — an explicit **rationale section** explaining why
these specific SLIs and targets were chosen, honestly flagged as ad hoc
where it is, because this is exactly the institutional knowledge that
otherwise disappears once the people who set the target move on. A
companion **error budget policy** document names who owns enforcement and
what concrete action each budget-miss state triggers, with the same
rationale-for-the-threshold requirement.

Discoverability matters as much as content: a central searchable index
(service names outlast team or org names, which get reorganized), and
documentation-as-code linking the definition directly to live
configuration so the two cannot drift apart unnoticed — the same principle
as [stable vs. volatile documentation](stable-vs-volatile-documentation.md)
applied to a specific requirement rather than to documentation in general.
See [requirement revisit triggers](requirement-revisit-triggers.md) for
what should prompt reopening a target like this one.
