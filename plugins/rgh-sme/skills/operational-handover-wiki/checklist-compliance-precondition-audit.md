---
type: concept
title: Checklist Compliance Precondition Audit
description: Verifying that the physical or logistical resources a checklist step depends on are reliably available before attributing compliance failures to operator discipline.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 2"
---

When a new checklist rolls out across many teams or sites and compliance is inconsistent, the default assumption is a discipline problem — operators aren't following the steps. Often the real cause is upstream: the resource a step depends on isn't reliably available at the point of use. In one large-scale checklist rollout, low compliance with a hygiene step traced back to the required supply being simply missing from most sites' stock, not to operators skipping it.

## The Audit

Before treating low checklist compliance as a training or discipline issue, audit whether every step's precondition is actually satisfied at the point of execution:

- **Physical materials**: Is the required tool, credential, access grant, or supply actually present and stocked where the step is performed, at every site or team running the checklist — not just at the site where the checklist was authored and tested?
- **System preconditions**: For operational (not just physical) checklists, does the operator actually have the access, permissions, or tooling the step assumes, in every environment the checklist is meant to run in?

## Why This Requires Organization-Level Fixes, Not Just Reminders

A missing precondition cannot be solved by re-emphasizing the checklist to operators — they cannot comply with a step whose prerequisite doesn't exist in front of them. The fix is upstream and usually requires authority beyond the immediate team: standardizing what's provisioned at every site (e.g. bundling the needed materials into a single kit so the precondition is satisfied by default), fixing an access-provisioning gap, or escalating to whoever owns the supply chain or provisioning process. Surfacing this kind of systemic gap is often only possible with executive-level visibility across all the sites or teams running the checklist, since any single team's-eye view looks like an isolated compliance problem.

This precondition audit complements the design guidance in [Runbook and Checklist Design](runbook-checklist-design.md) — a well-designed checklist can still fail in practice if its steps assume resources that aren't actually there.
