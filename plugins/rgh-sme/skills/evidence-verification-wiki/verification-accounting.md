---
type: concept
title: Verification Accounting
description: Structuring verification reporting around subject status, evaluation methodology, and strategy adequacy to provide transparent audit trails.
sources:
  - title: "Taking Testing Seriously"
    resource: "Taking Testing Seriously (James Bach, Michael Bolton), ch. 5"
---

# Verification Accounting

**Verification accounting** is the practice of presenting a complete, empirical narrative of verification work. Reporting only a pass/fail summary forces stakeholders into false security; honest accounting requires communicating status, methodology, and strategy boundaries.

## The Three Verification Narratives
To provide a complete audit trail, a verification report must include three distinct narratives:
1. **The Subject Narrative**: The empirical state of the evaluated system or document. Identifies verified facts, confirmed defects, unexamined areas, and remaining operational risks.
2. **The Verification Narrative**: The detailed methodology used during evaluation. Explains what coverage was achieved, what oracles and reference standards were applied, what configurations were sampled, and what environment constraints blocked testing.
3. **The Strategy Adequacy Narrative**: The justification of why the evaluation was sufficient and responsible. Explicitly details known limitations, blind spots, and assumptions to allow independent reviewers to evaluate validity.

## Activity-Based Audit Trails vs. Metric Distortion
Relying on static artifact counts (such as total test case tallies or percentage pass rates) triggers Goodhart's Law: when a metric becomes a target, it incentivizes superficial checking to hit quotas. Use [qualitative coverage depth](qualitative-coverage-depth.md) tiers instead.
- **Session-Based Logging**: Structure evaluation into time-boxed sessions with explicit charters, detailed execution logs, coverage maps, and debrief notes.
- **Transparent Risk Communication**: Documenting environmental obstacles, unresolved uncertainties, and testing blind spots is essential for technical integrity and ethical verification.
