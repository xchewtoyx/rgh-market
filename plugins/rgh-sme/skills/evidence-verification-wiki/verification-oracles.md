---
type: concept
title: Verification Oracles
description: Heuristic consistency principles used by reviewers to identify contradictions, errors, and unstated assumptions in claims.
sources:
  - title: "Taking Testing Seriously"
    resource: "Taking Testing Seriously (James Bach, Michael Bolton), ch. 3"
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 1"
---

# Verification Oracles

A **verification oracle** is any heuristic principle, reference standard, or tool used by a reviewer to recognize errors, contradictions, or unsupported assertions. An oracle provides the benchmark against which observed claims are evaluated for consistency.

## Consistency Heuristics
Reviewers evaluate assertions by testing their consistency against key operational heuristics:
- **Explicit Claims**: Contradictions between the text and official specifications, data sheets, or author statements.
- **Historical Baseline**: Inconsistencies with prior versions, baseline measurements, or established historical records — see [characterization baseline as a verification oracle](characterization-baseline-as-verification-oracle.md) for why a baseline built from nothing but a system's own observed output is still valid evidence of drift, even though it says nothing about correctness.
- **Statutes and Technical Standards**: Non-compliance with governing regulations, industry standards, or protocol specifications.
- **Comparable References**: Discrepancies between the evaluated system and independent reference implementations or competing benchmarks.
- **Physical Reality**: Conflicts with real-world physical constraints, spatial relationships, or verified timelines. A well-established quantitative law can serve the same role for measured data: if load-test throughput and response-time figures combined via Little's Law (queue length = throughput × time-in-system) imply an impossible number of concurrently active requests, the correct inference is that the measurement apparatus is broken (e.g., a client thread pool silently throttling), not that the law has been violated — a trusted formula is itself a consistency oracle against which raw measurements can be checked before they are believed.
- **Internal Self-Consistency**: Contradictions between different sections, figures, or claims within the same document.

## Coded Oracles vs. Human Verification
- **Automated Checks**: Binary assertions encoded into software (such as assertion statements or linter rules). Automated checks can only detect pre-programmed violations.
- **Exploratory Verification**: Human inquiry applying open-ended heuristics to uncover unexpected anomalies, unstated assumptions, and novel failure modes beyond the reach of static checks.

Before trusting any coded oracle's passing result, confirm the oracle can actually fail — see [test oracle self-validation](test-oracle-self-validation.md). A check that has never been observed to fail may simply be incapable of detecting the fault it claims to guard against.
