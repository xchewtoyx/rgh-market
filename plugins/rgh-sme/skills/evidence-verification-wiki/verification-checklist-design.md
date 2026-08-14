---
type: concept
title: Verification Checklist Design
description: Principles for designing concise, practical checklists that prevent critical errors during technical verification.
sources:
  - title: "The Checklist Manifesto"
    resource: "The Checklist Manifesto (Atul Gawande), ch. 2, 6, 8"
---

# Verification Checklist Design

**Verification checklist design** is the discipline of creating focused, operational tools that assist human reviewers without imposing bureaucracy. Effective review checklists guard against critical omissions during high-cognitive-load checks.

## Cognitive Safeguards
Verification checklists protect against two primary human failure modes in complex evaluation:
- **Memory & Attention Degradation**: Human focus fails on routine checks under pressure, fatigue, or high cognitive load. Checklists protect **all-or-none processes** where omitting a single step invalidates the entire verification.
- **Complacency & Step-Skipping**: Expert reviewers lulling themselves into bypassing steps because an error occurs infrequently. Checklists enforce procedural discipline for minimum necessary steps.

## Execution Modes
Verification checklists operate in one of two execution modes:
- **DO-CONFIRM**: Reviewers perform their evaluation independently, then pause at a designated verification gate to confirm that all critical checklist items were satisfied.
- **READ-DO**: Reviewers execute verification checks sequentially as they read each item line by line.

## Core Design Rules
- **Target Killer Items**: Focus exclusively on 5 to 9 critical, high-impact checks ("killer items") that are easily forgotten under cognitive load, rather than trying to spell out every routine step.
- **Strict Time Boundaries**: Structure pause points to take no more than 60 to 90 seconds. Overly long checklists cause fatigue and trigger shortcutting.
- **Visual Ergonomics**: Ensure text is concise, uncluttered, and readable under operational constraints.
- **Empirical Field Validation**: Checklists must be tested in real or simulated verification workflows and refined based on actual reviewer feedback before formal deployment.

## Enforcement & Stopping Power
Checklists require governance authority to be effective:
- **Stopping Power**: Empower reviewers to halt approval or escalation if any mandatory checklist step is skipped.
- **Supply & Environment Verification**: Use checklist non-compliance data to identify upstream system or environment friction blocking thorough verification.

## Two Checklist Types: Procedural and Communication
Effective checklists in complex, multi-party review settings combine two complementary forms, not just one:
- **Procedural (task) checklists** ensure routine, predictable steps are never skipped — the "did we check X" items.
- **Communication checklists** don't specify what the answer should be; they force a mandatory touchpoint between specific parties at a specific moment, so that people with different expertise or context are compelled to compare notes on judgment calls a pure procedural item can't anticipate. A catastrophic near-failure in a real skyscraper's structural design was traced to exactly this gap: a cost-saving substitution passed every procedural check but was never run past the engineer who could have caught its risk, because no step in the process required that conversation to happen.
A checklist limited to procedural items can pass every box while still missing the failure modes that only surface when the right two people actually talk to each other.

## Deriving Checklist Items From Cataloged Past Mistakes
A durable technique for finding an effective set of "killer items" for a verification checklist is to catalogue past verification failures and add a specific check for each one, rather than trying to derive the full list from first principles. Independent groups building due-diligence checklists for investment decisions converged on this same method: one investor built a 70-item checklist directly from cataloguing prior mistakes (their own and others'), including a specific added check — "confirm you have asked whether revenues may be overstated or understated due to boom/bust conditions" — traced back to one identifiable prior failure where reported financial strength turned out to be entirely dependent on a temporary favorable cycle rather than durable performance. A checklist built this way keeps expanding as new, previously-uncaught failure modes are discovered, and should be treated as a living document (carrying a revision date, expected to change) rather than a document finalized once and left alone.

A checklist assembled this way can also unexpectedly *speed up* review rather than slow it down: with clear, pre-identified checkpoints, an evaluator can reach a confident stop/continue decision as soon as the checklist is satisfied or a killer item fails, rather than open-endedly re-examining everything for as long as time allows.

## See Also
- [Cross-Statement Consistency Check](cross-statement-consistency-check.md)
- [Incentive Bias in Verification](incentive-bias-in-verification.md)
