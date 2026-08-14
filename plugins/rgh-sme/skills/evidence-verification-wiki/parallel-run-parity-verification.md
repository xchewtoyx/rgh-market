---
type: concept
title: Parallel-Run Parity Verification
description: Running an old and new system side by side against the same input and comparing outputs is a direct way to verify equivalence, but the reference oracle it relies on may be a buggy legacy system rather than a correct one.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 1"
---

# Parallel-Run Parity Verification

A claim like "the replacement system behaves the same as the one it's replacing" is hard to verify by reading either system's code — it requires observing both systems' actual outputs against the same real inputs. **Parallel-run parity verification** does this directly: route the same live traffic (or the same batch of records) to both the old and new system simultaneously, without yet cutting users over, and compare the results. Disagreements are evidence of a genuine behavioral difference, which must then be resolved (fix the new system, or confirm the difference is intentional and acceptable) before cutover.

This is the loosely-coupled-systems version of [assumption verification via runtime instrumentation](assumption-verification-via-runtime-instrumentation.md): instead of asserting that two values agree inside one running system, it asserts that two whole systems agree across many real transactions, and treats an instrumentation window with zero observed disagreement as the evidence needed to proceed — not proof, but the best evidence available short of running forever (see [non-conclusive evidence still shifts probability](non-conclusive-evidence-still-shifts-probability.md)).

## The reference oracle can itself be wrong

The subtle failure mode: parallel-run verification checks agreement with the *old system*, not agreement with *correctness* — and the old system is exactly the thing being replaced, often because it has known defects. A verification process that treats "matches the old system" and "is correct" as the same claim will flag a bug fix in the new system as a parity failure.

A worked case from a financial-system replacement illustrates the resolution: the domain required the new system to match the old one "to the penny" before cutover was permitted. During parallel-run comparison, engineers discovered the old system contained a non-standard currency-conversion bug — and rather than treat this as unfixable evidence of nonequivalence, they deliberately reverse-engineered and re-implemented that same bug in the new system, achieved a clean parity match, cut over, and then removed the now-safely-isolated bug as the very first post-cutover change. The verification target was explicitly *behavioral parity*, not correctness; conflating the two would have either blocked a working migration indefinitely or forced an untested simultaneous "migrate and fix a bug" cutover that the parity process was specifically designed to avoid.

## Verification action

Before starting a parallel run, be explicit about which claim it verifies: "produces identical output" or "produces correct output." If the two systems are expected to (and should) diverge on known-defective cases, either exclude those cases from the comparison in advance or route them through a separate fix-then-verify process — do not let an oracle inherited from a known-buggy predecessor silently redefine "correct" as "matches the bug."

## See Also
- [Assumption Verification Via Runtime Instrumentation](assumption-verification-via-runtime-instrumentation.md)
- [Verification Oracles](verification-oracles.md)
- [Characterization Baseline as Verification Oracle](characterization-baseline-as-verification-oracle.md)
