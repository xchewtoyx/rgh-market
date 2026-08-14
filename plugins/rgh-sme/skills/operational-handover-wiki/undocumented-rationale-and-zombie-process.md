---
type: concept
title: Undocumented Rationale and Zombie Process
description: A control, gate, or approval step that outlives the reason for its existence because that reason was never written down, turning into pure friction no one can safely remove.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 18"
---

A process control adopted in response to a real past problem is only as removable as its rationale is discoverable. If the reason for a gate, review board, or approval step is never captured anywhere, the control outlives its justification: the organization keeps paying its coordination cost long after the incident that motivated it is forgotten, because no one currently working there can say with confidence that it's now safe to drop.

## The Pattern

A team facing a slow, unexplained approval process traces it back and finds only a vague institutional memory of "some past disaster" — no record of what happened, why the control was the chosen response, or what conditions would make it safe to relax. Unable to prove the control is now unnecessary, everyone defers to it indefinitely, even as its cost (weeks of delay per change, blocked adoption of needed tools) visibly exceeds any plausible remaining benefit. The control survives by inertia and diffused uncertainty, not because anyone can currently justify it.

## Why This Matters for Handover

This is the mirror image of [Unauthorized Substitution Change Control](unauthorized-substitution-change-control.md): that note is about a deviation silently violating an assumption nobody wrote down; this is about a *control* silently persisting because nobody wrote down the assumption that motivated it in the first place. Both failures trace back to the same root cause — reasoning that lived only in someone's head at decision time and was never captured as part of the artifact or process itself.

## The Fix

- **Record the "why," not just the "what," when a new control is adopted**: capture the specific incident or risk that motivated a gate, review requirement, or approval step at the time it's created, alongside the control itself — not just the rule.
- **Ask "why does this exist" before assuming a control must stay**: when a process step's cost is questioned, actively dig for its origin (a "five whys" style trace back to source) rather than defaulting to keeping it because removing an unexplained control feels risky.
- **Retire or replace controls whose rationale can't be reconstructed**: if a control's origin can't be traced and its current cost is clearly out of proportion to any plausible remaining risk, that is itself evidence it is a candidate for removal — not a reason for indefinite caution. Where the underlying risk is real but the manual gate is not, replace it with an [automated guardrail](automated-guardrails-for-safe-changes.md) that enforces the same protection without the compounding coordination cost.
