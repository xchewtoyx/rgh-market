---
type: concept
title: Characterization Tests for Undocumented Behavior
description: Writing a test that pins down what a piece of undocumented legacy code currently does, before changing it, so a change can be verified safe without first understanding why the code behaves that way.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery (Humble, Farley), ch. 4"
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

[Hyrum's Law](hyrums-law.md) guarantees that undocumented behavior is still real, depended-upon behavior to somebody — so when a new operator inherits code with no tests and no record of its intended behavior, the honest starting point is not "what should this do" but "what does this actually do right now." A characterization test captures the latter: exercise the existing code, record its current output as the expected result, and commit that test before making any change. The test doesn't assert the code is correct — only that a future change either preserves this exact behavior or changes it deliberately and visibly.

## Why This Is a Handover Technique, Not Just a Testing One

This inverts the usual order of "understand it, then test it." For inherited code with no design record and no author left to ask, full understanding may not be achievable before a change is needed. A characterization test substitutes a mechanical safety net for the missing tacit knowledge: it can't tell a new maintainer *why* the code behaves as it does, but it guarantees that any modification they make either preserves that behavior or forces them to notice, at the moment of the change, that they've altered it. This makes it a way to change a poorly-documented system safely without first fully reconstructing the missing rationale — see [Undocumented Rationale and Zombie Process](undocumented-rationale-and-zombie-process.md) for the related failure mode when nobody ever revisits *why* a behavior exists.

## Mechanics

1. Identify a *seam* — a place where the code's behavior can be observed or altered without editing its internals (a function boundary, an interface, an injectable dependency).
2. Exercise the code through that seam with realistic inputs and record its actual current output, not a hoped-for one.
3. Commit the resulting test as a permanent regression guard.
4. Make the intended change. If the characterization test now fails, that failure is a deliberate signal — confirm the new behavior is intentional before accepting it, rather than treating the red test as a bug to silence.

This complements [External Annotations for Fragile Legacy Systems](external-annotations-for-fragile-legacy-systems.md): annotations document what a component is *for*, while characterization tests document what it *does*, and the two techniques are often needed together on the same fragile, undocumented code.

## A Team Norm, Not Just a Technique

Applied consistently, this becomes a standing rule worth stating explicitly to a team inheriting a system: before using any undocumented legacy method, check whether a characterization test exists for it, and write one first if not. This does double duty as a handover mechanism — a maintainer can read the accumulated characterization tests to learn a method's actual contract, in the same way they might read a runbook, except the tests can't silently drift out of date the way prose notes can.

Contrast this with [Acceptance Tests as Durable Behavior Record](acceptance-tests-as-durable-behavior-record.md): a characterization test is written defensively, after the fact, with no claim the pinned behavior is correct, while an acceptance test is written proactively and does assert the behavior is the intended one.
