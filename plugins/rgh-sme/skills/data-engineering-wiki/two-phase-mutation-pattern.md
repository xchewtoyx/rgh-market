---
type: concept
title: Two-Phase Mutation Pattern
description: >
  Writing a pipeline's proposed changes to a temporary store and validating
  them before a separate phase commits anything to the real destination, so a
  canary run can be checked without polluting production output.
sources:
  - title: "The Site Reliability Workbook: Practical Ways to Implement SRE"
    resource: "The Site Reliability Workbook (Google SRE series), ch. 13"
---

Testing a pipeline change safely against real production data runs into a
structural problem: running the new logic against real input and letting it
write straight to the real destination means any bug in the new logic has
already corrupted production output by the time anyone notices — there's no
way to inspect the result before it counts.

The **two-phase mutation** pattern splits a pipeline run into two distinct
phases to close that gap:

1. **Read and transform**: the pipeline runs its full read-and-transform
   logic against real input, but instead of writing to the actual
   destination, it writes its *proposed* mutations to a temporary store.
2. **Validate, then apply**: a separate validation step checks the proposed
   mutations for correctness — comparing them against expected output,
   running [quality screens](quality-screens.md) against them, or diffing
   against what the previous, known-good version of the pipeline would have
   produced for the same input — and only mutations that pass are applied to
   the real destination in a second, distinct pipeline phase.

This is what makes canarying a pipeline change genuinely safe rather than
just probabilistically safe: a canary running the new logic against a slice
of real production traffic writes only to the temporary store during phase
one, so a bug in the new logic produces bad *proposed* mutations that get
caught and discarded in phase two, never bad *committed* output. It's the
pipeline-level analogue of a database transaction's prepare/commit split —
work is fully computed and inspectable before anything becomes irreversible
— applied specifically to validate a pipeline's actual real-world output,
not just its logic in isolation the way a pre-deployment test suite does.

The cost is real: every mutation gets computed and stored twice (once
proposed, once applied) rather than once, and the validation step itself
needs to be trustworthy enough that a pipeline team isn't just moving the
risk of a bad check from "wrong data" to "false confidence in a validation
step that doesn't actually catch the failure mode in question."
