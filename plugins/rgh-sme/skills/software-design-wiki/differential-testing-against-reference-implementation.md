---
type: concept
title: Differential Testing Against a Reference Implementation
description: >
  Run the same inputs through two implementations of the same behavior and
  assert their outputs match, to validate a replacement or alternative
  implementation without having to independently specify correctness.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 13, Correctness Validation"
---

When two implementations claim to do the same thing — an old parser and its
drop-in replacement, or two libraries under consideration for the same
role — a useful test strategy sidesteps writing new correctness assertions
entirely: generate inputs, run each implementation on the same input, and
assert the outputs agree. A mismatch is the test failure, regardless of
which of the two answers is actually "correct" — the point is confirming
equivalence between old and new, not re-deriving correctness from
scratch.

This is a variant of [characterization testing](characterization-tests.md)
specialized to the migration case: instead of pinning down one
implementation's current behavior in isolation to protect it during a
refactor, a differential test pins down the *relationship* between two
implementations, which is exactly the property that matters when the goal
is a compatible replacement rather than an internal restructuring. It's
especially valuable for esoteric corner cases — compilers testing edge
cases of a language grammar, or a cryptographic library validated against a
shared set of known-attack test vectors that any conformant implementation
must handle the same way — where hand-writing an independent correctness
oracle for every case would be at least as much work as writing the
implementation itself.

The technique composes naturally with randomly generated inputs rather than
only a fixed hand-written set — feeding both implementations the same
generated input surfaces discrepancies that only occur on inputs no one
thought to write down, treating any output mismatch as a failure worth
investigating on its own.
