---
type: concept
title: Change-Size Gating
description: >
  Automatically flag or block a change whose size is anomalously large
  relative to normal — lines changed, records affected, or percentage
  delta — since an unexpectedly huge change is a strong, cheap-to-detect
  signal of a mistake rather than intent.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2, ch. 6"
---

# Change-Size Gating

A change's raw size is a surprisingly good, cheap proxy for risk that is
independent of what the change actually does: an operator who meant to
edit one firewall rule but instead generated a diff touching every rule,
or a data import that would overwrite 30% of records when normal daily
churn is under 20%, is very likely acting on a mistake (a bad template
expansion, a wrong scope, a stale source file) rather than genuine intent.
Gating on size catches this class of error before it lands, without
needing to understand the change's semantics at all.

Two forms of the same technique:

- **Code/config change-size gating**: require additional approval, or
  block automatically, when a change exceeds a threshold measured in lines
  changed or percentage of a generated artifact affected. This is a
  specific, automatable instance of the human-judgment call an experienced
  reviewer already makes ("this diff looks bigger than it should be for
  what the ticket describes") — see [continuous deployment automated
  gates](continuous-deployment-automated-gates.md) for the general
  principle of converting such hunches into explicit gate conditions.
- **Data import change-limit**: for periodic bulk data imports, require
  manual approval if a batch would change more than a configured
  percentage of records (e.g. a weekly import updating ≥30% of records
  when normal churn is under 20%) — this catches a corrupted or wrongly-
  scoped source batch before it propagates, the same role [safe
  configuration change properties](safe-configuration-change-properties.md)'
  gradual-deployment property plays for config, applied instead to bulk
  data.

Like most pre-checks, change-size thresholds tend to be added reactively —
after a specific incident exposes the gap a size check would have caught —
rather than derived up front, so the threshold itself should be revisited
and tightened as real incidents inform what "anomalously large" actually
means for a given system.
