---
type: concept
title: Actionable Paging Hygiene
description: Every page sent to an on-call human should represent something only a human can resolve, reflect real user impact, and point to a specific runbook — anything less erodes trust in the alerting system.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
---

Baseline hygiene rules for paging alerts:

- Every page must be **actionable** — there must be something a responder can actually do about it right now.
- Every page must require **human intelligence**; if the response is fully mechanical, automate it instead of paging a person.
- Paging alerts should trigger on real, [symptom-based](symptom-based-vs-cause-based-alerting.md) user-facing conditions, not presumed causes.
- Every alert should link to a specific runbook — see [runbooks: value and limits](runbooks-value-and-limits.md) for what a runbook is and isn't good for.

Violating these rules is one of the main paths to [alert fatigue and normalized deviance](alert-fatigue-and-normalized-deviance.md): non-actionable pages train responders to dismiss alerts, so the one page that matters has to fight through learned distrust.
