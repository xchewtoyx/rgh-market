---
type: concept
title: STAR Incident Action Plan
description: A four-milestone structure — Size up, Triage, Act, Review — for building and executing an incident action plan under time pressure.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 3"
---

**STAR** structures an incident commander's action plan into four
milestones:

- **Size up**: build situational awareness — not just that an incident
  exists, but what is actually happening — by pulling monitoring data and
  SME input into the "conditions" part of a [CAN report](can-report.md).
  The reminder here is blunt: "monitoring tools provide data, humans use
  judgment to make decisions."
- **Triage**: assign a severity level so the right kind and amount of help
  gets engaged — see [incident severity classification](incident-severity-classification.md)
  for the tiering schemes this maps onto.
- **Act**: execute a plan built from a clear, data-backed understanding of
  the problem, a stated objective, a timeline, and a backup plan, confirmed
  through a pre-action CAN report that gets explicit support (not just
  passive agreement) from each SME — see [seeking support, not
  consensus](incident-bridge-communication-patterns.md). A short list of
  discipline rules governs how information is handled while acting: treat
  everything as news rather than good or bad news, keep raw data separate
  from opinion unless asked, solve before notifying where possible, and
  don't let hope substitute for a plan.
- **Review**: an ongoing loop of periodic CAN-report checkpoints while the
  incident is live, plus two follow-up reviews once it's resolved — an
  [after action review](after-action-review.md) of how the *people*
  responded, and a root-cause analysis, done separately and afterward, of
  why the *technology* failed. A fix applied during Act that restores
  service without addressing the underlying cause needs to be documented
  and fed back into peacetime work, or it becomes an undocumented "time
  bomb" for a future incident.

STAR gives the [incident commander's](incident-command-system.md)
[command presence](command-presence.md) a repeatable shape to apply,
regardless of how large or small the incident turns out to be.
