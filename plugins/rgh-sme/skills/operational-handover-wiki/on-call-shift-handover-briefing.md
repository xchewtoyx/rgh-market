---
type: concept
title: On-Call Shift Handover Briefing
description: A recurring, structured briefing between outgoing and incoming on-call engineers that transfers in-progress context, not just the pager.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer et al.), ch. 11"
---

On-call responsibility changes hands far more often than system ownership does — every shift, not every few years — but each handoff carries the same risk on a smaller scale: an incoming engineer who doesn't know what's currently in flight will waste time rediscovering it, or miss it entirely.

## What the Briefing Must Cover

A formal shift handover, rather than a silent pager reassignment, should explicitly transfer:

- **Recent changes**: deploys, config pushes, or infrastructure changes in the recent window that could plausibly be an incident's root cause if something breaks next.
- **Open incidents**: anything currently being mitigated or investigated, including what's already been tried and ruled out, so the incoming engineer doesn't repeat dead-end diagnostic paths.
- **Active or recently-firing alerts**: including ones that resolved on their own, since a self-resolved alert is a leading indicator worth watching, not a closed matter.

## Why a Silent Handoff Fails

Without this briefing, the incoming engineer starts every page from zero context, even for a problem the outgoing engineer already partially diagnosed a few hours earlier. This is the same tacit-knowledge-loss failure mode as a full system handover, compressed into a recurring, shift-length cycle — which is exactly why it needs the same discipline of deliberately stating context aloud rather than assuming it will somehow carry over.

For the training that prepares an engineer to act competently once they're holding the pager, see [On-Call Onboarding and Training](on-call-onboarding-and-training.md). For the slower, one-time transition of owning a system rather than a shift, see [Operational Responsibility Transition](operational-responsibility-transition.md).
