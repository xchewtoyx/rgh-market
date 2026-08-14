---
type: concept
title: Sensing as a Verification Precondition
description: A claim about an internal computation or effect cannot be checked at all until some channel exists to observe it, so creating that channel is itself part of verification work.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 3"
---

# Sensing as a Verification Precondition

Some claims resist verification not because the evidence is weak, but because there is no way to observe the thing the claim is about in the first place. A component that computes a value or produces an effect entirely inside a closed system — writing to hardware, mutating private state, calling a collaborator with no return value — is a "closed box" from a verifier's perspective: correct or incorrect, it looks identical from outside. **Sensing** is the act of deliberately creating an observation channel where none existed, specifically so a claim about that internal behavior becomes checkable at all.

## The technique

Substitute a recording stand-in for the real collaborator that a computation's effect would otherwise disappear into (a fake network endpoint, a fake display, a fake downstream service), route the code under scrutiny through that stand-in, and inspect what the stand-in captured. The stand-in typically presents two faces: the same interface the real collaborator would offer (so the code under test needs no special-casing) and a separate inspection surface used only by the verifier to read back what happened.

## Why this belongs alongside claim definition, not after it

A claim only counts as [checkable](defining-checkable-claims.md) if a concrete path exists to verify it — sensing is what supplies that path when the system's natural structure offers none. Treating "I can't observe this" as a reason to skip verification concedes the point before starting; treating it as a design problem to solve (build an observation channel) keeps the claim checkable. This differs from [assumption verification via runtime instrumentation](assumption-verification-via-runtime-instrumentation.md), which assumes an observation channel already exists and uses it to check an assumption against live data — sensing is the prior step of getting a channel to exist in the first place, often needed exactly because the code was never built with verification in mind.

## Scope limit

A sensing channel only ever gives evidence about the interaction it was built to observe (e.g., "this component asked the display to show this exact line"), not about everything downstream of it (e.g., whether the real hardware would render that line correctly). This is not a defect unique to sensing — see [claim scope calibration](claim-scope-calibration.md) for why a narrowly scoped check is still valid evidence for the narrower claim it actually covers.
